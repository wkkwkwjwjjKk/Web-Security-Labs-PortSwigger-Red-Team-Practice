# 🔄 CSRF – Cross-Site Request Forgery | PortSwigger Web Security Academy

## 📋 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Requisições Web & Manipulação |
| **Nível de Dificuldade** | Apprentice a Practitioner |
| **Status** | ✅ Concluído |
| **Data** | Junho 2026 |
| **Ferramentas** | Burp Suite, Browser DevTools |

---

## 🎯 Objetivo do Laboratório

Compreender e explorar Cross-Site Request Forgery (CSRF), incluindo bypass de tokens CSRF, contorno de validação de origin/referer e técnicas de escalação de privilégios via CSRF.

---

## 📖 Resumo Executivo

CSRF permite forçar um usuário autenticado a executar ações não intencionais em uma aplicação. O atacante cria uma página maliciosa que, quando visitada, submete requisições em nome da vítima sem seu consentimento.

---

## 📚 Conceitos Teóricos

### O que é CSRF?

Ocorre quando:
1. Vítima está autenticada em aplicação (ex: banco.com)
2. Vítima visita site malicioso (ex: ataque.com)
3. Site malicioso envia requisição para banco.com em nome da vítima
4. Navegador **automaticamente inclui cookies** da vítima
5. Ação é executada sem consentimento

### Por que é perigoso?

- Vítima não percebe que ação ocorreu
- Cookies são enviados automaticamente
- Ação é legítima sob perspectiva do servidor
- Difícil de detectar se token CSRF estiver fraco

### Como acontece?

```html
<!-- Site malicioso -->
<img src="https://banco.com/api/transfer?to=atacante&amount=1000">
<!-- Navegador da vítima envia requisição automaticamente -->
```

---

## 🛡️ Mitigação & Defesa

### ✅ Implementação Segura

```python
# CSRF Token Seguro
from secrets import token_urlsafe

def generate_csrf_token():
    # Gerar token aleatório de 32 bytes
    return token_urlsafe(32)

# Validar antes de ação sensível
@app.route('/transfer', methods=['POST'])
def transfer():
    # ✅ Validar CSRF token
    token = request.form.get('csrf_token')
    if token != session.get('csrf_token'):
        return "CSRF token inválido", 403
    
    # ✅ Validar origin/referer
    origin = request.headers.get('Origin')
    if origin != 'https://banco.com':
        return "Origin inválido", 403
    
    # ✅ Apenas POST/PUT/DELETE, não GET
    # ✅ SameSite cookie
    return transfer_money()
```

### Princípios de Defesa

- [x] CSRF token único por sessão
- [x] Token aleatório e impredizível
- [x] Validar token em TODA ação sensível
- [x] Verificar Origin/Referer headers
- [x] SameSite=Strict em cookies
- [x] Sem GET para ações (apenas POST/PUT/DELETE)
- [x] Logout automático após inatividade

---

## 📖 Referências

- **OWASP**: [Cross-Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf)
- **CWE**: [CWE-352 - Cross-Site Request Forgery (CSRF)](https://cwe.mitre.org/data/definitions/352.html)
- **PortSwigger**: [CSRF](https://portswigger.net/web-security/csrf)

---

**Autor**: Aislan Silva  
**Status**: ✅ Documentado
