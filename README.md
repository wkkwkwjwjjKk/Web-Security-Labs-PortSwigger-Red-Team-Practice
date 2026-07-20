# 📚 Web Security Labs – PortSwigger | Red Team Practice

**Documentação completa de estudo e domínio de vulnerabilidades web ofensivas, com foco em exploração manual, análise crítica e desenvolvimento de raciocínio de ataque.**

---

## 📊 Resumo do Progresso

| Métrica | Status | Detalhe |
|---------|--------|----------|
| **Laboratórios Mapeados** | 20 | Distribuídos em 6 categorias |
| **Concluídos & Dominados** | 16 (80%) | Conceitos totalmente internalizados |
| **Em Estudo** | 0 (0%) | — |
| **Não Iniciados** | 4 (20%) | Planejado para breve |
| **Total de Horas** | ~70h | Tempo investido em estudo + prática |

---

## 🗺️ Roteiro de Estudo por Nível

### 🟢 Iniciante – Fundamentos Sólidos

**O que você aprenderá**: Conceitos fundamentais de segurança web, como requisições HTTP funcionam, e como identificar vulnerabilidades básicas.

- Autenticação e controle de acesso básico
- SQL Injection simples (UNION SELECT)
- Conceitos fundamentais de requisições HTTP
- **Tempo estimado**: ~4 horas

**Labs**: `01-Autenticacao/Password-Based-Login`, `02-Injecao/SQL-Injection` (primeiros 3)

---

### 🟡 Intermediário – Técnicas de Exploração

**O que você aprenderá**: Técnicas mais avançadas quando não há retorno direto de dados, manipulação de headers e parâmetros, e uso de ferramentas fora de banda (OAST).

- Injeções avançadas: SQLi cega, SSRF, Command Injection
- Manipulação de cabeçalhos, parâmetros, caminhos e URLs
- Técnicas OAST para detecção e extração sem retorno visível
- Exploração de 2FA e fluxos de autenticação
- **Tempo estimado**: ~15 horas

**Labs**: Toda categoria `02-Injecao`, `01-Autenticacao/2FA-Broken-Logic`, `04-Requisicoes-Web/SSRF`

---

### 🔴 Avançado – Exploração Complexa

**O que você aprenderá**: Exploração de vulnerabilidades sofisticadas, encadeamento de ataques, e como pensar como um attacker para encontrar falhas lógicas.

- XXE em todas as variantes, manipulação de XML
- CSRF, parameter pollution, mass assignment em APIs
- Análise e exploração de falhas em lógica de negócio
- Testes e segurança em APIs REST
- **Tempo estimado**: ~20 horas

**Labs**: `02-Injecao/XXE-Injection`, `06-APIs-Seguranca`, `04-Requisicoes-Web/CSRF`

---

## 📂 Organização dos Diretórios

```
01-Autenticacao/
├── 2FA-Broken-Logic/                  Bypass de 2FA via manipulação de estado
├── Authentication-Vulnerabilities/    Vulnerabilidades gerais em login
├── Password-Based-Login/              Exploração de fluxo de senha
└── JWT-Authentication/                Bypass de JWT e manipulação de token

02-Injecao/
├── SQL-Injection/                     9 labs: UNION, enumeração, bypass
├── Blind-SQL-Injection/               3 labs: boolean, time-based, OAST
├── Command-Injection/                 Execução de comandos do SO
└── XXE-Injection/                     8 labs: file read, SSRF, blind XXE

03-Controle-Acesso/
└── Access-Control/                    IDOR, privs horizontais/verticais

04-Requisicoes-Web/
├── CSRF/                              Bypass de proteções, contorno de tokens
└── SSRF/                              7 labs: localhost, redes internas, metadata

05-Upload-Arquivos/
└── File-Upload/                       [Planejado para breve]

06-APIs-Seguranca/
├── API-Security-Exploitation/         5 labs: endpoints ocultos, mass assignment
└── OAuth-OpenID-Labs/                 Bypass de OAuth, account linking

07-Avancado/
├── Server-Side-Template-Injection/    [Planejado]
├── Deserialization/                   [Planejado]
└── Business-Logic-Flaws/              [Planejado]

docs/
├── TEMPLATES.md                       Padrão para documentar novos labs
└── CONTRIBUTING.md                    Guia de como adicionar conteúdo

scripts/
└── [Ferramentas de automação Python]  Auto-refactor, geração de estrutura
```

