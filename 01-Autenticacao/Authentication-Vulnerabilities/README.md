# 🔐 Authentication Vulnerabilities – PortSwigger Web Security Academy

## 📌 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Autenticação & Controle de Acesso |
| **Nível de Dificuldade** | Apprentice a Practitioner |
| **Status** | ✅ 100% Concluído |
| **Data** | Maio-Junho 2026 |
| **Ferramentas** | Burp Suite, Browser DevTools |

---

## 🎯 Objetivo do Laboratório

Dominar técnicas de exploração de vulnerabilidades em mecanismos de autenticação, incluindo bypass de login, enumeração de usuários, contorno de proteções de força bruta e falhas em fluxos de recuperação de conta.

---

## 📖 Resumo Executivo

Esta categoria abrange 4 classes principais de vulnerabilidades em autenticação:
1. **Bypass de credenciais** — exploração de lógica de verificação falha
2. **Enumeração de usuários** — descoberta de nomes de usuário válidos
3. **Bypass de proteções** — contorno de rate limiting e bloqueio de conta
4. **Falhas em fluxo de recuperação** — redefinição de senha insegura

Todos os conceitos foram explorados manualmente, validados e documentados.

---

## 📚 Conceitos Teóricos

### O que são Vulnerabilidades de Autenticação?

Autenticação é o processo de verificar que um usuário é realmente quem diz ser. Vulnerabilidades surgem quando:

- Credenciais são verificadas de forma insegura
- Proteções contra força bruta são inadequadas
- Identidades de usuário são fáceis de descobrir
- Fluxos de recuperação não validam propriedade da conta
- Estado de autenticação não é mantido corretamente

### Por que acontecem?

- Implementação superficial de mecanismos de segurança
- Falta de compreensão de ataques comuns
- Priorização de usabilidade sobre segurança
- Testes de segurança inadequados antes do deploy
- Reutilização de código legado vulnerável

### Qual é o impacto?

- **Crítico**: Acesso não autorizado a contas de usuários
- Comprometimento de dados sensíveis
- Roubo de identidade
- Escalonamento de privilégios
- Conformidade regulatória (GDPR, PCI DSS, HIPAA)

---

## 🧪 Técnicas Exploradas

### 1. Username Enumeration (Enumeração de Usuários)

**Técnica**: Diferenças de resposta revelam se um usuário existe.

```http
POST /login HTTP/1.1
Host: target.com
Content-Type: application/x-www-form-urlencoded

username=invalid&password=test
```

**Resposta (usuário não existe)**:
```
Response time: 80ms
Status: 401
Mensagem: "Usuário ou senha inválidos"
```

```http
POST /login HTTP/1.1
Host: target.com
Content-Type: application/x-www-form-urlencoded

username=administrator&password=test
```

**Resposta (usuário existe)**:
```
Response time: 250ms  ← Mais lento!
Status: 401
Mensagem: "Usuário ou senha inválidos"
```

**Por que funciona**: A aplicação tenta verificar a senha mesmo se o usuário não existir, vazando informações de tempo.

---

### 2. Flawed Logic (Lógica Defeituosa)

**Técnica**: Bypass de verificação por falha na lógica condicional.

```java
// ERRADO
if (username == request.getParameter("username")) {
    if (password == request.getParameter("password")) {
        // Espaço entre as verificações permite bypass!
        logged_in = true;
    }
}
```

**Payload**:
```
username=administrator&password=wrongpassword
```

Se a lógica usar `==` em vez de `.equals()` ou não validar corretamente, pode ser contornada.

---

### 3. Brute Force com Rate Limiting Defeituoso

**Técnica**: Contorno de proteção por IP, usando header `X-Forwarded-For`.

```http
POST /login HTTP/1.1
Host: target.com
X-Forwarded-For: 192.168.1.1          ← Spoofar IP
Content-Type: application/x-www-form-urlencoded

username=carlos&password=password123
```

**Por que funciona**: Servidor confia em header `X-Forwarded-For` para rate limiting, permitindo múltiplas tentativas com IPs diferentes.

**Defesa**: Rate limiting deve ser por usuário, não por IP.

---

### 4. Account Lockout Bypass

**Técnica**: Após N tentativas erradas, explorar reset de contador.

```
Tentativa 1-4: Senha errada (contador aumenta)
Tentativa 5: Uma senha correta e várias erradas
Tentativa final: Se contador não foi resetado, brute force continua
```

**Por que funciona**: Se uma tentativa correta não reseta o contador de tentativas erradas antes dele.

---

### 5. Password Reset Flaws

**Técnica**: Token de reset previsível ou não validado corretamente.

```http
GET /reset-password?token=12345 HTTP/1.1
```

**Problemas comuns**:
- Token numérico simples (fácil de adivinhar)
- Token não vinculado ao usuário
- Token não expira
- Qualquer usuário pode resetar qualquer conta

**Exploit**: Tentar tokens sequenciais ou modificar parâmetro de usuário.

---

## 💥 Impacto Técnico

