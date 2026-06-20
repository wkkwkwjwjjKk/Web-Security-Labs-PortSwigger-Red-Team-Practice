
---

```markdown
# OAuth & OpenID Labs Write-ups
**Plataforma**: PortSwigger Web Security Academy
**Níveis**: Apprentice / Practitioner
**Status**: ✅ Resolvidos

---

## 📋 Índice
- [OAuth Implicit Flow Authentication Bypass](#oauth-implicit-flow-authentication-bypass)
- [SSRF via OpenID Dynamic Registration](#ssrf-via-openid-dynamic-registration)
- [Forced OAuth Profile Linking](#forced-oauth-profile-linking)

---

## OAuth Implicit Flow Authentication Bypass
**Nível**: Apprentice

### 🎯 Objetivo
Contornar a autenticação e acessar contas de outros usuários explorando falhas no fluxo implícito do OAuth.

### 📝 Contexto
No fluxo implícito, o token de acesso é retornado diretamente na URL. Se a aplicação confiar cegamente no token sem realizar validações adequadas, é possível manipulá-lo para assumir a identidade de outro usuário.

### 🔍 Passo a Passo
1. Acesse a página de login e selecione a opção "Entrar com OAuth".
2. Após autorizar o provedor, observe a URL de retorno:
   ```
   https://alvo.com/callback#access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```
3. Verifique que não há validação de assinatura, emissor ou validade do token.
4. Altere o identificador de usuário ou modifique o valor do token.
5. Recarregue a página — o acesso à conta alvo é concedido.

### ⚠️ Causa da Vulnerabilidade
- Uso inseguro do fluxo implícito.
- Falta de validação do token no lado do servidor.
- Confiança excessiva em dados recebidos do cliente.

### ✅ Correção / Boas Práticas
- Utilize o Fluxo de Código de Autorização com PKCE.
- Sempre valide assinatura, emissor, validade e escopo do token.

---

## SSRF via OpenID Dynamic Registration
**Nível**: Practitioner

### 🎯 Objetivo
Realizar um ataque de SSRF explorando o recurso de registro dinâmico de clientes no OpenID Connect.

### 📝 Contexto
O registro dinâmico permite enviar configurações em formato JSON, incluindo URLs como `logo_uri` ou `policy_uri`. Se o provedor acessar esses endereços sem restrições, pode ser forçado a consultar serviços e recursos da rede interna.

### 🔍 Passo a Passo
1. Identifique o endpoint de registro dinâmico:
   ```
   POST /openid/register
   Content-Type: application/json
   ```
2. Envie a requisição com uma URL interna:
   ```json
   {
     "client_name": "Test",
     "redirect_uris": ["https://exemplo.com/callback"],
     "logo_uri": "http://127.0.0.1/admin"
   }
   ```
3. O servidor tentará acessar o endereço informado.
4. Teste outros endereços: `http://localhost`, `http://169.254.169.254`, etc.
5. A resposta da aplicação confirma o acesso, provando a existência do SSRF.

### ⚠️ Causa da Vulnerabilidade
- Ausência de filtro e validação das URLs enviadas.
- Permissão do servidor para acessar endereços de redes internas.

### ✅ Correção / Boas Práticas
- Bloqueie IPs de loopback, redes privadas e serviços de metadados.
- Restrinja o acesso de saída do servidor apenas para domínios confiáveis.

---

## Forced OAuth Profile Linking
**Nível**: Practitioner

### 🎯 Objetivo
Fazer com que um usuário vincule involuntariamente sua conta a uma conta OAuth controlada pelo atacante, permitindo acesso posterior à conta da vítima.

### 📝 Contexto
A funcionalidade de vinculação de contas é vulnerável se não houver proteção adequada contra manipulação do fluxo e do estado da sessão.

### 🔍 Passo a Passo
1. Crie sua própria conta e vincule-a ao seu provedor OAuth. Observe a estrutura da URL:
   ```
   GET /oauth/link?client_id=...&redirect_uri=...&state=XYZ123
   ```
2. Verifique que o parâmetro `state` não é seguro, não é único ou não está vinculado à sessão do usuário.
3. Monte um link de vinculação usando suas credenciais OAuth.
4. Envie o link para a vítima; ao acessá-lo já logada em sua conta, a vinculação é feita automaticamente.
5. Agora é possível acessar a conta da vítima usando suas próprias credenciais OAuth.

### ⚠️ Causa da Vulnerabilidade
- Parâmetro `state` mal implementado ou ausente.
- Falta de confirmação explícita antes de vincular contas.
- Não validação da identidade do usuário durante a operação.

### ✅ Correção / Boas Práticas
- Use o parâmetro `state` com valor único, aleatório e associado à sessão.
- Sempre peça confirmação ou senha antes de realizar alterações na conta.
- Valide a sessão e a permissão do usuário em cada etapa.

---

## 📚 Referências
- [OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/rfc6819)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
- [PortSwigger Web Security Academy - OAuth](https://portswigger.net/web-security/oauth)
```

---

