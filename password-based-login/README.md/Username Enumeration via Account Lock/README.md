 Username Enumeration via Account Lock
🎯 Objetivo
Explorar o mecanismo de bloqueio de conta (account lock) para identificar usuários válidos durante o processo de autenticação.

🧠 Resumo
A aplicação implementava um mecanismo de bloqueio após múltiplas tentativas de login falhas.
Esse comportamento permitia diferenciar usuários válidos de inválidos, já que apenas contas existentes eram bloqueadas após várias tentativas.

🔍 Metodologia
1. Testes iniciais


Foram enviadas múltiplas tentativas de login com diferentes usernames


Observou-se que algumas contas retornavam resposta de bloqueio após várias tentativas


👉 Isso indicava que esses usuários existiam

2. Confirmação


O comportamento foi reproduzido para validar consistência


Apenas usuários válidos acionavam o mecanismo de account lock



3. Exploração


Utilização do Burp Suite Intruder


Estratégia de automação para testar múltiplos usernames


Identificação de usuários válidos com base no comportamento de bloqueio


👉 Após a enumeração, ataques direcionados de autenticação se tornam possíveis

⚙️ Ferramentas


Burp Suite


Intruder


Wordlists



🧩 Insight principal
Mecanismos de bloqueio de conta podem introduzir vazamento de informação quando aplicados apenas a usuários válidos.
Isso permite:


enumeração de usuários


otimização de ataques de brute force


redução do espaço de tentativa



📌 Aprendizados


Diferenças de comportamento são exploráveis


Proteções mal implementadas podem criar novas vulnerabilidades


Enumeração é uma etapa crítica em ataques reais


Segurança deve padronizar respostas independentemente da existência do usuário



🚀 Conclusão
O lab demonstra como mecanismos de proteção, quando mal implementados, podem ser explorados para identificar usuários válidos e facilitar ataques subsequentes.

Se quiser, posso te fazer uma versão alternativa:
👉 mais curta (pra LinkedIn)
👉 ou mais “agressiva” estilo bug bounty (com mais impacto técnico)
