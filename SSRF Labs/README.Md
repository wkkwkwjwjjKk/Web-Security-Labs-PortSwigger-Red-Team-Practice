
# SSRF Labs - PortSwigger Web Security Academy

O objetivo é documentar técnicas de exploração, raciocínio e evolução prática em cenários de SSRF.

---

## 📊 Status Geral

| Lab | Dificuldade | Status |
|-----|------------|--------|
| Basic SSRF against the local server | Apprentice | ✅ Solved |
| Basic SSRF against another back-end system | Apprentice | ✅ Solved |
| Blind SSRF with out-of-band detection | Practitioner | ❌ Not solved |
| SSRF with blacklist-based input filter | Practitioner | ✅ Solved |
| SSRF with filter bypass via open redirection vulnerability | Practitioner | ✅ Solved |
| Blind SSRF with Shellshock exploitation | Expert | ❌ Not solved |
| SSRF with whitelist-based input filter | Expert | ❌ Not solved |

---

## 🧠 Overview Técnico

Durante os laboratórios de SSRF, foram explorados diferentes vetores de ataque contra requisições server-side, incluindo:

- Acesso a recursos internos (localhost e sistemas back-end)
- Manipulação de URLs internas via input do usuário
- Bypass de filtros baseados em blacklist e whitelist
- Encadeamento de vulnerabilidades (SSRF + Open Redirect)
- Tentativas de exploração cega (Blind SSRF via OAST)

---

## 🟢 Labs Resolvidos

### 1. Basic SSRF against the local server (Apprentice)

Foi possível explorar o parâmetro vulnerável de URL para acessar serviços internos no próprio servidor (`localhost`), permitindo requisições a endpoints restritos.

---

### 2. Basic SSRF against another back-end system (Apprentice)

O SSRF foi utilizado para interagir com um sistema interno não acessível diretamente pelo usuário, demonstrando comunicação entre serviços internos.

---

### 3. SSRF with blacklist-based input filter (Practitioner)

Foi identificado filtro baseado em blacklist bloqueando hosts comuns.

O bypass foi realizado através de variações de encoding e manipulação de URL, permitindo acessar recursos internos mesmo com restrição.

---

### 4. SSRF with filter bypass via open redirection (Practitioner)

O ataque foi possível combinando SSRF com Open Redirect.

O fluxo permitiu redirecionar a requisição para um endpoint interno, burlando o filtro direto de URL.

---

## 🔴 Labs Não Resolvidos (Em progresso)

### Blind SSRF with out-of-band detection (Practitioner)

O laboratório envolve exploração cega com detecção via canais OAST.

Ainda em análise de vetores de callback e validação de exfiltração.

---

### Blind SSRF with Shellshock exploitation (Expert)

Exploração envolve execução remota via headers manipulados (Shellshock).

Ainda em estudo sobre payloads e vetores de execução em ambientes CGI.

---

### SSRF with whitelist-based input filter (Expert)

Filtro baseado em whitelist dificulta manipulação direta de URL.

Em investigação de bypass via parsing, encoding e inconsistências de validação.

---

## 🛠️ Técnicas Estudadas

- URL manipulation (scheme / host / path abuse)
- Bypass de blacklist filters
- Open Redirect chaining
- Internal network probing via SSRF
- OAST-based blind detection (teórico em progresso)
- HTTP request smuggling concepts (parcialmente relacionado)

---

## 🧠 Aprendizados

- SSRF não depende só de input direto, mas de como o backend interpreta URLs
- Filtros de segurança podem ser contornados via encoding e chaining de vulnerabilidades
- Blind SSRF exige validação indireta (OAST / callbacks)
- Combinação de falhas aumenta impacto significativamente

---

## 📌 Observação

Todos os testes foram realizados exclusivamente em ambiente controlado da PortSwigger Web Security Academy para fins educacionais.

Este repositório representa progresso contínuo, incluindo laboratórios concluídos e em andamento.
