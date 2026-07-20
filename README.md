---

# 📑 Web Security Labs – PortSwigger | Red Team Practice
**Documentação completa de estudo e domínio de vulnerabilidades web ofensivas, com foco em exploração manual, análise crítica e desenvolvimento de raciocínio de ataque.**

---

## 📋 Dados Gerais
| Item | Detalhe |
|---|---|
| **Nível** | Intermediário a Avançado |
| **Plataforma** | PortSwigger Web Security Academy |
| **Idioma** | Português (PT-BR) |
| **Total de laboratórios mapeados** | 20 |
| **Conceitos totalmente dominados** | 16 |
| **Progresso geral** | 80% |
| **Concluído / Dominado** | 16 (80%) |
| **Em estudo** | 0 (0%) |
| **Não iniciado** | 4 (20%) |

---

## 🗺️ Roteiro de Estudo por Nível
### Iniciante – Fundamentos sólidos
- Autenticação e controle de acesso
- SQL Injection básica
- Conceitos fundamentais de requisições HTTP
- **Tempo estimado gasto**: ~4 horas

### Intermediário – Técnicas de exploração
- Injeções avançadas: SQLi cega, SSRF, Command Injection
- Manipulação de cabeçalhos, parâmetros, caminhos e URLs
- Técnicas OAST para detecção e extração sem retorno visível
- **Tempo estimado gasto**: ~15 horas

### Avançado – Exploração complexa
- XXE em todas as variantes, SSTI e Desserialização Insegura
- Análise e exploração de falhas em lógica de negócio
- Testes e segurança em APIs REST e GraphQL
- **Tempo estimado gasto**: ~20 horas

---

## 📂 Categorias e Laboratórios – Detalhamento do Conhecimento Adquirido

### 🔐 Autenticação e Controle de Acesso
**Status: 100% concluído e dominado**
- Enumeração de usuários e contas
- Bypass de limites de tentativas e bloqueios de taxa
- Contornos em fluxos de autenticação de dois fatores (2FA)
- Vulnerabilidades em fluxos OAuth e OpenID Connect
- Escalonamento de privilégios e falhas de Referência de Objeto Direto (IDOR)

---

### 💉 Injeção de Código e Comandos

#### SQL Injection
**Status: 9/9 laboratórios concluídos – metodologia 100% dominada**
- Injeção simples com `UNION` para extração direta de dados
- Enumeração completa de esquemas, tabelas e colunas do banco de dados
- SQLi cega por comparação booleana e por atraso no tempo de resposta
- Bypass de filtros, validações e sistemas de proteção como WAF
- Injeção em formatos estruturados: XML e JSON

#### SSRF – Server-Side Request Forgery
**Status: 7/7 laboratórios trabalhados – conceito e exploração 100% dominados**
> **Conceito dominado**: Falha que permite manipular requisições feitas pela própria aplicação, transformando o servidor em um proxy para acessar recursos internos, restritos ou externos.

**Laboratórios explorados e lições aprendidas:**
- *Basic SSRF against the local server*: Manipulação para `http://127.0.0.1/admin` → Acesso a interfaces administrativas locais
- *Basic SSRF against another back-end system*: Alteração para faixas como `192.168.0.0/24` → Acesso a servidores internos da rede
- *SSRF with blacklist-based filter*: Representações alternativas de IP, hexadecimal e domínios → Bypass total de listas negras
- *SSRF with filter via open redirection*: Combinação com redirecionamento aberto → Validação contornada com sucesso
- *Blind SSRF com detecção OAST*: Cabeçalho `Referer` + Interactsh → Confirmação da falha sem retorno visível na resposta
- *SSRF com filtro de lista branca*: Uso de `@`, `#`, codificação e manipulação de porta → Validação de lista branca contornada
- *Blind SSRF com Shellshock*: Exploração combinada com vetor em cabeçalhos → Fluxo dominado, limitação apenas de ambiente da plataforma

**Aprendizados consolidados:** Listas brancas não são garantia de segurança; é possível encadear vulnerabilidades; cabeçalhos não convencionais são vetores válidos; técnicas OAST são fundamentais para falhas cegas.

---

