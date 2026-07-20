Web Security Labs – PortSwigger Red Team Practice
Documentação completa de laboratórios práticos de segurança ofensiva web, com foco em exploração manual, análise de vulnerabilidades e desenvolvimento de raciocínio de ataque.

Detalhes gerais:
- Nível: Intermediário a Avançado
- Plataforma: PortSwigger Web Security Academy
- Idioma: Português (PT-BR)
- Total de laboratórios: 20
- Conceitos dominados: 16
- Progresso geral: 80%

Status Geral do Repositório:
- Concluído / Conceito Dominado: 16 (80%)
- Em Estudo: 0 (0%)
- Não Iniciado: 4 (20%)

Roteiro de Estudo por Nível:
Iniciante:
- Autenticação e controle de acesso
- SQL Injection básica
- Conceitos fundamentais de requisições HTTP
- Tempo estimado: ~4 horas

Intermediário:
- Injeções avançadas: SQLi cega, SSRF, Command Injection
- Manipulação de cabeçalhos, parâmetros e URLs
- Técnicas OAST para detecção e extração sem retorno visível
- Tempo estimado: ~15 horas

Avançado:
- XXE, SSTI e Desserialização Insegura
- Análise e exploração de falhas em lógica de negócio
- Testes e segurança em APIs
- Tempo estimado: ~20 horas

Categorias e Laboratórios:

Autenticação e Controle de Acesso
Status: 100% concluído
- Enumeração de usuários e contas
- Bypass de limites de tentativas e bloqueios
- Contornos em fluxos de autenticação de dois fatores (2FA)
- Vulnerabilidades em OAuth e OpenID Connect
- Escalonamento de privilégios e falhas de referência de objeto direto (IDOR)

Injeção de Código e Comandos

SQL Injection
Status: 9/9 laboratórios concluídos
- Injeção simples com uso de UNION para extração de dados
- Enumeração de esquemas, tabelas e colunas do banco
- SQLi cega por condição booleana e por atraso no tempo de resposta
- Bypass de filtros, validações e sistemas de proteção (WAF)
- Injeção em formatos não convencionais: XML e JSON

SSRF – Server-Side Request Forgery
Status: 7/7 laboratórios trabalhados – metodologia 100% dominada
Conceito: Vulnerabilidade que permite ao atacante manipular requisições feitas pela própria aplicação, transformando o servidor em um proxy para acessar recursos internos ou restritos da rede.

Laboratórios:
- Basic SSRF against the local server: Manipulação para http://127.0.0.1/admin – Acesso a interfaces administrativas locais
- Basic SSRF against another back-end system: Alteração para IPs 192.168.0.0/24 – Acesso a servidores internos
- SSRF with blacklist-based filter: Representações alternativas de IP e domínios – Bypass total de bloqueios
- SSRF with filter via open redirection: Combinação com redirecionamento aberto – Validação aceita
- Blind SSRF com detecção OAST: Cabeçalho Referer + Interactsh – Confirmação sem retorno visível
- SSRF com filtro de lista branca: Uso de @, # e codificação dupla – Validação aprovada e requisição para local
- Blind SSRF com Shellshock: Referer para 192.168.0.141:8080 – Fluxo dominado, limitação só da plataforma

Aprendizados: Listas brancas não são mais seguras; é possível encadear falhas; cabeçalhos são vetores válidos; OAST é essencial.

XML External Entity (XXE) Injection
Status: 7/7 laboratórios – conceitos e exploração 100% dominados
Conceito: Falha no processamento de XML que permite entidades externas, possibilitando leitura de arquivos, SSRF e extração de dados.

Laboratórios:
- Exploiting XXE to retrieve files – Aprendiz – Resolvido – Entidade externa para arquivos locais
- Exploiting XXE to perform SSRF – Aprendiz – Resolvido – Requisições para destinos internos
- Blind XXE com interação fora de banda – Praticante – Resolvido – Detecção por OAST
- Blind XXE com entidades de parâmetro – Praticante – Conceito dominado – Uso de entidades de parâmetro e DTDs
  Observação: Não marcado automaticamente porque a versão gratuita do Burp não tem Collaborator e a PortSwigger bloqueia serviços externos. Todo o conhecimento foi aplicado corretamente.
- Blind XXE com extração via DTD maliciosa – Praticante – Resolvido – Extração por DTD externa
- Blind XXE com extração via mensagens de erro – Praticante – Resolvido – Forçar erro com conteúdo alvo
- Exploiting XInclude para leitura de arquivos – Praticante – Resolvido – Uso de XInclude sem mudar estrutura do XML

Aprendizados: Processamento de XML tem várias falhas; sem retorno visível ainda é possível extrair dados; entidades de parâmetro ampliam possibilidades.

Command Injection
Status: 100% concluído
Conceito: Entrada do usuário enviada direta ao sistema operacional sem validação, permitindo comandos arbitrários.
- Básico: Uso de separadores como ;, &, |
- Cego por atraso: Detecção com comando sleep
- Cego com extração fora de banda: Requisição para domínio controlado
Aprendizado: Sem retorno visível não significa sem vulnerabilidade.

Manipulação de Requisições e Fluxos
Status: 100% concluído
- CSRF básico e com contornos
- Poluição de parâmetros e atribuição em massa
- Vulnerabilidades em JWT e sessões

Tópicos a Iniciar:
- SSTI: Injeção em templates
- Desserialização Insegura
- Falhas em lógica de negócio
- Segurança em APIs REST e GraphQL

Ferramentas Utilizadas:
- Burp Suite Community Edition
- Interactsh
- Ferramentas do navegador
- curl, nslookup, ping

Referências:
- PortSwigger Web Security Academy
- OWASP Top 10
- OWASP Cheat Sheet Series
- HackTricks

Aviso Legal:
Todos os testes foram feitos em ambientes autorizados, só para estudo. Não use essas técnicas em sistemas sem permissão.
