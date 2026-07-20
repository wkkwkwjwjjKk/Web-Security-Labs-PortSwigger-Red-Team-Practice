# 🔓 Access Control – PortSwigger Web Security Academy

## 📋 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Controle de Acesso |
| **Nível de Dificuldade** | Apprentice a Practitioner |
| **Status** | ✅ Concluído |
| **Data** | Junho 2026 |
| **Ferramentas** | Burp Suite, Browser |

---

## 🎯 Objetivo do Laboratório

Explorar falhas em controle de acesso (authorization), incluindo acesso a recursos não autorizados, escalonamento horizontal (lateral) e vertical de privilégios.

---

## 📖 Resumo Executivo

Controle de acesso determina quem pode acessar o quê. Falhas permitem usuários não autorizados acessarem recursos sensíveis ou executarem ações administrativas.

---

## 📚 Conceitos Teóricos

### Tipos de Controle de Acesso

1. **Vertical** — Privilégios diferentes por função (admin > user > guest)
2. **Horizontal** — Acesso entre dados do mesmo nível (seu perfil vs perfil alheio)
3. **Context-based** — Baseado em tempo, localização, contexto

### Falhas Comuns

- Validação inadequada de autorização
- Dependência de parâmetros do cliente
- URLs guessáveis (1, 2, 3...)
- Sem verificação de propriedade de recurso
- Erro que revela estrutura

---

## 🛡️ Mitigação & Defesa

### ✅ Implementação Segura

```python
# ✅ Verificar autorização no servidor
@app.route('/profile/<user_id>')
def get_profile(user_id):
    # ❌ ERRADO
    # return User.query.get(user_id)
    
    # ✅ CORRETO - Verificar se é o usuário ou admin
    current_user = get_current_user()
    user = User.query.get(user_id)
    
    if user_id != current_user.id and not current_user.is_admin:
        return "Acesso negado", 403
    
    return user
```

### Princípios

- [x] Validar autorização **no servidor** sempre
- [x] Nunca confiar em parâmetros do cliente
- [x] Verificar propriedade de recurso
- [x] Usar IDs opacos (UUID) em vez de sequenciais
- [x] Falhar seguro (deny por padrão)
- [x] Logging de tentativas de acesso negado

---

## 📖 Referências

- **OWASP**: [Access Control](https://owasp.org/www-community/Access_Control)
- **CWE**: [CWE-639 - Authorization Bypass Through User-Controlled Key](https://cwe.mitre.org/data/definitions/639.html)
- **PortSwigger**: [Access Control](https://portswigger.net/web-security/access-control)

---

**Autor**: Aislan Silva  
**Status**: ✅ Documentado
