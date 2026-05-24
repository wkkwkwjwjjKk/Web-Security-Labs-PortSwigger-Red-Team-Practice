# Web Security Labs

Repositório dedicado a estudos práticos de segurança ofensiva e exploração de vulnerabilidades web utilizando labs da PortSwigger Web Security Academy.

---

# Objetivo

Este repositório foi criado para documentar:

- resolução de labs
- writeups técnicos
- exploração manual de vulnerabilidades
- metodologia de pentest web
- aprendizado contínuo em Application Security

O foco principal é desenvolver habilidades práticas em:
- Web Application Security
- Offensive Security
- Pentest Web
- HTTP Analysis
- Exploração manual
- Enumeração
- Bypass de filtros

---

# Vulnerabilidades Estudadas

## SQL Injection

Labs resolvidos envolvendo:

- Authentication Bypass
- UNION Attacks
- Blind SQL Injection
- Boolean-Based SQLi
- Time-Based SQLi
- Conditional Responses
- XML-based SQLi
- WAF Bypass
- Database Enumeration

### Conceitos praticados
- UNION SELECT
- comments (`--`)
- concatenação SQL
- information_schema
- XML entities
- conditional logic
- delays
- encoding bypass

---

## SSRF (Server-Side Request Forgery)

Labs envolvendo:

- Basic SSRF
- SSRF against localhost
- SSRF with blacklist bypass
- SSRF with open redirect
- SSRF filter bypass

### Conceitos praticados
- internal services
- localhost access
- URL parsing
- open redirect abuse
- SSRF chaining

---

## Access Control Vulnerabilities

Labs resolvidos:

- Unprotected Admin Functionality
- IDOR
- User Role Modification
- Password Disclosure
- Multi-Step Process Vulnerabilities
- Referer-Based Access Control
- URL-Based Access Control Bypass

### Conceitos praticados
- privilege escalation
- parameter tampering
- horizontal escalation
- vertical escalation
- insecure direct object references

---

## Command Injection

Labs envolvendo:

- Basic Command Injection
- Blind Command Injection
- Time Delays
- Output Redirection
- Out-of-Band Data Exfiltration

### Conceitos praticados
- OS command execution
- blind injection
- time-based detection
- OAST
- shell operators

---

## File Upload Vulnerabilities

Labs resolvidos:

- Web Shell Upload
- Extension Blacklist Bypass
- Content-Type Restriction Bypass
- Obfuscated File Extensions
- Path Traversal Upload

### Conceitos praticados
- file validation bypass
- MIME bypass
- upload filters
- web shells
- path traversal

---

## Authentication Vulnerabilities

Labs envolvendo:

- Username Enumeration
- Broken Brute Force Protection
- MFA Vulnerabilities
- Response Timing Attacks

### Conceitos praticados
- brute force logic
- timing analysis
- authentication flaws
- enumeration techniques

---

# Ferramentas Utilizadas

- Burp Suite
- Burp Repeater
- Burp Intruder
- Hackvertor
- Browser DevTools
- HTTP Requests
- Python (automação básica)

---

# Habilidades Desenvolvidas

- análise de requisições HTTP
- exploração manual de vulnerabilidades
- enumeração de aplicações
- bypass de filtros
- manipulação de payloads
- raciocínio ofensivo
- análise de respostas
- entendimento de lógica insegura

---

# Mitigações Estudadas

- Prepared Statements
- Parameterized Queries
- Input Validation
- Least Privilege
- Secure File Validation
- Proper Access Control
- Output Encoding

---

# Plataforma

Labs realizados na:

PortSwigger Web Security Academy  
https://portswigger.net/web-security

---

# Observação

Todos os testes e explorações realizados neste repositório foram executados exclusivamente em ambientes autorizados e laboratoriais destinados ao aprendizado de segurança ofensiva.
