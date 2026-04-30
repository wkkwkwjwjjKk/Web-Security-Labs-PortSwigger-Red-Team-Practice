🧪 Username Enumeration via Account Lock (Cluster Bomb)
🎯 Objetivo

Explorar o mecanismo de autenticação para identificar credenciais válidas utilizando enumeração simultânea de usuários e senhas.

🧠 Resumo

A aplicação apresentava comportamento diferente ao autenticar credenciais válidas, retornando um status HTTP 302 (redirect) após login bem-sucedido.

Essa diferença permitiu identificar combinações corretas de username e senha através de automação.

🔍 Metodologia
1. Preparação do ataque
Interceptação da requisição de login via Burp Suite
Identificação dos parâmetros de autenticação (username e password)
2. Configuração do ataque
Uso do Intruder
Modo: Cluster Bomb
Payloads:
Payload 1 → lista de usernames
Payload 2 → lista de senhas
3. Execução
O Intruder enviou múltiplas combinações de credenciais
A maioria das respostas retornava erro de autenticação (status padrão)
Uma requisição específica retornou:

👉 HTTP 302 Found (redirect)

4. Identificação da credencial válida
O código 302 indicava login bem-sucedido
A resposta foi isolada com base no status code
A combinação de username e senha correspondente foi identificada como válida
⚙️ Ferramentas
Burp Suite
Intruder (Cluster Bomb Attack)
Wordlists de usuários e senhas
🧩 Insight principal

Diferenças no comportamento da resposta HTTP, como códigos de status, podem ser utilizadas como indicador confiável de sucesso em ataques automatizados.

Isso permite:

enumeração de credenciais válidas
brute force eficiente
automação de ataques de autenticação
📌 Aprendizados
Status codes são indicadores críticos em testes de autenticação
Cluster Bomb permite testar múltiplos parâmetros simultaneamente
Automação reduz significativamente o tempo de exploração
Diferenças sutis de resposta são altamente exploráveis
🚀 Conclusão

O lab demonstra como a análise de respostas HTTP, combinada com automação via Cluster Bomb, permite identificar credenciais válidas de forma eficiente.