---

## 🎯 Detalhamento por Categoria

### 🔐 01. Autenticação & Controle de Acesso

**Status**: 100% concluído e dominado ✅

**O que você vai aprender**:
- Exploração de falhas em lógica de login
- Bypass de 2FA por manipulação de estado de sessão
- Enumeração de usuários via timing/mensagens de erro
- Bypass de limites de tentativas (rate limiting)
- Vulnerabilidades em fluxos de recuperação de senha
- Exploração de OAuth e OpenID Connect
- Escalamento de privilégios (vertical)
- Falhas em Referência de Objeto Direto (IDOR)

**Labs completados**: 4/4
- ✅ 2FA Broken Logic (Apprentice)
- ✅ Authentication Vulnerabilities (Apprentice → Practitioner)
- ✅ Password-Based Login (Apprentice)
- ✅ JWT Authentication (Practitioner)

**Conceito-chave**: O estado de autenticação deve ser **SEMPRE vinculado ao servidor**, nunca confie em valores do cliente.

---

### 💉 02. Injeção de Código

#### SQL Injection

**Status**: 9/9 laborat órios concluídos – metodologia 100% dominada ✅

- Injeção simples com `UNION` para extração direta de dados
- Enumeração completa de esquemas, tabelas e colunas do banco
- SQLi cega por comparação booleana
- SQLi cega por atraso no tempo de resposta
- Bypass de filtros e proteções como WAF
- Injeção em formatos estruturados: XML e JSON

**Conceito-chave**: Nunca concatene entrada do usuário em SQL. Use **Prepared Statements SEMPRE**.

---

#### Blind SQL Injection

**Status**: 3/3 laborat órios concluídos – técnicas avançadas dominadas ✅

- Exploração boolean-based (AND 1=1 vs AND 1=2)
- Exploração baseada em erro (CASE WHEN, CAST)
- Exploração baseada em delay (SLEEP, WAITFOR)
- OAST: exfiltração via DNS e HTTP
- Extração via DTD malicioso
- Reutilização de DTD local para bypass

**Conceito-chave**: Sem retorno visível, **ainda há canais de inferência**: tempo, erros, DNS, HTTP.

---

#### Command Injection

**Status**: 100% concluído e dominado ✅

- Execução arbitrária de comandos via separadores (`;`, `|`, `&`)
- Command injection cega com delays
- Extração via requisições out-of-band

**Conceito-chave**: Use `subprocess` com arrays, **nunca** `os.system` com strings.

---

#### XML External Entity (XXE) Injection

**Status**: 8/8 laborat órios concluídos – todas as variantes exploradas ✅

- Exploração básica para leitura de arquivos
- SSRF via entidades externas
- Blind XXE com interação fora de banda
- Blind XXE com entidades de parâmetro
- Extração via DTD malicioso
- Extração via mensagens de erro
- XInclude para bypass de restrições
- Exploração via upload de SVG
- Reutilização de DTD local (técnica Expert)

**Conceito-chave**: O processamento XML apresenta **múltiplas superfícies de ataque**. Desabilite entidades externas SEMPRE.

---

### 🔄 03. Controle de Acesso

**Status**: Conteúdo disponível, novos labs em planejamento

**O que você vai aprender**:
- IDOR (Insecure Direct Object Reference)
- Escalonamento horizontal de privilégios
- Escalonamento vertical de privilégios
- Validação inadequada de autorização

