
---
## 🔐 2FA Broken Logic –

### 📌 Visão geral

Este laboratório demonstra uma vulnerabilidade de **lógica quebrada na autenticação em dois fatores (2FA)**, onde a aplicação não vincula corretamente o usuário autenticado na primeira etapa ao processo de verificação da segunda etapa.

Como resultado, um atacante pode **alterar o contexto da conta durante a verificação do 2FA**, permitindo acesso a contas de outros usuários.

---

### ⚙️ Fluxo vulnerável

Após o login inicial com usuário e senha, a aplicação define um cookie identificando a conta:

```http id="qk2g5r"
POST /login-steps/first HTTP/1.1
Host: vulnerable-website.com

username=carlos&password=qwerty
```

Resposta:

```http id="v1m8xk"
HTTP/1.1 200 OK
Set-Cookie: account=carlos
```

Na segunda etapa, o sistema usa esse cookie para determinar qual conta está sendo verificada:

```http id="7p0tld"
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=carlos

verification-code=123456
```

---

### 🚨 Exploração da vulnerabilidade

O problema é que o cookie `account` é controlado pelo cliente e não está corretamente ligado à sessão autenticada.

Um atacante pode modificar esse valor antes de enviar o código de verificação:

```http id="x9d3aa"
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=victim-user

verification-code=123456
```

Se o código 2FA puder ser brute force, isso permite o acesso a contas de qualquer usuário.

---

### 💥 Impacto

* Bypass completo da autenticação em dois fatores
* Acesso não autorizado a contas de outros usuários
* Possibilidade de brute force no código de verificação
* Falha na associação entre sessão e autenticação

---

### 🛠️ Causa raiz

A aplicação não associa corretamente o estado do 2FA à sessão no servidor. Em vez disso, confia em um valor controlado pelo cliente (`cookie account`) para identificar o usuário durante a verificação.

---

### 🔒 Correção

* Vincular o estado do 2FA à sessão no servidor
* Não confiar em cookies ou parâmetros controlados pelo cliente para identificar usuários
* Garantir que o código de verificação esteja associado à sessão autenticada na primeira etapa

---

Se quiser, posso te ajudar a transformar isso num **repositório completo de PortSwigger write-ups (com estrutura, pastas por lab e padrão profissional)**.
