
## Overview

Concluí todos os labs de SQL Injection da PortSwigger Web Security Academy com foco em:

- exploração manual
- entendimento da lógica SQL
- enumeração de banco
- bypass de autenticação
- UNION attacks
- Blind SQL Injection
- WAF bypass
- XML/JSON SQLi
- extração de dados
- análise de respostas da aplicação

## Principais conceitos praticados

### Authentication Bypass
Exploração de login vulnerável utilizando comentários SQL:

```sql
administrator'--
````

Conceitos:

* quebra de query
* comentários SQL
* manipulação de lógica da aplicação

---

### UNION Attacks

Prática de:

* descoberta de número de colunas
* identificação de colunas refletidas
* extração de dados de outras tabelas

Exemplo:

```sql
UNION SELECT username,password FROM users
```

Conceitos:

* UNION SELECT
* concatenação
* enumeração de banco

---

### Blind SQL Injection

Técnicas estudadas:

* Boolean-based
* Time-based
* Conditional responses

Exemplos:

```sql
AND 1=1
AND 1=2
```

```sql
SLEEP(5)
```

Conceitos:

* inferência lógica
* enumeração cega
* delays
* resposta condicional

---

### SQLi em XML

Exploração de SQL Injection em XML com bypass de WAF utilizando entidades XML hexadecimais.

Exemplo:

```xml
&#x53;ELECT
```

Conceitos:

* XML parsing
* encoding bypass
* canonicalization
* WAF bypass

---

## Ferramentas utilizadas

* Burp Suite
* Repeater
* Intruder
* Hackvertor
* DevTools

---

## Conhecimentos desenvolvidos

* análise de requisições HTTP
* manipulação manual de payloads
* raciocínio de exploração
* enumeração de banco de dados
* bypass de filtros
* entendimento de queries SQL vulneráveis

---

## Mitigação

As principais formas de prevenção incluem:

* Prepared Statements
* Parameterized Queries
* validação de input
* princípio de menor privilégio
* whitelist de parâmetros

---

## Plataforma

Labs realizados na:

PortSwigger Web Security Academy
[https://portswigger.net/web-security](https://portswigger.net/web-security)

