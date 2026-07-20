---

# 🔒 Web Security Labs – PortSwigger Red Team Practice
**Documentação completa de laboratórios práticos de segurança ofensiva web, com foco em exploração manual, análise de vulnerabilidades e desenvolvimento de raciocínio de ataque.**

| Detalhe | Informação |
|---|---|
| Nível | Intermediário → Avançado |
| Plataforma | PortSwigger Web Security Academy |
| Idioma | Português (PT‑BR) |
| Total de laboratórios | 20 |
| Conceitos 100% dominados | 16 |
| Progresso geral | **80%** |

---

## 📊 Status Geral do Repositório
| Status | Quantidade | Percentual |
|---|---|---|
| ✅ Concluído / Conceito Dominado | 16 | 80% |
| 🟡 Em Estudo | 0 | 0% |
| 🔴 Não Iniciado | 4 | 20% |

---

## 🚀 Roteiro de Estudo por Nível
### 🟢 Iniciante
- Autenticação e controle de acesso
- SQL Injection básica
- Conceitos fundamentais de requisições HTTP
- **Tempo estimado**: ~4 horas

### 🟠 Intermediário
- Injeções avançadas: SQLi cega, SSRF, Command Injection
- Manipulação de cabeçalhos, parâmetros e URLs
- Técnicas OAST para detecção e extração sem retorno visível
- **Tempo estimado**: ~15 horas

### 🔴 Avançado
- XXE, SSTI e Desserialização Insegura
- Análise e exploração de falhas em lógica de negócio
- Testes e segurança em APIs
- **Tempo estimado**: ~20 horas

---

## 🎓 Categorias e Laboratórios

### 🟢 Autenticação e Controle de Acesso
**✅ Status: 100% concluído**
- Enumeração de usuários e contas
- Bypass de limites de tentativas e bloqueios
- Contornos em fluxos de autenticação de dois fatores (2FA)
- Vulnerabilidades em OAuth e OpenID Connect
- Escalonamento de privilégios e falhas de referência de objeto direto (IDOR)

---

### 🟡 Injeção de Código e Comandos
#### 📌 SQL Injection
**✅ Status: 9/9 laboratórios concluídos**
- Injeção simples com uso de `UNION` para extração de dados
- Enumeração de esquemas, tabelas e colunas do banco
- SQLi cega por condição booleana e por atraso no tempo de resposta
- Bypass de filtros, validações e sistemas de proteção (WAF)
- Injeção em formatos não convencionais: XML e JSON

#### 📌 SSRF – Server‑Side Request Forgery
**✅ Status: 7/7 laboratórios trabalhados – metodologia 100% dominada**
> **Conceito**: Vulnerabilidade que permite ao atacante manipular requisições feitas pela própria aplicação, transformando o servidor em um "proxy" para acessar recursos internos ou restritos da rede.

| Laboratório | Técnicas Aplicadas | Resultado |
|---|---|---|
| Basic SSRF against the local server | Manipulação de parâmetro para `http://127.0.0.1/admin` | Acesso a interfaces administrativas locais |
| Basic SSRF against another back‑end system | Alteração para IPs da faixa `192.168.0.0/24` | Acesso a servidores internos sem exposição pública |
| SSRF with blacklist‑based filter | Representações alternativas de IP, domínios resolvidos para localhost | Bypass total de bloqueios |
| SSRF with filter via open redirection | Combinação com falha de redirecionamento aberto | Validação aceita, requisição direcionada ao alvo |
| Blind SSRF com detecção OAST | Cabeçalho `Referer` + Interactsh | Confirmação da falha sem retorno visível |
| SSRF com filtro de lista branca | Uso de `@`, `#` e codificação dupla: `http://stock.weliketoshop.net%2523@127.0.0.1/admin` | Validação aprovada e requisição executada para o servidor local |
| Blind SSRF com Shellshock | Cabeçalho `Referer` para `192.168.0.141:8080` + vetor `() { :; }; COMANDO` | Fluxo de ataque dominado; limitação apenas por restrição da plataforma |

