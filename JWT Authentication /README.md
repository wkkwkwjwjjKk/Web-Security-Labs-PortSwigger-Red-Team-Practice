# Lab: JWT Authentication Bypass via Flawed Signature Verification

## Informações do Laboratório

* Plataforma: PortSwigger Web Security Academy
* Categoria: JWT Attacks
* Nível: Apprentice
* Status: Solved

---

## 🎯 Objetivo

Explorar uma falha de implementação no mecanismo de autenticação baseado em JWT para obter acesso ao painel administrativo da aplicação e excluir o usuário `carlos`.

O laboratório demonstra como uma validação incorreta da assinatura de tokens JWT pode permitir que um atacante modifique informações críticas de autenticação e escale privilégios.

---

## 📖 Entendendo a Vulnerabilidade

JWT (JSON Web Token) é amplamente utilizado para autenticação e gerenciamento de sessões.

Um JWT é composto por três partes:

```text
HEADER.PAYLOAD.SIGNATURE
```

### Header

Define o algoritmo utilizado para assinatura.

Exemplo:

```json
{
  "alg": "RS256",
  "typ": "JWT"
}
```

### Payload

Contém as claims (informações) do usuário.

Exemplo:

```json
{
  "sub": "wiener"
}
```

### Signature

Garante a integridade do token.

Quando a assinatura não é validada corretamente pelo servidor, um atacante pode modificar o payload livremente e assumir a identidade de qualquer usuário.

---

## 🔧 Ferramentas Utilizadas

* Burp Suite Community Edition
* Navegador (Firefox / Chrome)
* JWT Editor do Burp Suite
* jwt.io (opcional)

---

## 🔍 Reconhecimento

Após efetuar login com as credenciais fornecidas:

```text
wiener:peter
```

foi possível identificar um JWT armazenado no cookie de sessão.

No Burp Suite:

```text
Proxy → HTTP History
```

Localizei a requisição:

```http
GET /my-account
```

Observando o cookie:

```http
Cookie: session=<JWT>
```

Ao decodificar o token, foi possível visualizar a seguinte claim:

```json
{
  "sub": "wiener"
}
```

A claim `sub` representa o usuário autenticado.

---

## 🚀 Exploração

### 1. Enviar a Requisição para o Repeater

Clique com o botão direito na requisição:

```text
Send to Repeater
```

---

### 2. Testar Acesso ao Painel Administrativo

Alterei o endpoint:

```http
GET /my-account
```

para:

```http
GET /admin
```

A aplicação retornou acesso negado, confirmando que o usuário atual não possui privilégios administrativos.

---

### 3. Modificar o JWT

No painel Inspector do Burp:

Payload original:

```json
{
  "sub": "wiener"
}
```

Payload modificado:

```json
{
  "sub": "administrator"
}
```

Após a alteração:

```text
Apply Changes
```

---

### 4. Falha de Verificação da Assinatura

O servidor não validava corretamente a assinatura do JWT.

Como consequência, a aplicação aceitou o token adulterado mesmo após a modificação do payload.

Isso permitiu assumir a identidade do usuário administrador sem possuir qualquer credencial válida.

---

### 5. Acesso Administrativo

Reenviei a requisição:

```http
GET /admin
```

Desta vez o servidor concedeu acesso ao painel administrativo.

---

### 6. Exclusão do Usuário Carlos

Dentro do painel administrativo foi identificado o endpoint:

```http
/admin/delete?username=carlos
```

Ao acessar essa URL utilizando o JWT adulterado, o usuário `carlos` foi removido com sucesso.

O laboratório foi concluído imediatamente após a exclusão.

---

## ⚠️ Impacto da Vulnerabilidade

Uma falha desse tipo pode permitir:

* Bypass completo da autenticação
* Escalação de privilégios
* Acesso administrativo não autorizado
* Comprometimento total da aplicação
* Manipulação de sessões de outros usuários

Caso explorada em produção, a vulnerabilidade pode resultar na tomada completa do sistema.

---

## 🛡️ Mitigações

Para prevenir esse tipo de falha:

* Validar rigorosamente a assinatura de todos os JWTs
* Aceitar apenas algoritmos previamente definidos
* Utilizar bibliotecas JWT atualizadas
* Implementar controles adicionais de autorização
* Evitar confiar exclusivamente em claims para decisões críticas de acesso
* Monitorar alterações suspeitas em tokens de sessão

---

## 📚 Conceitos Aprendidos

Durante este laboratório foram praticados os seguintes conceitos:

* Estrutura de um JWT
* Header, Payload e Signature
* Claims de autenticação
* Claim `sub`
* Manipulação de tokens JWT
* Verificação de assinatura
* Escalação de privilégios
* Bypass de autenticação
* Análise de sessões utilizando Burp Suite

---

## 🏁 Conclusão

Este laboratório demonstrou como uma implementação incorreta de JWT pode comprometer completamente o mecanismo de autenticação de uma aplicação.

Mesmo utilizando um padrão moderno de autenticação, a ausência de validação adequada da assinatura permite que um atacante modifique informações sensíveis dentro do token e assuma privilégios administrativos.

A principal lição aprendida é que a segurança de um JWT não está apenas em seu formato, mas na verificação correta de sua assinatura e integridade pelo servidor.

✅ Lab resolvido com sucesso.
