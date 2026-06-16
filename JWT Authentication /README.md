# JWT Attacks – Authentication Bypass Labs

## 📌 Informações Gerais

* Plataforma: PortSwigger Web Security Academy
* Categoria: JWT Attacks
* Nível: Apprentice → Expert
* Ferramentas utilizadas:

  * Burp Suite Community
  * Firefox
  * JWT Editor (Burp Extension)
  * Hashcat
  * OpenSSL
  * Python (PyJWT / jwt_forgery)
  * Linux CLI

---

# 🧠 Visão Geral

Durante estes laboratórios foi explorada a quebra de mecanismos de autenticação baseados em JWT (JSON Web Tokens), abordando falhas em:

* Assinaturas (HS256 / RS256)
* Confiança indevida em headers
* Validação fraca de chaves
* Injeção de parâmetros (`jwk`, `jku`, `kid`)
* Confusão de algoritmos (algorithm confusion)

---

# 1. JWT Authentication Bypass via Unverified Signature

## 🔓 Vulnerabilidade

A aplicação aceitava tokens JWT sem validar a assinatura quando:

```json
{
  "alg": "none"
}
```

---

## 🧪 Exploração

O token foi modificado:

**Payload:**

```json
{
  "sub": "administrator"
}
```

**Header:**

```json
{
  "alg": "none"
}
```

A assinatura foi removida completamente.

---

## 🎯 Resultado

O servidor aceitou o token sem assinatura válida, permitindo acesso como administrador.

Endpoints explorados:

```http
/admin
/admin/delete?username=carlos
```

---

## 📚 Conceitos

* JWT unsigned tokens
* `alg: none`
* Falta de verificação de assinatura
* Privilege escalation

---

# 2. JWT Authentication Bypass via Weak Signing Key

## 🔓 Vulnerabilidade

Uso de chave secreta fraca em tokens HS256.

---

## 🧪 Exploração

Brute force da chave com Hashcat:

```bash
hashcat -a 0 -m 16500 jwt.txt jwt.secrets.list
```

Chave recuperada:

```text
secret1
```

---

## 🎯 Resultado

Token foi reassinado com a chave descoberta, alterando:

```json
{
  "sub": "administrator"
}
```

Acesso administrativo obtido.

---

## 📚 Conceitos

* HS256 (HMAC)
* Brute force de secrets
* Reassinar JWT
* Hashcat mode 16500

---

# 3. JWT Authentication Bypass via JWK Header Injection

## 🔓 Vulnerabilidade

A aplicação aceitava a chave pública fornecida pelo cliente via:

```json
"jwk": { ... }
```

---

## 🧪 Exploração

Geração de chaves RSA:

```bash
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```

Conversão para JWK:

```json
{
  "kty": "RSA",
  "e": "AQAB",
  "n": "..."
}
```

---

## 🎯 Resultado

O servidor utilizou a chave fornecida no JWT para validação, permitindo assinatura válida do atacante.

---

## 📚 Conceitos

* RSA key pairs
* JWK injection
* Trusting client-supplied keys
* RS256 validation bypass

---

# 4. JWT Authentication Bypass via JKU Header Injection

## 🔓 Vulnerabilidade

O servidor aceitava URLs externas no header:

```json
"jku": "https://attacker.com/jwks.json"
```

---

## 🧪 Exploração

Criação de JWKS controlado pelo atacante:

```json
{
  "keys": [
    {
      "kty": "RSA",
      "e": "AQAB",
      "n": "..."
    }
  ]
}
```

---

## 🎯 Resultado

O servidor buscou a chave pública do atacante e validou o JWT malicioso.

---

## 📚 Conceitos

* JWKS (JSON Web Key Set)
* JKU abuse
* Trust boundary violation
* Remote key loading

---

# 5. JWT Authentication Bypass via KID Path Traversal

## 🔓 Vulnerabilidade

O parâmetro `kid` era usado diretamente para localizar arquivos de chave no filesystem.

---

## 🧪 Exploração

Path traversal no header:

```json
{
  "kid": "../../../../../../../dev/null"
}
```

Chave utilizada:

```json
{
  "k": ""
}
```

---

## 🎯 Resultado

O servidor carregou `/dev/null`, invalidando a verificação e permitindo assinatura arbitrária.

---

## 📚 Conceitos

* Path traversal
* File-based key selection
* KID injection
* Key resolution abuse

---

# 6. JWT Authentication Bypass via Algorithm Confusion

## 🔓 Vulnerabilidade

O servidor aceitava RS256 mas podia ser enganado para validar como HS256 usando chave pública como segredo.

---

## 🧪 Exploração

* Obtenção de JWTs válidos
* Derivação da chave pública via `sig2n`
* Conversão para chave simétrica (`kty: oct`)
* Reassinatura do token com HS256

---

## 🎯 Resultado

Token assinado com a chave pública foi aceito como válido, permitindo acesso administrativo.

---

## 📚 Conceitos

* RSA → HMAC confusion
* Key reuse vulnerability
* Signature algorithm downgrade
* Public key as HMAC secret

---

# 🧨 7. JWT Authentication Bypass (No Exposed Key)

## 🔓 Vulnerabilidade

Mesmo sem chave pública exposta, foi possível reconstruí-la a partir de múltiplos tokens.

---

## 🧪 Exploração

* Captura de 2 JWTs válidos
* Uso de ferramenta `jwt_forgery.py` / `sig2n`
* Recuperação matemática da chave pública

---

## 🎯 Resultado

Chave recuperada → assinatura HS256 gerada com sucesso → admin access.

---

## 📚 Conceitos

* Cryptanalysis aplicada
* RSA modulus recovery
* Key derivation from signatures
* Advanced algorithm confusion

---

# 📊 Impacto Geral

Essas falhas permitem:

* Bypass completo de autenticação
* Escalada de privilégios
* Comprometimento de contas admin
* Execução de ações críticas
* Quebra do modelo de confiança do sistema

---

# 🧠 Conhecimentos Consolidado

* JWT structure (Header / Payload / Signature)
* HS256 vs RS256
* Algorithm Confusion attacks
* JWK / JWKS injection
* JKU exploitation
* KID injection / path traversal
* Weak secret brute force
* RSA fundamentals
* Public key abuse as HMAC secret
* Burp Suite JWT Editor
* Cryptographic trust failures

---

## 🔥 Observação final

O ponto mais importante desses labs não é só “explorar JWT”, mas entender que:

> **JWT não é seguro por padrão — a segurança depende totalmente da implementação.**