> **Principais aprendizados**: Listas brancas não são mais seguras que listas negras; é possível encadear vulnerabilidades; cabeçalhos aparentemente inofensivos são vetores válidos; técnicas OAST são essenciais para explorações cegas.

#### 📌 XML External Entity (XXE) Injection
**✅ Status: 7/7 laboratórios – conceitos e exploração 100% dominados**
> **Conceito**: Falha no processamento de arquivos XML que permite a declaração de entidades externas, possibilitando leitura de arquivos locais, requisições arbitrárias e até execução de código em alguns cenários.

| Laboratório | Nível | Status | Técnica Principal |
|---|---|---|---|
| Exploiting XXE to retrieve files | Aprendiz | ✅ Resolvido | Declaração de entidade externa apontando para caminhos do sistema |
| Exploiting XXE to perform SSRF | Aprendiz | ✅ Resolvido | Uso de entidades para fazer requisições do servidor a alvos internos |
| Blind XXE com interação fora de banda | Praticante | ✅ Resolvido | Detecção via consultas DNS/HTTP para servidor controlado |
| Blind XXE com entidades de parâmetro | Praticante | ✅ Conceito dominado | Aplicação de entidades de parâmetro e DTDs externas |
| Blind XXE com extração via DTD maliciosa | Praticante | ✅ Resolvido | Hospedagem de DTD externa para enviar dados para fora |
| Blind XXE com extração via mensagens de erro | Praticante | ✅ Resolvido | Forçar retorno de erros contendo o conteúdo alvo |
| Exploiting XInclude para leitura de arquivos | Praticante | ✅ Resolvido | Uso da instrução `XInclude` sem alterar a estrutura raiz do XML |

> ℹ️ **Observação**: O laboratório *Blind XXE com entidades de parâmetro* não foi marcado automaticamente na plataforma pois a versão gratuita do Burp não inclui o Collaborator, e a PortSwigger bloqueia serviços externos como o Interactsh. Toda a lógica, fluxo de ataque e técnicas foram compreendidas e aplicadas corretamente — trata‑se apenas de limitação de ferramenta, não de domínio do assunto.

> **Principais aprendizados**: O processamento de XML pode ser explorado de formas não óbvias; falhas cegas não impedem extração de dados; entidades de parâmetro e DTDs externas ampliam as possibilidades de ataque.

#### 📌 Command Injection
**✅ Status: 100% concluído**
> **Conceito**: Ocorre quando entrada do usuário é enviada diretamente ao interpretador de comandos do SO sem sanitização, permitindo execução arbitrária.

- Básico: uso de separadores como `;`, `&`, `|` para encadear comandos
- Cego por atraso: detecção através do comando `sleep`
- Cego com extração fora de banda: requisição para domínio controlado confirmando a execução
> **Aprendizado**: Ausência de retorno visível não significa ausência de vulnerabilidade.

---

### 🟢 Manipulação de Requisições e Fluxos
**✅ Status: 100% concluído**
- CSRF básico e com contorno de validações
- Poluição de parâmetros e atribuição em massa
- Vulnerabilidades em tokens JWT e mecanismos de sessão

---

### 🔴 Tópicos a Iniciar
- SSTI: Injeção em mecanismos de renderização de templates
- Desserialização Insegura: Manipulação de objetos serializados
- Falhas em lógica de negócio
- Vulnerabilidades em APIs REST e GraphQL

---

## 🛠️ Ferramentas Utilizadas
- **Burp Suite Community Edition**: Interceptação, análise e modificação de requisições
- **Interactsh**: Serviço OAST gratuito para detecção e extração em ataques cegos
- **Ferramentas do navegador**: Depurador, análise de rede e inspeção de requisições
- **Utilitários de linha**: `curl`, `nslookup`, `ping`

---

## 📚 Referências
- PortSwigger Web Security Academy
- OWASP Top 10
- OWASP Cheat Sheet Series
- HackTricks

---

⚠️ **Aviso Legal**
Todos os testes e análises foram realizados exclusivamente em ambientes autorizados e controlados, para fins de estudo e pesquisa em segurança da informação. Não aplique as técnicas descritas em sistemas ou aplicações sem permissão explícita do responsável.

---
