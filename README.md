# Web Security Labs - PortSwigger Web Security Academy

Repositório dedicado aos meus estudos práticos em **Application Security (AppSec)** e exploração manual de vulnerabilidades web.

**Autor:** Aislan Silva  
**Última atualização:** Maio de 2026  
**Foco:** Pentest Web / Bug Bounty / Exploração de APIs

---

## 🎯 Objetivo

Documentar minha evolução prática em segurança ofensiva, com foco em:

- Exploração manual de vulnerabilidades em aplicações web e APIs
- Resolução de laboratórios da PortSwigger Web Security Academy
- Desenvolvimento de raciocínio ofensivo (attack thinking)
- Criação e adaptação de payloads
- Análise de requisições HTTP com Burp Suite

---

## 🧠 Resumo Técnico (Visão Prática)

Experiência aplicada em:

- Interceptação e manipulação de tráfego HTTP/HTTPS
- Enumeração de endpoints e superfícies de ataque
- Exploração de falhas lógicas em APIs
- Bypass de controles de autenticação e autorização
- Análise de código client-side (JavaScript)
- Testes manuais com Burp Suite (Repeater, Intruder, Proxy)

---

## 🛡️ Vulnerabilidades Exploradas (Hands-on)

### SQL Injection
- Authentication bypass via SQLi
- UNION-based extraction
- Blind SQLi (boolean-based e time-based)
- Conditional responses exploitation
- Database enumeration (`information_schema`)
- WAF bypass techniques

### SSRF (Server-Side Request Forgery)
- Basic SSRF exploitation
- SSRF contra localhost/internal services
- Bypass de blacklist e whitelist filters
- SSRF via Open Redirect chaining

### Access Control (Broken Authorization)
- IDOR (Insecure Direct Object Reference)
- Vertical e horizontal privilege escalation
- Admin panel bypass
- Referer-based access control bypass
- Multi-step workflow bypass

### Command Injection
- Blind command injection
- Time-based detection techniques
- Out-of-Band (OAST) exfiltration
- Output redirection exploitation

### File Upload Vulnerabilities
- Web shell upload
- Bypass de whitelist/blacklist
- Content-Type manipulation
- Extension obfuscation
- Path traversal via upload features

### Authentication Vulnerabilities
- Username enumeration
- Broken brute-force protection
- Logic flaws em login flows
- Bypass de MFA/2FA em cenários específicos

### API Security
- API endpoint discovery via documentation
- Exploração de endpoints não utilizados
- Mass Assignment (object property injection)
- Server-Side Parameter Pollution (SSPP - Query e REST path)

---

## 📊 Progresso em Labs

| Categoria | Dificuldade | Status |
|-----------|------------|--------|
| SQL Injection | Apprentice → Expert | ✅ Concluído |
| SSRF | Practitioner | ✅ Concluído |
| Access Control | Apprentice → Practitioner | ✅ Concluído |
| Command Injection | Practitioner | ✅ Concluído |
| File Upload | Practitioner | ✅ Concluído |
| Authentication | Practitioner | ✅ Concluído |
| API Security & SSPP | Apprentice → Expert | 5+ labs resolvidos |

---

## 🛠️ Ferramentas Utilizadas

- Burp Suite Professional (Proxy, Repeater, Intruder)
- Browser DevTools (Network / Sources)
- Hackvertor
- Python (scripts auxiliares de análise)
- Wordlists customizadas

---

## 🧪 Metodologia de Teste

- Interceptação e análise de requisições HTTP
- Testes manuais de parâmetros e inputs
- Enumeração de endpoints e funcionalidades ocultas
- Reutilização de payloads e adaptação por contexto
- Validação de comportamento do backend via Burp Repeater

---

## 🔐 Mitigações Estudadas

- Prepared Statements (SQLi prevention)
- Proper Access Control (RBAC / ABAC)
- Input validation + sanitization
- Secure file upload handling
- Output encoding
- Rate limiting e proteção contra brute force

---

## 📌 Observação

Todos os testes foram realizados exclusivamente em ambientes controlados da **PortSwigger Web Security Academy**, com finalidade educacional.

---

## 📍 Referência

PortSwigger Web Security Academy  
https://portswigger.net/web-security
