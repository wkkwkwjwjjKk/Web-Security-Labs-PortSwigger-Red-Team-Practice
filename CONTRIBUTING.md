# 📝 Guia de Contribuição

Este documento explica como adicionar documentação de um novo laboratório mantendo padrão e qualidade.

---

## 📋 Pré-requisitos

- Ter resolvido o laboratório na PortSwigger Web Security Academy
- Conhecimento técnico sobre a vulnerabilidade
- Tempo disponível: ~30-45 minutos para documentar adequadamente

---

## 🚀 Passo a Passo

### 1️⃣ Criar Diretório com Nome Padronizado

Use **kebab-case** (letras minúsculas com hífens):

```bash
# ✅ Correto
mkdir Categoria-Do-Lab/Sub-Categoria-Lab

# ❌ Evitar
mkdir "Sub Categoria Lab"  # espaços
mkdir sub_categoria_lab     # underscores
mkdir Sub_Categoria_Lab     # mix
```

**Exemplos válidos:**
- `2FA-Broken-Logic/`
- `SQL-Injection/`
- `XXE-Injection/`
- `File-Upload/`
- `Command-Injection/`

---

### 2️⃣ Copiar e Preencher o Template

```bash
# Copiar template padrão
cp docs/TEMPLATES.md Categoria-Do-Lab/README.md
```

Abra `docs/TEMPLATES.md` como referência e preencha **todas** as seções:

- ✅ **Informações Gerais** — plataforma, nível, data, ferramentas
- ✅ **Objetivo** — uma frase clara do que conquistar
- ✅ **Resumo Executivo** — 30 segundos (3-4 linhas)
- ✅ **Conceitos Teóricos** — explicar a vulnerabilidade
- ✅ **Exploração Passo a Passo** — 4 passos mínimo
- ✅ **Impacto Técnico** — tabela CIA + risco
- ✅ **Mitigação** — código vulnerável vs seguro
- ✅ **Lições Aprendidas** — insights práticos
- ✅ **Referências** — OWASP, CWE, RFC, CVE se houver

---

### 3️⃣ Validar Estrutura

Verificar manualmente:
- ✅ Todas as seções presentes
- ✅ Sem erros de markdown
- ✅ Links funcionais
- ✅ Formatação consistente

---

### 4️⃣ Fazer Commit e Push

```bash
# Stage dos arquivos
git add Categoria-Do-Lab/README.md

# Commit com mensagem descritiva
git commit -m "docs: add Categoria-Do-Lab documentation"

# Exemplo:
git commit -m "docs: add SSTI labs and write-ups"

# Push
git push origin main
```

Mensagens de commit sugeridas:
- `docs: add [categoria] labs`
- `docs: add [lab-name] write-up`
- `docs: update [categoria] documentation`
- `chore: fix typos in [categoria]`

---

## 🎯 Exemplo Prático: Adicionar Labs de SSTI

```bash
# 1. Criar diretório
mkdir Server-Side-Template-Injection
cd Server-Side-Template-Injection

# 2. Copiar template
cp ../docs/TEMPLATES.md README.md

# 3. Editar com seu conteúdo
vim README.md  # ou seu editor preferido

# 4. Commit
git add README.md
git commit -m "docs: add Server-Side-Template-Injection labs (8 labs resolved)"
git push origin main
```

---

## 📋 Checklist antes de Fazer Commit

- [ ] Nome da pasta está em **kebab-case**
- [ ] Arquivo é `README.md` (não `.MD` ou outro)
- [ ] Todas as 8 seções do template preenchidas
- [ ] Código comentado quando aplicável
- [ ] Referências técnicas incluídas (OWASP, CWE)
- [ ] Mitigação tem código de exemplo
- [ ] Impacto claro na tabela CIA
- [ ] Sem erros de digitação
- [ ] Sem espaços ou caracteres especiais no nome
- [ ] Links testados e funcionais

---

## 🧩 Estrutura de Categorias

Categorias principais:

```
01-Autenticacao/
├── 2FA-Broken-Logic/
├── Authentication-Vulnerabilities/
├── Password-Based-Login/
└── JWT-Authentication/

02-Injecao/
├── SQL-Injection/
├── Blind-SQL-Injection/
├── Command-Injection/
└── XXE-Injection/

03-Controle-Acesso/
├── Access-Control/
└── IDOR-Vulnerabilities/

04-Requisicoes-Web/
├── CSRF/
└── SSRF/

05-Upload-Arquivos/
└── File-Upload/

06-APIs-Seguranca/
├── API-Security-Exploitation/
└── OAuth-OpenID-Labs/

07-Avancado/
├── Server-Side-Template-Injection/
├── Deserialization/
└── Business-Logic-Flaws/

docs/
├── TEMPLATES.md
└── CONTRIBUTING.md

scripts/
└── [ferramentas de automação]
```

---

## ⚡ Dicas Rápidas

### Código comentado
```python
# ✅ Bom
name = request.args.get('name')  # Input do usuário
query = f"SELECT * FROM users WHERE name = '{name}'"  # ❌ Vulnerável!
```

### Formatação de payloads
```markdown
**Payload de teste:**
```http
GET /search?q=1' AND '1'='1
Host: target.com
```

**Resposta:**
```
200 OK - todos os produtos listados
```
```

### Referências técnicas
```markdown
- **OWASP**: [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- **CWE**: [CWE-89 SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
- **RFC**: [RFC 3986 URI Generic Syntax](https://datatracker.ietf.org/doc/html/rfc3986)
```

---

## 🤔 Perguntas Frequentes

**P: Posso usar espaços no nome da pasta?**
R: Não. Use hífens: `My-New-Lab` ✅ ao invés de `My New Lab` ❌

**P: Devo usar uppercase ou lowercase?**
R: Use **kebab-case** (tudo minúsculo com hífens): `server-side-template-injection` ✅

**P: E números no início?**
R: Sim, é permitido: `2FA-Broken-Logic`, `XXE-Injection` ✅

**P: Quantas seções são obrigatórias?**
R: Todas as 8 do template. Se não se aplica, coloque "N/A" com justificativa.

---

**Última atualização**: Julho 2026  
**Versão**: 1.0  
**Status**: Pronto para uso