**Conceito-chave**: **Verificar autorização no servidor em TODA requisição**. Nunca confiar em cliente.

---

### 🌐 04. Requisições Web & Manipulação

#### CSRF – Cross-Site Request Forgery

**Status**: 100% concluído e dominado ✅

- Bypass de tokens CSRF
- Contorno de validação de Origin/Referer
- Técnicas de escalonamento via CSRF

**Conceito-chave**: Token CSRF deve ser **único por sessão**, aleatório e validado SEMPRE.

---

#### SSRF – Server-Side Request Forgery

**Status**: 7/7 laboratórios concluídos – conceito e exploração 100% dominados ✅

**Laboratórios explorados**:
- Basic SSRF contra servidor local (`127.0.0.1`)
- SSRF contra sistemas internos (redes `192.168.x.x`, `10.0.0.x`)
- SSRF com blacklist-based filter (bypass com IPv6, octal, hex)
- SSRF com filter via open redirection
- Blind SSRF com detecção OAST (DNS/HTTP)
- SSRF com filtro de whitelist (bypass com `@`, `#`, encoding)
- Blind SSRF com Shellshock (exploração combinada)

**Conceito-chave**: Firewall interno não protege contra SSRF. Use **whitelist de domínios**, não blacklist.

---

### 🔐 05. Upload de Arquivos

**Status**: 🟡 Planejado para breve (Agosto 2026)

**O que será explorado**:
- Bypass de validação de extensão
- Race conditions em processamento
- Exploit de processadores de imagem
- RCE via upload de arquivo

---

### 🔗 06. APIs & Segurança Web

#### API Security & Web Exploitation

**Status**: 5/5 laboratórios concluídos ✅

- **Lab 1**: Usando documentação de API (`/api/docs`) para descoberta
- **Lab 2**: Encontrando endpoints ocultos sem autenticação
- **Lab 3**: Mass Assignment (inje ção de parâmetros não esperados)
- **Lab 4**: Server-Side Parameter Pollution (Query String)
- **Lab 5**: Server-Side Parameter Pollution (REST URL Path)

**Conceito-chave**: APIs compartilham vulnerabilidades web + suas próprias. **Sempre validar autorização e whitelist de campos**.

---

#### OAuth & OpenID Connect

**Status**: Fundações documentadas ✅

- Bypass de estado (state parameter)
- Account linking vulnerabilities
- Scope escalation

**Conceito-chave**: O parâmetro `state` deve ser **aleatório, único por sessão e SEMPRE validado**.

---

### 🚀 07. Avançado

**Status**: 🟡 Planejado para breve (Julho-Agosto 2026)

**Categorias a Explorar**:

1. **Server-Side Template Injection (SSTI)**
   - Exploração em Jinja2, ERB, Smarty, etc
   - RCE via template injection

2. **Deserialization Insegura**
   - PHP unserialize()
   - Java ObjectInputStream
   - Python pickle
   - RCE via gadget chains

3. **Falhas em Lógica de Negócio**
   - Bypass de validações de negócio
   - Race conditions
   - Inconsistências entre processos

---

## 🛠️ Ferramentas Utilizadas no Estudo

### Essenciais

- **Burp Suite Community Edition** — Proxy, Repeater, Intruder, Decoder
- **Browser DevTools** — Inspeção de requisições, console, storage
- **Interactsh** — OAST (Out-of-band data exfiltration)
- **Hackvertor** — Encoding/decoding dentro do Burp

### Utilitários de Terminal

```bash
curl              # Requisições HTTP manuais
wget              # Download de recursos
nslookup          # Consultas DNS
ping              # Teste de conectividade
cat / grep        # Manipulação de texto
jq                # Parsing JSON
base64            # Encoding/decoding
openssl           # Criptografia
```

### Referências Técnicas

