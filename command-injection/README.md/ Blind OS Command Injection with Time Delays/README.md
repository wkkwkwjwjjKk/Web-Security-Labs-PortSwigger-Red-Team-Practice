🧪 Blind OS Command Injection with Time Delays
🎯 Objetivo

Explorar uma vulnerabilidade de Blind OS Command Injection utilizando time delays para confirmar a execução de comandos no servidor.

🧠 Resumo

A aplicação executava comandos do sistema operacional com base em entrada do usuário, porém não retornava a saída diretamente.

Para confirmar a vulnerabilidade, foi utilizada a técnica de time-based injection, onde comandos que causam atraso na resposta permitem inferir a execução no servidor.

🔍 Metodologia
1. Identificação do ponto vulnerável
Um parâmetro da aplicação era processado pelo sistema operacional
Não havia retorno direto da execução (cenário blind)
2. Teste de injeção
Inserção de operadores de comando (;, &&)
Introdução de comandos que geram atraso proposital

👉 Exemplo de abordagem:

uso de comandos como sleep para atrasar a resposta
3. Confirmação da vulnerabilidade
Observação do tempo de resposta da aplicação
Requisições com payload malicioso apresentaram atraso consistente

👉 Isso confirmou a execução do comando no servidor

4. Exploração
Uso de delays controlados para validar comportamento
Possibilidade de evoluir para exfiltração de dados em cenários mais avançados
⚙️ Ferramentas
Burp Suite
Repeater
Intruder (opcional para automação)
🧩 Insight principal

Mesmo sem retorno direto, a execução de comandos pode ser detectada através de efeitos colaterais, como tempo de resposta.

Isso permite:

identificação de vulnerabilidades blind
confirmação de execução remota de comandos
base para exploração mais avançada
📌 Aprendizados
Blind vulnerabilities exigem técnicas indiretas de validação
Time delays são uma forma eficaz de confirmar execução
Segurança não deve depender da ausência de output
Monitoramento de comportamento é essencial em testes
🚀 Conclusão

O lab demonstra como vulnerabilidades de command injection podem ser exploradas mesmo sem retorno visível, utilizando técnicas baseadas em tempo para confirmar a execução no servidor.
