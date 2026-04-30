🧪 OS Command Injection – Simple Case
🎯 Objetivo

Explorar uma vulnerabilidade de OS Command Injection em um cenário básico, permitindo a execução de comandos no servidor.

🧠 Resumo

A aplicação processava entrada do usuário e a utilizava diretamente em comandos do sistema operacional, sem validação adequada.

Isso permitia injetar comandos adicionais e controlar a execução no servidor.

🔍 Metodologia
1. Identificação do ponto de entrada
Um parâmetro da aplicação era utilizado para executar comandos no sistema
Não havia sanitização ou validação da entrada
2. Teste da vulnerabilidade
Foram inseridos operadores de comando (;, &&, |) na entrada
A aplicação executou comandos adicionais além do esperado

👉 Isso confirmou a existência de command injection

3. Exploração
Injeção de comandos simples para verificar execução
Exemplo de abordagem:
encadear comandos para obter resposta visível
observar alterações no comportamento da aplicação
⚙️ Ferramentas
Burp Suite
Repeater
Browser
🧩 Insight principal

Aplicações que executam comandos do sistema com entradas não confiáveis são altamente vulneráveis.

Isso pode permitir:

execução remota de comandos (RCE)
acesso ao sistema operacional
comprometimento total do servidor
📌 Aprendizados
Nunca confiar em input do usuário
Sanitização inadequada leva a falhas críticas
Operadores de shell são indicadores fortes de exploração
Command Injection é uma das vulnerabilidades mais impactantes
🚀 Conclusão

O lab demonstra como uma falha simples de validação pode levar à execução arbitrária de comandos no servidor, comprometendo completamente a aplicação