| Aspecto | Risco | Justificativa |
|---------|-------|---------------|
| **Confidencialidade** | 🔴 Alto | Acesso total aos dados do usuário |
| **Integridade** | 🔴 Alto | Modificação de perfil, dados pessoais |
| **Disponibilidade** | 🟡 Médio | Bloqueio de conta legítima |
| **Privilégios Necessários** | Verde | Nenhum (ataque anônimo) |
| **Tipo de Ataque** | Ativo | Requer envio de múltiplas requisições |

---

## 🛡️ Mitigação & Defesa

### ✅ Boas Práticas

```python
# CORRETO - Autenticação segura
from werkzeug.security import check_password_hash
import secrets
import time
from datetime import datetime, timedelta

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # 🟢 NÃO revelar se usuário existe
    generic_error = "Username or password is incorrect"
    
    user = User.query.filter_by(username=username).first()
    
    if not user:
        # 🟢 Sempre usar password hashing para evitar timing attack
        check_password_hash(secrets.token_hex(32), password)
        return generic_error, 401
    
    # 🟢 Verificar lockout
    if user.locked_until and user.locked_until > datetime.utcnow():
        return "Conta bloqueada. Tente novamente em 15 minutos", 403
    
    # 🟢 Verificar senha com hash seguro (bcrypt, argon2)
    if not check_password_hash(user.password_hash, password):
        # 🟢 Incrementar contador de tentativas
        user.failed_attempts += 1
        if user.failed_attempts >= 5:
            user.locked_until = datetime.utcnow() + timedelta(minutes=15)
        db.session.commit()
        return generic_error, 401
    
    # 🟢 Sucesso - resetar contador
    user.failed_attempts = 0
    user.locked_until = None
    user.last_login = datetime.utcnow()
    db.session.commit()
    
    # 🟢 Criar sessão segura
    session['user_id'] = user.id
    session.permanent = True
    return "Login successful"

@app.route('/reset-password', methods=['POST'])
def request_password_reset():
    email = request.form.get('email')
    
    # 🟢 NÃO revelar se email existe
    user = User.query.filter_by(email=email).first()
    
    if user:
        # 🟢 Gerar token criptograficamente seguro
        reset_token = secrets.token_urlsafe(32)
        
        # 🟢 Vincular ao usuário e expirar em 1 hora
        user.reset_token = reset_token
        user.reset_token_expires = datetime.utcnow() + timedelta(hours=1)
        db.session.commit()
        
        # 🟢 Enviar link seguro
        send_reset_email(email, reset_token)
    
    # 🟢 Sempre retornar mensagem genérica
    return "Se o email existir, link de reset foi enviado"

@app.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    # 🟢 Validar token
    user = User.query.filter_by(reset_token=token).first()
    
    if not user or user.reset_token_expires < datetime.utcnow():
        return "Token inválido ou expirado", 403
    
    new_password = request.form.get('password')
    
    # 🟢 Hash seguro da nova senha
    user.password_hash = generate_password_hash(new_password, method='pbkdf2')
    user.reset_token = None
    user.reset_token_expires = None
    db.session.commit()
    
    return "Senha resetada com sucesso"
```

### Princípios de Defesa

- [x] Mensagens de erro genéricas (não revelar se usuário existe)
- [x] Hash seguro com salt (bcrypt, argon2, PBKDF2)
- [x] Rate limiting por usuário + IP
- [x] Lockout de conta temporário (15+ minutos)
- [x] Tokens aleatórios e criptograficamente seguros
- [x] Expiração de tokens (1 hora máximo)
- [x] Validação de origem (CSRF tokens)
- [x] Logging e alertas de atividade suspeita
- [x] Autenticação multifator (2FA, TOTP)
- [x] Validação de força de senha

---

## 🎓 Lições Aprendidas

### Insight 1: Detalhes Matam
Mensagens de erro genéricas, tempos de resposta consistentes e comportamento uniforme são fundamentais.

### Insight 2: Defense in Depth
Uma única camada de defesa nunca é suficiente. Combine múltiplas técnicas.

### Insight 3: Timing Matters
Se uma operação legítima leva 100ms, a ilegítima também deve levar ~100ms. Use constant-time comparisons.

### Insight 4: Usuários São Únicos
Rate limiting por IP é inútil em proxy corporativo. Sempre use por usuário + IP.

---

## 🔗 Referências Completas

- **OWASP**: [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- **OWASP**: [Testing for Authentication](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/README.html)
- **CWE**: [CWE-287 - Improper Authentication](https://cwe.mitre.org/data/definitions/287.html)
- **CWE**: [CWE-640 - Weak Password Recovery Mechanism for Forgotten Password](https://cwe.mitre.org/data/definitions/640.html)
- **PortSwigger**: [Authentication](https://portswigger.net/web-security/authentication)
- **NIST**: [SP 800-63B - Authentication and Lifecycle Management](https://pages.nist.gov/800-63-3/sp800-63b.html)

---

**Autor**: Aislan Silva  
**Data de Conclusão**: Junho 2026  
**Status**: ✅ Documentado  
**Qualidade**: ⭐⭐⭐⭐⭐
