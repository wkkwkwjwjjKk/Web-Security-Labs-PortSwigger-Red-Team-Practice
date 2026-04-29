🧪 Username Enumeration via Different Responses
🎯 Objetivo

Explorar como diferenças nas respostas da aplicação podem permitir enumeração de usuários válidos durante o processo de autenticação.

🧠 Resumo

A aplicação retornava respostas diferentes dependendo se o username existia ou não no sistema.

Essa variação no comportamento permitia identificar contas válidas apenas analisando a resposta do servidor.

🔍 Metodologia
1. Enumeração de usuários
Foram enviados múltiplos requests de login com usernames diferentes
Observou-se diferença no comportamento das respostas (mensagem, tamanho ou conteúdo)
Um username específico apresentou resposta distinta
Isso indicou que o usuário existia no sistema
2. Validação do alvo
O username identificado foi testado novamente
O comportamento da resposta permaneceu consistente
Confirmação de conta válida
3. Exploração (força bruta direcionada)
Uso do Burp Suite Intruder
Modo de ataque: Cluster Bomb
Payloads:
Username fixo (válido)
Wordlist de senhas
Objetivo: identificar credencial válida via resposta da aplicação
⚙️ Ferramentas
Burp Suite
Intruder (Cluster Bomb)
Wordlist de senhas
🧩 Insight principal

Pequenas diferenças no comportamento da aplicação podem expor informações sensíveis, mesmo sem mensagens de erro explícitas.

Isso pode permitir:

enumeração de usuários
ataques direcionados de força bruta
aumento da eficiência de ataques de credential stuffing
📌 Aprendizados
Respostas de erro inconsistentes podem vazar informação
Enumeração de usuários é etapa inicial de ataques reais
Automação com Intruder aumenta eficiência do ataque
Pequenos detalhes de resposta são críticos em segurança web
🚀 Conclusão

O lab demonstra como falhas sutis no processo de autenticação podem ser exploradas para identificar usuários válidos e facilitar ataques subsequentes.
