# 🔐 OAuth & OpenID Connect | PortSwigger Web Security Academy

## 📋 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | APIs & Segurança Web |
| **Nível de Dificuldade** | Practitioner |
| **Status** | ✅ Concluído |
| **Data** | Junho 2026 |
| **Ferramentas** | Burp Suite, Browser |

---

## 🎯 Objetivo do Laboratório

Explorar vulnerabilidades em implementações de OAuth 2.0 e OpenID Connect, incluindo fixação de estado, bypass de validação e account linking.

---

## 📖 Resumo Executivo

OAuth é protocolo de autorização amplamente usado para "Login com Google/Facebook". Implementações fracas permitem:
1. **Account linking** — vincular conta atacante com conta vítima
2. **State bypass** — ignorar validação CSRF
3. **Scope escalation** — solicitar permissões extras

---

## 📚 Conceitos Teóricos

### Fluxo OAuth Seguro

```
1. Usuário clica "Login com Google"
2. App gera estado aleatório + armazena na sessão
3. Redireciona para Google com state=RANDOM
4. Google autentica usuário, redireciona com code + state
5. App valida que state === session.state
6. Troca code por token com Google
7. Cria sessão para usuário
```

### Vulnerabilidades Comuns

- State não validado
- State reutilizado
- Não vincular account ao usuário
- Aceitar qualquer valor de state

---

## 🛡️ Mitigação & Defesa

### ✅ Implementação Segura

```python
import secrets

@app.route('/login/oauth')
def oauth_login():
    # ✅ Gerar state aleatório
    state = secrets.token_urlsafe(32)
    session['oauth_state'] = state
    
    return redirect(f"https://oauth-provider.com/authorize?state={state}&...")

@app.route('/oauth/callback')
def oauth_callback():
    returned_state = request.args.get('state')
    
    # ✅ Validar state
    if returned_state != session.get('oauth_state'):
        return "State inválido", 403
    
    # ✅ Limpar state usado
    del session['oauth_state']
    
    # ✅ Apenas então processar callback
    code = request.args.get('code')
    return complete_oauth_login(code)
```

---

## 📖 Referências

- **RFC**: [RFC 6749 - OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
- **OWASP**: [OAuth 2.0 Security](https://cheatsheetseries.owasp.org/cheatsheets/OAuth_2_Cheat_Sheet.html)
- **PortSwigger**: [OAuth 2.0](https://portswigger.net/web-security/oauth)

---

**Autor**: Aislan Silva  
**Status**: ✅ Documentado
