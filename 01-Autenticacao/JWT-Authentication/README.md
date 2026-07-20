# 🔐 JWT Authentication – PortSwigger Web Security Academy

## 📌 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Autenticação & Controle de Acesso |
| **Nível de Dificuldade** | Practitioner |
| **Status** | ✅ Resolvido |
| **Data** | Junho 2026 |
| **Ferramentas** | Burp Suite, jwt.io |

---

## 🎯 Objetivo do Laboratório

Compreender vulnerabilidades em implementação de JSON Web Tokens (JWT), incluindo validação fraca de assinatura, manipulação de payload e algoritmos inseguros.

---

## 📖 Resumo Executivo

JWT é amplamente usado em APIs modernas, mas implementações deficientes podem permitir bypass de autenticação através de manipulação de token, algoritmos inseguros ou falha em validação de assinatura.

---

## 📚 Conceitos Teóricos

### O que é JWT?

JSON Web Token é um padrão (RFC 7519) para transmissão segura de claims entre partes. Estrutura:

```
Header.Payload.Signature

Header:    {"alg":"HS256","typ":"JWT"}
Payload:   {"user_id":1,"admin":false}
Signature: HmacSHA256(base64(header)+"."+base64(payload), secret)
```

### Vulnerabilidades Comuns

1. **None Algorithm**: Servidor aceita `alg=none`
2. **Algorithm Confusion**: HS256 vs RS256 (symmetric vs asymmetric)
3. **Weak Secret**: Senha fácil de adivinhar
4. **Missing Validation**: Não valida assinatura
5. **Payload Modification**: Não há verificação de integridade

---

## 🛡️ Mitigação & Defesa

### ✅ Implementação Segura

```python
import jwt
from datetime import datetime, timedelta

# 🟢 Usar algoritmo seguro (RS256, ES256)
secret = secrets.token_bytes(32)

# 🟢 Sempre validar assinatura
def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            secret,
            algorithms=['HS256'],  # 🟢 Whitelist de algoritmos
            options={"verify_signature": True}  # 🟢 Forçar validação
        )
        return payload
    except jwt.InvalidSignatureError:
        return None

# 🟢 Expiração obrigatória
payload = {
    "user_id": 1,
    "exp": datetime.utcnow() + timedelta(hours=1)
}
```

---

## 🔗 Referências

- **RFC**: [RFC 7519 - JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)
- **OWASP**: [JSON Web Token (JWT) Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)
- **CWE**: [CWE-347 - Improper Verification of Cryptographic Signature](https://cwe.mitre.org/data/definitions/347.html)
- **PortSwigger**: [JWT](https://portswigger.net/web-security/jwt)

---

**Autor**: Aislan Silva  
**Status**: ✅ Documentado
