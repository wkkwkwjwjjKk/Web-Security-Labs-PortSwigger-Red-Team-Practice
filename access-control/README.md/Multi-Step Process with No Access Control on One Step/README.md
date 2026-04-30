🧪 Multi-Step Process with No Access Control on One Step
🎯 Objetivo

Explorar uma falha de controle de acesso em um processo dividido em múltiplas etapas, onde uma das etapas críticas não possui verificação de autorização.

🧠 Resumo

A aplicação implementava um fluxo de múltiplas etapas para execução de uma ação sensível.

Embora algumas etapas possuíssem validação de permissões, uma etapa intermediária ou final não realizava nenhuma verificação de acesso, permitindo que a ação fosse executada diretamente.

🔍 Metodologia
1. Análise do fluxo da aplicação
Identificação de um processo dividido em múltiplas requisições
Observação de validações em etapas iniciais
2. Identificação da falha
Uma das etapas do fluxo não possuía controle de acesso
A aplicação confiava que o usuário havia passado pelas etapas anteriores

👉 Isso abriu possibilidade de acessar diretamente essa etapa

3. Exploração
Interceptação das requisições com Burp Suite
Requisição da etapa vulnerável foi reproduzida diretamente
A ação sensível foi executada sem passar pelas validações anteriores
⚙️ Ferramentas
Burp Suite
Proxy / Repeater
🧩 Insight principal

Aplicações que dependem de fluxos multi-step podem introduzir falhas críticas quando não validam permissões em todas as etapas.

Isso permite:

bypass de controle de acesso
execução de ações privilegiadas
manipulação direta de endpoints internos
📌 Aprendizados
Nunca confiar em fluxo de navegação para controle de acesso
Cada requisição deve validar autorização independentemente
Segurança deve ser aplicada em todas as etapas do processo
Ferramentas de interceptação facilitam identificação de falhas lógicas
🚀 Conclusão

O lab demonstra como falhas em processos multi-step podem ser exploradas para contornar mecanismos de autorização, permitindo execução de ações sensíveis sem as devidas permissões.
