
# 📝 OAuth & OpenID Connect Labs Write-ups
**Plataforma**: PortSwigger Web Security Academy  
**Níveis**: Apprentice / Practitioner  
**Status**: ✅ Todos resolvidos  
**Baseado em**: RFC 6749, RFC 6819, OpenID Connect Core 1.0

---

## 📋 Índice
- [OAuth Implicit Flow Authentication Bypass](#oauth-implicit-flow-authentication-bypass)
- [SSRF via OpenID Dynamic Client Registration](#ssrf-via-openid-dynamic-client-registration)
- [Forced OAuth Profile Linking](#forced-oauth-profile-linking)

---

## 🔓 OAuth Implicit Flow Authentication Bypass
**Nível**: Apprentice

### 🎯 Objetivo
Contornar o mecanismo de autenticação e assumir a identidade de outros usuários explorando uma implementação insegura do fluxo implícito do OAuth 2.0.

### 📚 Contexto Técnico
O **Fluxo Implícito (`response_type=token`)** foi originalmente projetado para aplicações do lado do cliente (ex: JavaScript no navegador). Nesse fluxo, o token de acesso é retornado diretamente na **parte de fragmento da URL** (`#`), sem passar por troca de segredos no servidor.

Como o fragmento não é enviado ao servidor, a aplicação **deve validar rigorosamente o token recebido**. Quando essa validação é negligenciada, o sistema confia cegamente nos dados enviados pelo usuário, permitindo manipulação.

### 🔍 Passo a Passo da Exploração
1. Acesse a página de login e escolha a opção **"Entrar com OAuth"**.
2. Após autorizar o provedor, observe a URL de retorno:
   ```
   https://alvo.com/callback#access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```
3. Verifique que o token é um **JWT** e que a aplicação não valida:
   - Assinatura criptográfica
   - Emissor (`iss`) e destinatário (`aud`)
   - Data de validade (`exp` e `iat`)
4. Modifique o valor do identificador do usuário (`sub`) ou gere um token próprio com dados arbitrários.
5. Recarregue a página — a aplicação aceita o token e concede acesso à conta associada ao novo valor.

### ⚠️ Causa da Vulnerabilidade
- Uso inadequado do Fluxo Implícito em aplicações com capacidade de manter segredos.
- Falta total de validação do token de acesso no lado do servidor.
- Confiança excessiva em dados controlados pelo cliente.
- Descumprimento das recomendações de segurança da [RFC 6819](https://datatracker.ietf.org/doc/html/rfc6819) e da especificação do OpenID Connect.

### ✅ Medidas de Correção
- Substitua o Fluxo Implícito pelo **Fluxo de Código de Autorização (`response_type=code`)**, preferencialmente com o **PKCE** para maior segurança.
- Sempre valide: assinatura, emissor, público-alvo, validade e escopo do token recebido.
- Nunca use tokens de acesso para decisões críticas sem verificação criptográfica.

---

## 🕳️ SSRF via OpenID Dynamic Client Registration
**Nível**: Practitioner

### 🎯 Objetivo
Explorar o recurso de **registro dinâmico de clientes** do OpenID Connect para realizar um ataque de **SSRF (Server-Side Request Forgery)**, fazendo com que o servidor acesse endereços internos ou restritos.

### 📚 Contexto Técnico
O registro dinâmico permite que novos clientes se cadastrem no provedor OpenID enviando uma requisição JSON com configurações, incluindo URLs como `logo_uri`, `policy_uri` ou `tos_uri`. Conforme a especificação [OpenID Connect Dynamic Client Registration](https://openid.net/specs/openid-connect-registration-1_0.html), o provedor pode buscar esses recursos para validação ou exibição.

Se não houver restrição sobre quais endereços podem ser acessados, o atacante pode forçar o servidor a consultar:
- Endereços de loopback (`127.0.0.1`, `localhost`)
- Redes privadas internas
- Serviços de metadados de nuvem (`169.254.169.254`)

### 🔍 Passo a Passo da Exploração
1. Identifique o endpoint de registro dinâmico:
   ```http
   POST /openid/register
   Content-Type: application/json
   ```
2. Envie uma requisição com uma URL controlada:
   ```json
   {
     "client_name": "TesteSeguranca",
     "redirect_uris": ["https://exemplo.com/callback"],
     "logo_uri": "http://127.0.0.1/admin"
   }
   ```
3. O servidor tentará acessar o endereço informado para verificar ou carregar o recurso.
4. Teste outros alvos:
   - `http://localhost`
   - `http://169.254.169.254` (metadados AWS)
   - `http://192.168.0.1` (rede interna)
5. Analise as respostas: diferenças no tempo de resposta, mensagens de erro ou conteúdo retornado confirmam o SSRF.

### ⚠️ Causa da Vulnerabilidade
- Ausência de filtros de validação nas URLs recebidas no cadastro.
- Permissão do servidor de sair para redes privadas, locais ou serviços de metadados.
- Falta de regras de acesso de rede para o provedor de identidade.

### ✅ Medidas de Correção
- Bloqueie IPs de loopback, redes privadas e faixas reservadas por padrão.
- Restrinja o acesso de saída do servidor apenas a domínios confiáveis.
- Valide o esquema (`https` apenas) e o domínio das URLs enviadas.
- Implemente listas de permissões (whitelist) em vez de bloqueios genéricos.

---

## 🔗 Forced OAuth Profile Linking
**Nível**: Practitioner

### 🎯 Objetivo
Fazer com que um usuário legítimo vincule involuntariamente sua conta na aplicação a uma conta OAuth controlada pelo atacante. Após a vinculação, o atacante consegue acessar a conta da vítima usando suas próprias credenciais.

### 📚 Contexto Técnico
A funcionalidade de **vinculação de contas** permite associar uma conta local a um provedor de identidade externo. Para evitar ataques CSRF e manipulação, o fluxo deve usar o parâmetro `state` conforme definido na [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749) e na especificação [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest).

Quando o `state` é fixo, previsível ou não vinculado à sessão do usuário, é possível criar um link malicioso e fazer com que a vítima finalize a vinculação sem perceber.

### 🔍 Passo a Passo da Exploração
1. Crie sua conta e inicie o processo de vinculação com seu provedor OAuth. Observe a estrutura da URL:
   ```
   GET /oauth/link?client_id=XYZ&redirect_uri=https://alvo.com/callback&state=12345
   ```
2. Verifique que o valor de `state` é sempre o mesmo ou pode ser facilmente adivinhado.
3. Monte o link final de vinculação usando os parâmetros obtidos e mantenha seu OAuth autorizado.
4. Envie esse link para a vítima. Se ela estiver logada em sua conta na aplicação, ao acessar o URL, a vinculação será concluída automaticamente.
5. Agora, ao usar sua própria conta OAuth, você será autenticado diretamente na conta da vítima.

### ⚠️ Causa da Vulnerabilidade
- Uso incorreto ou ausência do parâmetro `state` para proteger o fluxo.
- Falta de confirmação explícita do usuário antes de realizar a vinculação.
- Não associação do estado da requisição à sessão do usuário atual.
- Ausência de validação de permissão para alterar a conta.

### ✅ Medidas de Correção
- Gere o parâmetro `state` com valor **aleatório, único e de alta entropia** para cada requisição.
- Armazene esse valor associado à sessão do usuário e valide-o no retorno.
- Sempre exija confirmação ou senha antes de vincular ou desvincular contas.
- Verifique que o usuário logado é o mesmo que iniciou o fluxo.

---

## 📚 Referências Oficiais
- [OAuth 2.0 Authorization Framework (RFC 6749)](https://datatracker.ietf.org/doc/html/rfc6749)
- [OAuth 2.0 Security Best Current Practice (RFC 6819)](https://datatracker.ietf.org/doc/html/rfc6819)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
- [OpenID Connect Dynamic Client Registration](https://openid.net/specs/openid-connect-registration-1_0.html)
- [PortSwigger Web Security Academy — OAuth](https://portswigger.net/web-security/oauth)
```

