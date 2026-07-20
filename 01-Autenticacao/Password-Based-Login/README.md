# 🔐 Password-Based Login – PortSwigger Web Security Academy

## 📌 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Autenticação & Controle de Acesso |
| **Nível de Dificuldade** | Apprentice |
| **Status** | ✅ Resolvido |
| **Data** | Maio 2026 |
| **Ferramentas** | Burp Suite, Browser |

---

## 🎯 Objetivo do Laboratório

Compreender e explorar vulnerabilidades em sistemas de login baseados em senha, incluindo bypass de autenticação e enumeração de usuários.

---

## 📖 Resumo Executivo

Laboratório focado em autenticação básica com senhas, explorando falhas na validação de credenciais e implementação de proteções inadequadas contra força bruta.

---

## 📚 Conceitos Teóricos

### O que é Login Baseado em Senha?

Mecanismo fundamental onde:
1. Usuário envia username e senha
2. Sistema valida contra banco de dados
3. Sessão é criada se credenciais forem corretas

### Vulnerabilidades Comuns

- Senhas armazenadas em plain text
- Falta de proteção contra brute force
- Mensagens de erro que revelam informações
- Validação inadequada de entrada

---

## 🛡️ Mitigação & Defesa

### ✅ Implementação Segura

- Hash de senha com salt (bcrypt, argon2)
- Rate limiting por usuário
- Mensagens de erro genéricas
- Logging de tentativas falhadas

---

## 🔗 Referências

- **OWASP**: [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- **CWE**: [CWE-287 - Improper Authentication](https://cwe.mitre.org/data/definitions/287.html)
- **PortSwigger**: [Authentication](https://portswigger.net/web-security/authentication)

---

**Autor**: Aislan Silva  
**Status**: ✅ Documentado