- **OWASP**
  - [OWASP Top 10 2021](https://owasp.org/Top10/)
  - [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
  - [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

- **PortSwigger Web Security Academy**
  - [Web Security Academy](https://portswigger.net/web-security)
  - Laboratórios prát icos + materiais educacionais

- **Outras Referências**
  - [CWE Top 25](https://cwe.mitre.org/top25/)
  - [HackTricks](https://book.hacktricks.xyz/)
  - [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)

---

## 📈 Progressão de Dificuldade

```
Apprentice (Iniciante)
↓
  Conceitos básicos, exploração direta
  Laboratórios: ~5-10 minutos cada
  Habilidade necessária: Nenhuma pré-requisito

↓

Practitioner (Intermediário)
↓
  Técnicas mais sofisticadas, sem retorno visível
  Laboratórios: ~15-30 minutos cada
  Habilidade necessária: Entender HTTP, SQL básico

↓

Expert (Avançado)
↓
  Exploração complexa, encadeamento de ataques
  Laboratórios: ~30-60 minutos cada
  Habilidade necessária: Profundidade técnica, mentalidade de attacker
```

---

## 🎓 Como Usar Este Repositório

### Para Iniciantes

1. **Comece aqui**: `01-Autenticacao/Password-Based-Login/`
2. **Depois**: `02-Injecao/SQL-Injection/` (primeiros 3 labs)
3. **Leia**: `docs/TEMPLATES.md` para entender a estrutura
4. **Entenda**: Cada lab explica o conceito + causa raiz + defesa

### Para Intermediários

1. **Pule para**: Categoria `02-Injecao` completa
2. **Estude**: `04-Requisicoes-Web/SSRF/` (técnicas avan çadas)
3. **Pratique**: Blind SQLi e OAST (conceitos desafiadores)
4. **Referência**: Use `CONTRIBUTING.md` se quiser adicionar novos labs

### Para Avançados

1. **Explore**: `02-Injecao/XXE-Injection/` para técnicas sofisticadas
2. **Estude**: `06-APIs-Seguranca/` para vulnerabilidades modernas
3. **Encadeie**: Combine múltiplas vulnerabilidades
4. **Contribua**: Adicione novos labs quando completar categoria `07-Avancado`

---

## 📝 Estrutura de Cada Laboratório

Cada diretório contém um `README.md` padronizado com:

```markdown
## 📋 Informações Gerais
  - Plataforma, nível, status, data

## 🎯 Objetivo
  - Uma frase clara do que conquistar

## 📚 Conceitos Teóricos
  - O que é a vulnerabilidade
  - Por que acontece
  - Qual é o impacto

## 🧪 Exploração Passo a Passo
  - 4+ passos detalhados
  - Payloads comentados
  - Resultado esperado

## 💥 Impacto Técnico
  - Tabela CIA (Confidencialidade, Integridade, Disponibilidade)
  - Risco por aspecto

## 🛡️ Mitigação & Defesa
  - Código vulnerável vs seguro
  - Princípios de defesa (checklist)

## 🎓 Lições Aprendidas
  - Insights práticos
  - Aplicação em bug bounty

## 🔗 Referências
  - OWASP, CWE, RFC, PortSwigger
```

---

## ✨ Destaques & Insights

### Mentalidade de Attacker

Cada vulnerabilidade ensina uma mentalidade:

1. **SQL Injection**: "Dados ≠ Código" — separar entrada de lógica SQL
2. **XXE**: "Múltiplas superfícies de ataque" — XML tem várias variantes
3. **SSRF**: "Firewall interno não protege" — servidor tem acesso
4. **2FA Broken**: "Estado ≠ Client" — autenticação crítica no servidor
5. **APIs**: "Whitelist sempre" — negação por padrão

### Progressão de Pensamento

```
Fase 1: "Como explorar?"
  ↓ Aprender técnicas, ferramentas

Fase 2: "Por que funciona?"
  ↓ Entender causa raiz, lógica

Fase 3: "Como contornar proteções?"
  ↓ Bypass de filtros, WAF, validações

Fase 4: "Como se defender?"
  ↓ Implementar controles, mitigações

Fase 5: "Como isso se conecta?"
  ↓ Encadear vulnerabilidades, pensar em ofensiva
```

---

## 🤝 Contribuindo Novos Labs

Para adicionar um novo laboratório:

1. **Leia** `CONTRIBUTING.md`
2. **Crie** novo diretório em categoria apropriada
3. **Copie** `docs/TEMPLATES.md` como `README.md`
4. **Preencha** TODAS as seções
5. **Valide** estrutura e links
6. **Commit** com mensagem descritiva

Exemplo:
```bash
mkdir 07-Avancado/Server-Side-Template-Injection
cp docs/TEMPLATES.md 07-Avancado/Server-Side-Template-Injection/README.md
# Editar e preencher
git add 07-Avancado/
git commit -m "docs: add SSTI labs and write-ups"
git push origin main
```

---

## 📊 Estatísticas & Métricas

### Por Nível de Dificuldade

| Nível | Total | Concluído | % |
|-------|-------|-----------|----|
| Apprentice | 8 | 8 | 100% |
| Practitioner | 10 | 8 | 80% |
| Expert | 2 | 0 | 0% |
| **TOTAL** | **20** | **16** | **80%** |

### Por Categoria

| Categoria | Labs | Status | Conceitos |
|-----------|------|--------|----------|
| 01-Autenticacao | 4 | ✅ 4/4 | 8 técnicas |
| 02-Injecao | 9 | ✅ 9/9 | 12+ vetores |
| 03-Controle-Acesso | 0 | 🟡 Planejado | — |
| 04-Requisicoes-Web | 2 | ✅ 2/2 | 10+ técnicas |
| 05-Upload-Arquivos | 0 | 🟡 Planejado | — |
| 06-APIs-Seguranca | 2 | ✅ 2/2 | 8 vulnerabilidades |
| 07-Avancado | 3 | 🟡 Planejado | — |

---

## 🎯 Próximos Passos

### Curto Prazo (Julho-Agosto 2026)

- [ ] Completar categoria `07-Avancado` (SSTI, Deserialization, Business Logic)
- [ ] Adicionar labs de `05-Upload-Arquivos`
- [ ] Criar guia prático de bug bounty

### Médio Prazo (Setembro 2026)

- [ ] Converter para website estático (Astro/Hugo)
- [ ] Adicionar vídeos explicativos
- [ ] Criar cheat sheets por categoria

### Longo Prazo

- [ ] Publicar como blog de segurança
- [ ] Criar workshoppe com exercícios práticos
- [ ] Manter atualizado com novas vulnerabilidades

---

## 📞 Suporte & Dúvidas

### Estrutura deste Repositório

- **`docs/TEMPLATES.md`** — Padrão para novos labs
- **`CONTRIBUTING.md`** — Como adicionar conteúdo
- **`README.md`** — Este arquivo

### Referências Externas

- **PortSwigger**: https://portswigger.net/web-security
- **OWASP**: https://owasp.org/
- **CWE**: https://cwe.mitre.org/

---

## ⚖️ Licença & Disclaimer

**Aviso Legal**: Este repositório é para fins **educacionais APENAS**. 

Todo o conteúdo:
- ✅ Pode ser usado para aprendizado pessoal
- ✅ Pode ser usado em ambientes de teste autorizados (CTFs, bug bounty, pentests com permissão)
- ❌ **NÃO** deve ser usado em sistemas sem autorização explícita
- ❌ **NÃO** constitui recomendação para atividades ilegais

Responsabilidade do usuário: Usar conhecimento ethicamente e legalmente.

---

**Autor**: Aislan Silva  
**Data de Início**: Maio 2026  
**Última Atualização**: Julho 2026  
**Status**: 📈 Em Evolução  
**Próxima Meta**: 100% (20/20 labs concluídos + 07-Avancado)

🔒 **Segurança é responsabilidade compartilhada. Aprenda, pratique, defenda.**
