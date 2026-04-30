Blind OS Command Injection with Output Redirection
🎯 Objetivo

Explorar uma vulnerabilidade de Blind OS Command Injection utilizando redirecionamento de saída para obter evidência da execução de comandos no servidor.

🧠 Resumo

A aplicação executava comandos do sistema operacional com base em entrada do usuário, porém não retornava a saída diretamente.

Para contornar essa limitação, foi utilizada a técnica de output redirection, salvando o resultado do comando em um recurso acessível pela aplicação.

🔍 Metodologia
1. Identificação do ponto vulnerável
Um parâmetro da aplicação era utilizado na execução de comandos do sistema
Não havia retorno direto da saída (cenário blind)
2. Teste de injeção
Inserção de operadores (;, &&) para encadear comandos
Confirmação de que comandos adicionais eram processados
3. Exploração via redirecionamento
Utilização de redirecionamento de saída (>)
O resultado do comando foi salvo em um arquivo dentro de um diretório acessível

👉 Exemplo de abordagem:

redirecionar saída para um arquivo público da aplicação
4. Validação
Acesso ao arquivo gerado
Confirmação da execução do comando com base no conteúdo armazenado
⚙️ Ferramentas
Burp Suite
Repeater
Browser
🧩 Insight principal

Mesmo sem retorno direto, é possível extrair informações através de efeitos indiretos, como armazenamento da saída em locais acessíveis.

Isso permite:

confirmação de execução de comandos
exfiltração de dados do servidor
exploração silenciosa da aplicação
📌 Aprendizados
Blind command injection pode ser explorada de várias formas
Output redirection é uma técnica eficiente para obter dados
Controle de permissões em diretórios é crítico
Falhas desse tipo podem levar a comprometimento total do sistema
🚀 Conclusão

O lab demonstra como vulnerabilidades de command injection podem ser exploradas mesmo sem retorno direto, utilizando redirecionamento de saída para obter evidência e extrair informações do servidor