#### XML External Entity (XXE) Injection
**Status: 7/7 laboratórios – todos os conceitos e técnicas de exploração 100% dominados**
> **Conceito dominado**: Falha no processamento de entradas XML que aceitam definição de entidades externas, permitindo leitura de arquivos locais, requisições arbitrárias (SSRF) e extração de dados de diversas formas.

**Laboratórios explorados e lições aprendidas:**
- *Exploiting XXE to retrieve files* – Aprendiz ✅ Resolvido: Entidade externa para leitura direta de arquivos como `/etc/passwd`
- *Exploiting XXE to perform SSRF* – Aprendiz ✅ Resolvido: Uso de entidades para fazer requisições a destinos internos
- *Blind XXE com interação fora de banda* – Praticante ✅ Resolvido: Detecção e extração via requisições para servidor controlado
- *Blind XXE com entidades de parâmetro* – Praticante 🧠 **Conceito totalmente dominado**: Uso de entidades de parâmetro (`%entidade;`) e DTDs para exploração mais avançada  
  *Observação*: Não marcado automaticamente como resolvido pois a versão gratuita do Burp Suite não dispõe do Collaborator nativo, e a plataforma restringe serviços externos. Toda a lógica e payloads foram aplicados corretamente.
- *Blind XXE com extração via DTD maliciosa* – Praticante ✅ Resolvido: Extração de dados carregando DTD externo
- *Blind XXE com extração via mensagens de erro* – Praticante ✅ Resolvido: Forçar mensagens de erro que revelam o conteúdo do arquivo alvo
- *Exploiting XInclude para leitura de arquivos* – Praticante ✅ Resolvido: Uso da instrução nativa `XInclude` quando não temos controle sobre todo o documento XML
- *Exploiting XXE via image file upload* – Praticante ✅ Resolvido: Exploração através de arquivos SVG, formato nativo XML
- *Exploiting XXE repurposing DTD local* – Especialista ✅ Resolvido: Reutilização de arquivos DTD que já existem no servidor alvo para contornar restrições de carregamento externo

**Aprendizados consolidados:** O processamento XML apresenta múltiplas superfícies de ataque; mesmo sem retorno visível é possível extrair dados; entidades de parâmetro ampliam muito as possibilidades de exploração; formatos como SVG são vetores pouco evidentes mas altamente eficazes.

---

#### Command Injection
**Status: 100% concluído e dominado**
> **Conceito dominado**: Ocorre quando a entrada do usuário é enviada diretamente ao interpretador de comandos do sistema operacional sem validação ou sanitização adequada.

- Básico: Uso de separadores como `;`, `&`, `|` e quebras de linha
- Cego por atraso: Detecção da falha através de comandos como `sleep`
- Cego com extração fora de banda: Envio da saída do comando para um servidor controlado

**Aprendizado consolidado:** A ausência de retorno visível na resposta não significa que a vulnerabilidade não exista.

---

### 🔄 Manipulação de Requisições e Fluxos
**Status: 100% concluído e dominado**
- CSRF básico e técnicas de contorno de proteções
- Poluição de parâmetros e falhas de atribuição em massa
- Vulnerabilidades em tokens JWT e gestão de sessões

---

## 🚧 Tópicos a Iniciar em Breve
- SSTI: Injeção em motores de template
- Desserialização Insegura
- Falhas em lógica de negócio
- Segurança em APIs REST e GraphQL

---

## 🛠️ Ferramentas Utilizadas no Estudo
- Burp Suite Community Edition
- Interactsh
- Ferramentas nativas de desenvolvedor dos navegadores
- Utilitários de terminal: `curl`, `nslookup`, `ping`, `cat`, `grep`

---

## 📚 Referências Técnicas
- PortSwigger Web Security Academy
- OWASP Top 10
- OWASP Cheat Sheet Series
- HackTricks

---

✅ **Observação final**: Todo o conteúdo reflete o conhecimento efetivamente adquirido e aplicado em laboratório. Eventuais itens não marcados como "resolvido" na plataforma se devem exclusivamente a limitações da versão gratuita das ferramentas, sem prejuízo ao domínio das técnicas e conceitos abordados.

---
