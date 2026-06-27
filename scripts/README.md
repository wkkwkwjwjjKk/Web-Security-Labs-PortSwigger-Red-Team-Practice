# 🤖 Scripts de Automação

Scripts Python que automatizam a gestão e documentação do repositório.

---

## 🚀 Como Usar

### Opção 1: Setup Completo (Recomendado)

Execute tudo de uma vez:

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### Opção 2: Executar Scripts Individuais

#### 1. Auto-Refactor (Renomear Pastas)

```bash
python3 scripts/auto-refactor.py
```

**O que faz:**
- Remove espaços em nomes de pastas
- Deleta arquivos desnecessários
- Padroniza nomenclatura
- Faz commit e push

---

#### 2. Create Structure (Criar Diretórios)

```bash
python3 scripts/create-structure.py
```

**O que faz:**
- Cria nova estrutura de diretórios
- Organiza por categorias (1-Authentication, 2-Injection, etc)
- Cria arquivos .gitkeep

---

#### 3. Generate Files (Criar READMEs)

```bash
python3 scripts/generate-files.py
```

**O que faz:**
- Cria README.md padronizado para cada categoria
- Usa template profissional
- Pré-preenchido com estrutura básica

---

#### 4. Standardize Docs (Padronizar Documentação)

```bash
python3 scripts/standardize-docs.py
```

**O que faz:**
- Aplica template padrão aos READMEs existentes
- Adiciona seções faltantes
- Padroniza referências

---

## 📋 O Que Cada Script Faz

### ✅ auto-refactor.py

**Entrada**: Repo com nomes inconsistentes  
**Saída**: Repo com nomenclatura padronizada

**Mudanças**:
```
CSRF  →  CSRF
JWT Authentication   →  JWT-Authentication
2FA Broken Logic  →  2FA-Broken-Logic
SQL_Injection  →  SQL-Injection
```

**Arquivos deletados**:
- `SQL-Injection/Screenshot 2026-05-24...` (2.1 MB)

---

### ✅ create-structure.py

**Entrada**: Repo flat  
**Saída**: Repo organizado por categorias

**Estrutura criada**:
```
1-Authentication/
  ├── Password-Based-Login/
  ├─��� Authentication-Vulnerabilities/
  └── 2FA-Broken-Logic/

2-Injection/
  ├── SQL-Injection/
  ├── Blind-SQL-Injection/
  ├── Command-Injection/
  └── XXE-Injection/

3-Access-Control/
4-Web-Requests/
5-API-Security/
6-Advanced/
7-File-Upload/
```

---

### ✅ generate-files.py

**Entrada**: Lista de labs a documentar  
**Saída**: READMEs padronizados

**Labs criados**:
- Command Injection
- File Upload
- Access Control / IDOR
- XXE Injection
- SSTI
- Deserialization
- Business Logic
- HTTP Request Smuggling

---

### ✅ standardize-docs.py

**Entrada**: READMEs inconsistentes  
**Saída**: READMEs padronizados

**Mudanças automáticas**:
- Adiciona seção de Referências se não existir
- Adiciona tabela de Impacto se não existir
- Formata headers de forma consistente

---

## 🔧 Requisitos

- Python 3.7+
- Git configurado
- Estar na raiz do repositório

---

## 📊 Status de Progresso

```
✅ Auto-Refactor     → Pronto
✅ Create Structure  → Pronto
✅ Generate Files    → Pronto
✅ Standardize Docs  → Pronto
✅ Setup Script      → Pronto
```

---

## 🐛 Troubleshooting

### Erro: "git: command not found"

Instale Git: `apt-get install git`

### Erro: "Python 3 not found"

Instale Python 3: `apt-get install python3`

### Erro: "Permission denied"

Dê permissão de execução:
```bash
chmod +x scripts/*.sh
chmod +x scripts/*.py
```

### Erro: "Already exists"

Já foi executado. Use `git reset` para reverter se necessário:
```bash
git reset --hard HEAD~1
```

---

## 🤝 Personalização

### Adicionar Novo Script

1. Crie `scripts/seu-script.py`
2. Use estrutura similar aos scripts existentes
3. Adicione à lista do `setup.sh`

### Modificar Template

Edite `docs/TEMPLATES.md` para mudar o padrão de documentação.

---

## 📝 Exemplos de Uso

### Cenário 1: Novo Repositório

```bash
# Clonar e entrar
git clone [seu-repo]
cd [seu-repo]

# Executar setup completo
chmod +x scripts/setup.sh
./scripts/setup.sh

# Revisar mudanças
git status

# Commit
git add -A
git commit -m "refactor: complete repository standardization"
git push origin main
```

### Cenário 2: Atualizar Documentação Existente

```bash
# Apenas padronizar documentação
python3 scripts/standardize-docs.py

# Commit
git add -A
git commit -m "docs: standardize documentation format"
git push origin main
```

### Cenário 3: Adicionar Novas Categorias

```bash
# Criar estrutura
python3 scripts/create-structure.py

# Gerar READMEs
python3 scripts/generate-files.py

# Commit
git add -A
git commit -m "feat: add new lab categories"
git push origin main
```

---

## 🚀 Próximas Melhorias

- [ ] Script para converter screenshots para WebP (reduz tamanho)
- [ ] Script para gerar tabela de progresso automática
- [ ] Script para validar links nos READMEs
- [ ] Script para enviar notificação ao completar um lab

---

## 📞 Suporte

Dúvidas sobre os scripts? Verifique:
1. Código comentado dos scripts
2. Exemplos de uso acima
3. Arquivo CONTRIBUTING.md

---

**Última atualização**: Junho 2026  
**Versão**: 1.0
