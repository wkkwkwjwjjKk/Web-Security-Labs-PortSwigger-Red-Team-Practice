🧪 Username Enumeration via Response Timing
🎯 Objetivo

Explorar como diferenças no tempo de resposta da aplicação podem permitir a enumeração de usuários válidos durante o processo de autenticação.

🧠 Resumo

A aplicação apresentava tempos de resposta diferentes dependendo se o username existia ou não.

Essa variação temporal permitiu identificar usuários válidos mesmo sem diferenças visíveis na resposta.

🔍 Metodologia
1. Testes iniciais de login
Foram enviados múltiplos requests com usernames aleatórios
As respostas pareciam idênticas em conteúdo
Porém, ao analisar o tempo de resposta, foi identificada uma diferença consistente em alguns casos

👉 Isso indicou possível existência de usuário válido

2. Confirmação do usuário
O username suspeito foi testado novamente
O tempo de resposta continuou sendo significativamente diferente
Isso confirmou a existência da conta
3. Exploração
Com o username validado, seria possível realizar ataques direcionados de autenticação
Redução do espaço de tentativa em brute force ou credential stuffing
⚙️ Ferramentas
Burp Suite
Intruder
Wordlists de teste
🧩 Insight principal

Mesmo quando a aplicação padroniza mensagens de erro, diferenças no tempo de resposta podem vazar informações sensíveis.

Isso pode permitir:

enumeração de usuários
ataques direcionados de força bruta
redução do custo de ataques automatizados
📌 Aprendizados
Timing attacks são sutis e muitas vezes ignorados
Tempo de resposta pode ser um canal de vazamento de informação
Segurança de autenticação deve considerar comportamento e não apenas conteúdo
Automação é essencial para detectar diferenças pequenas
🚀 Conclusão

O lab demonstra como variações no tempo de resposta da aplicação podem ser exploradas para identificar usuários válidos, mesmo quando não há diferenças visíveis no conteúdo das respostas.
