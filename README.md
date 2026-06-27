# 🔒 Web Security Labs – PortSwigger Red Team Practice

[![Progress](https://img.shields.io/badge/Progress-75%25-brightgreen?style=flat-square)](https://github.com/wkkwkwjwjjKk/Web-Security-Labs-PortSwigger-Red-Team-Practice)
[![Labs](https://img.shields.io/badge/Labs-15%2F20-blue?style=flat-square)](https://github.com/wkkwkwjwjjKk/Web-Security-Labs-PortSwigger-Red-Team-Practice)
[![Status](https://img.shields.io/badge/Status-Active-green?style=flat-square)](https://github.com/wkkwkwjwjjKk/Web-Security-Labs-PortSwigger-Red-Team-Practice)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](./LICENSE)

Documentação completa de **20+ laboratórios práticos** de segurança ofensiva web, com foco em exploração manual, análise de vulnerabilidades e desenvolvimento de raciocínio atacante.

> **Nível**: Intermediário → Avançado | **Plataforma**: PortSwigger Web Security Academy | **Linguagem**: Português (PT-BR)

---

## 📊 Status Geral do Repositório

```
████████████░░░░░░░░░░ 75% Completo (15/20 labs documentados)
```

| Status | Quantidade | Percentual |
|--------|-----------|-----------|
| ✅ **Concluído** | 12 | 60% |
| 🟡 **Em Progresso** | 3 | 15% |
| 🔴 **Não Iniciado** | 5 | 25% |

---

## 🚀 Comece Rápido

### Por Seu Nível

**🟢 Iniciante em Web Security**
```
1. Leia: Authentication Vulnerabilities
2. Resolva: Password-Based Login labs
3. Teste: Força bruta simples
```
**Tempo**: ~4 horas

**🟠 Intermediário**
```
1. Explore: SQL Injection (9 labs)
2. Teste: CSRF + SSRF
3. Domine: API Security
```
**Tempo**: ~15 horas

**🔴 Avançado**
```
1. Estude: JWT Attacks (cryptanalysis)
2. Domine: XXE + SSTI
3. Explore: Deserialization
```
**Tempo**: ~20 horas

---

## 🎓 Mapa Completo de Estudos

### **Trilha 1: Autenticação & Acesso** (Iniciante)

```
🟢 Password-Based-Login/
   └─ 7 labs ✅ | Username enumeration, brute-force bypass, rate limiting
   
🟢 Authentication-Vulnerabilities/
   └─ 6 labs ✅ | 2FA bypass, logic flaws, HTTP Basic Auth
   
🟢 2FA-Broken-Logic/
   └─ 1 lab ✅ | Cookie manipulation, 2FA bypass
   
🟢 OAuth & OpenID Labs/
   └─ 5 labs ✅ | Implicit flow, SSRF, token stealing, redirect_uri bypass
```

**Tempo Total**: 4.5 horas | **Tópicos Chave**: Enumeração, Brute-force, 2FA, OAuth
**[→ Acessar Trilha 1](./1-Authentication/)**

---

### **Trilha 2: Injection Attacks** (Intermediário)

```
🟢 SQL-Injection/
   └─ 9 labs ✅ | UNION, Blind, WAF bypass, XML/JSON SQLi
   
🟡 Blind-SQL-Injection/
   └─ 5 labs ⏳ | Boolean-based, Time-based, OAST, Cryptanalysis
   
🔴 Command-Injection/
   └─ 3 labs ❌ | Blind command injection, Time-based, OOB exfiltration
   
🔴 XXE-Injection/
   └─ 5 labs ❌ | XXE básico, Blind XXE, XXE + SSRF, XXE + File Upload
```

**Tempo Total**: 20 horas | **Tópicos Chave**: SQLi, Blind techniques, OAST
**[→ Acessar Trilha 2](./2-Injection/)**

---

### **Trilha 3: Web Requests & Logic** (Intermediário)

```
🟢 CSRF/
   └─ 2 labs ✅ | CSRF token bypass, GET vs POST validation
   
🟡 SSRF/
   └─ 7 labs (4 resolvidos) 🟡 | Blind OAST, Shellshock, Whitelist bypass
   
🔴 HTTP-Request-Smuggling/
   └─ 4 labs ❌ | TE.CL, CL.TE, Morphing, Response queue poisoning
```

**Tempo Total**: 18 horas | **Tópicos Chave**: CSRF, SSRF, HTTP Smuggling
**[→ Acessar Trilha 3](./4-Web-Requests/)**

---

### **Trilha 4: API & Autorização** (Intermediário → Avançado)

```
🟢 API-Security-SSPP/
   └─ 5 labs ✅ | Mass Assignment, Parameter Pollution (Query & REST)
   
🟢 Access-Control/
   └─ 8 labs ✅ | IDOR, Privilege Escalation, Multi-step workflows
   
🟢 JWT-Authentication/
   └─ 7 labs ✅ | Algorithm confusion, JWK/JKU injection, Cryptanalysis
```

**Tempo Total**: 16 horas | **Tópicos Chave**: API exploitation, IDOR, JWT attacks
**[→ Acessar Trilha 4](./5-API-Security/)**

---

### **Trilha 5: Avançado** (Avançado)

```
🔴 SSTI/
   └─ 4 labs ❌ | Jinja2, Mako, Freemarker, RCE via template
   
🔴 Insecure-Deserialization/
   └─ 5 labs ❌ | Java, Python, PHP serialization, Gadget chains
   
🔴 Business-Logic-Flaws/
   └─ 8 labs ❌ | Race conditions, Price manipulation, State machine
   
🔴 Web-Cache-Poisoning/
   └─ 3 labs ❌ | Cache key injections, Header poisoning
```

**Tempo Total**: 25 horas | **Tópicos Chave**: SSTI, Deserialization, Logic flaws
**[→ Acessar Trilha 5](./6-Advanced/)**

---

## 📈 Progresso Detalhado por Categoria

### ✅ Concluído com Qualidade Alta (12 Labs)

| Categoria | Status | Labs | Nível |
|-----------|--------|------|-------|
| **SQL Injection** | ✅ 9/9 | UNION, Blind, XML/JSON, WAF bypass | Apprentice → Expert |
| **JWT Attacks** | ✅ 7/7 | Algorithm confusion, JWK/JKU, Cryptanalysis | Apprentice → Expert |
| **API Security** | ✅ 5/5 | Mass Assignment, SSPP Query & REST | Apprentice → Expert |
| **CSRF** | ✅ 2/2 | Sem proteção, Validação por método | Apprentice |
| **Authentication** | ✅ 6/6 | Username enum, Brute-force, Rate limiting | Practitioner |
| **OAuth & OpenID** | ✅ 5/5 | Implicit flow, Dynamic registration, Token stealing | Practitioner |
| **2FA Broken Logic** | ✅ 1/1 | Cookie manipulation | Apprentice |

---

### 🟡 Em Andamento (3 Labs)

| Categoria | Status | Faltam | Próximo Passo |
|-----------|--------|--------|---------------|
| **SSRF Labs** | 🟡 4/7 | Blind OAST, Shellshock, Whitelist | Estudar OAST + Burp Collaborator |
| **Blind SQL** | 🟡 Teórico | 5 labs práticos | Resolver labs boolean/time-based |
| **Access Control** | 🟡 Conceitual | 8 labs práticos | Explorar IDOR + privilege escalation |

---

### 🔴 Não Iniciado (5 Trilhas)

| Trilha | Labs | Dificuldade | Pré-Requisito |
|--------|------|------------|---------------|
| **Command Injection** | 3 | Practitioner | SQL Injection |
| **XXE Injection** | 5 | Practitioner | XML basics |
| **SSTI** | 4 | Practitioner | Web frameworks |
| **Insecure Deserialization** | 5 | Expert | Serialization concepts |
| **Business Logic** | 8 | Practitioner | Lógica de aplicação |

---

## 💡 Conceitos por Trilha

### Trilha 1: Autenticação
- ✅ Username enumeration (3 métodos)
- ✅ Brute-force com rate limiting bypass
- ✅ 2FA com cookies mal vinculados
- ✅ OAuth implicit flow + redirect_uri bypass
- ✅ SSRF via OpenID registration

**Aprendizado Chave**: Autenticação não é só senha, é validação de identidade em múltiplas camadas

---

### Trilha 2: Injection
- ✅ UNION SELECT para extração
- ✅ Blind SQLi (boolean + time-based)
- ✅ WAF bypass com encoding XML/JSON
- ⏳ OAST (Out-of-Band Application Security Testing)
- ⏳ Command injection via DNS exfiltration

**Aprendizado Chave**: Dados controlados pelo usuário = vetores de ataque

---

### Trilha 3: Web Requests
- ✅ CSRF token validation flaws
- ✅ SSRF contra localhost + internal services
- ✅ Open redirect chaining
- ⏳ HTTP Request Smuggling (TE.CL, CL.TE)

**Aprendizado Chave**: Requisições HTTP podem ser manipuladas de formas criativas

---

### Trilha 4: API & Autorização
- ✅ Mass Assignment (object property injection)
- ✅ SSPP (Server-Side Parameter Pollution)
- ✅ IDOR (Insecure Direct Object Reference)
- ✅ JWT cryptographic flaws

**Aprendizado Chave**: APIs precisam validar não só autenticação, mas autorização

---

### Trilha 5: Avançado
- ❌ SSTI (Template injection com RCE)
- ❌ Deserialization gadget chains
- ❌ Business logic race conditions
- ❌ Cache poisoning attacks

**Aprendizado Chave**: Vulnerabilidades complexas requerem entendimento profundo da aplicação

---

## 🛠️ Ferramentas Utilizadas

- **Burp Suite Professional** – Proxy, Repeater, Intruder, JWT Editor, Collaborator
- **Browser DevTools** – Network, Console, Storage, Sources
- **Python 3** – Scripts de automação (JWT, SQLi, encoding)
- **curl / wget** – Requisições HTTP diretas
- **Hashcat** – Brute force de secrets
- **OpenSSL** – Geração de chaves RSA
- **nmap / rustscan** – Port scanning
- **gobuster / dirb** – Directory enumeration

---

## 📚 Referências Técnicas Completas

### Especificações & Padrões
- [RFC 6749 – OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
- [RFC 6819 – OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/rfc6819)
- [RFC 3986 – URI Generic Syntax](https://datatracker.ietf.org/doc/html/rfc3986)
- [RFC 7519 – JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)
- [RFC 6265 – HTTP State Management Mechanism](https://datatracker.ietf.org/doc/html/rfc6265)

### Segurança & Vulnerabilidades
- [OWASP Top 10](https://owasp.org/Top10/)
- [OWASP CWE Top 25](https://cwe.mitre.org/top25/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

### Plataformas & Recursos
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) – 100+ labs práticos
- [OWASP CheatSheets](https://cheatsheetseries.owasp.org/)
- [HackTricks](https://book.hacktricks.xyz/)

---

## 🎯 Roadmap Futuro

### Q3 2026 (Próximas 8 Semanas)

```
Semana 1-2:  Complete SSRF (últimos 3 labs)
Semana 3-4:  Documenta Blind SQL Injection (5 labs práticos)
Semana 5-6:  Resolva Command Injection (3 labs)
Semana 7-8:  Inicie XXE Injection (5 labs)
```

### Q4 2026

```
Semana 1-4:  SSTI + Deserialization (9 labs)
Semana 5-8:  Business Logic Flaws (8 labs)
```

### Objetivo Final
- ✅ 20+ labs 100% documentados
- ✅ Portfólio pronto para apresentação
- ✅ Nível: Avançado (9/10)

---

## 🤝 Como Contribuir

Encontrou um erro? Quer melhorar a documentação?

1. **Fork** o repositório
2. **Crie uma branch**: `git checkout -b feature/melhoria`
3. **Commit**: `git commit -m "docs: melhoria na documentação de SQL Injection"`
4. **Push**: `git push origin feature/melhoria`
5. **Abra um Pull Request**

---

## 📊 Estatísticas do Repositório

- **Labs Concluídos**: 12/20 (60%)
- **Horas de Estudo**: ~150h estimadas
- **Tópicos Cobertos**: 15+ categorias de segurança
- **Versão Atual**: 1.0 (em desenvolvimento)
- **Última Atualização**: Junho 2026

---

## 📌 Notas Importantes

⚠️ **Disclaimer Legal**

Todos os testes foram realizados **exclusivamente em ambientes controlados** da PortSwigger Web Security Academy, com propósito **educacional e de pesquisa**.

**Não use** essas técnicas em sistemas que você não possua ou não tenha autorização explícita por escrito.

---

## 🎓 Estrutura de Aprendizado Recomendada

### **Caminho 1: Seguro (Recomendado)**
```
1. Autenticação (4h) ─→ Injection (20h) ─→ Web Requests (18h)
   ↓
2. API & Autorização (16h) ─→ Avançado (25h)

Total: ~85 horas | Duração: 3-4 meses
```

### **Caminho 2: Aprofundado**
```
1. Autenticação (4h) ─→ SQL Injection (intensivo)
   ├─ UNION attacks
   ├─ Blind SQLi + OAST
   └─ WAF bypass

2. API Security ─→ JWT Cryptanalysis ─→ Avançado
```

### **Caminho 3: Focado em Bug Bounty**
```
Prioridade: IDOR → SSRF → API Security → XXE → SSTI
(Foco no impacto prático e real)
```

---

## 📞 Contato & Suporte

- **Autor**: Aislan Silva
- **GitHub**: [@wkkwkwjwjjKk](https://github.com/wkkwkwjwjjKk)
- **Repositório**: [Web-Security-Labs-PortSwigger-Red-Team-Practice](https://github.com/wkkwkwjwjjKk/Web-Security-Labs-PortSwigger-Red-Team-Practice)

---

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](./LICENSE).

Sinta-se livre para:
- ✅ Usar como referência pessoal
- ✅ Compartilhar com fins educacionais
- ✅ Adaptar e melhorar
- ✅ Citar em seus próprios portfólios

Mantenha a atribuição original quando compartilhar.

---

## ⭐ Se Esse Repositório Foi Útil

Deixe uma ⭐ no GitHub! Ajuda outros pesquisadores a descobrir.

---

**Última Atualização**: 27 de Junho de 2026  
**Status**: 🟢 Ativo e em desenvolvimento  
**Próximo Milestone**: 20 labs 100% documentados
