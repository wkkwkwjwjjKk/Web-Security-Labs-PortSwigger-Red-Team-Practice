🔐 Authentication Vulnerabilities – PortSwigger Web Security Academy
👨‍💻 Overview

Este repositório documenta estudos práticos sobre vulnerabilidades em autenticação baseada em senha, realizados na PortSwigger Web Security Academy.

O foco é entender como falhas simples em login podem levar a:

account takeover
username enumeration
bypass de brute-force protection
credential stuffing
falhas em HTTP Basic Auth

🧠 Conceitos estudados

🔑 Password-based authentication

Sistemas que utilizam login e senha assumem que:

“quem sabe a senha é o usuário legítimo”

Isso torna o sistema vulnerável quando credenciais podem ser:

adivinhadas
vazadas
brute-forçadas
💣 Brute-force attacks

Ataques automatizados de tentativa e erro para descobrir:

usernames
passwords
🔧 Técnicas usadas:
wordlists
automação (Burp Intruder)
lógica de padrões humanos (senhas previsíveis)
👤 Username enumeration

Técnica para descobrir se um username existe baseado em diferenças na resposta da aplicação.

Indicadores comuns:
🔹 HTTP status code diferente
🔹 mensagens de erro diferentes
🔹 variação no tempo de resposta
Impacto:

Reduz drasticamente o espaço de ataque para brute-force.

🔐 Password guessing patterns

Senhas frequentemente seguem padrões humanos:

password1!
Mypassword1
Mypassword2
variações previsíveis com símbolos/números

Isso permite ataques mais eficientes do que brute-force puro.

🚧 Flawed brute-force protection
🔒 1. Account locking
bloqueia conta após tentativas
pode ser bypassado com lógica de reset
🌐 2. IP blocking
bloqueia IP após várias tentativas
pode ser contornado com:
alternância de requests válidos
distribuição de tentativas
⚔️ Credential stuffing

Uso de credenciais reais vazadas:

username:password

Como muitos usuários reutilizam senhas, isso pode comprometer múltiplas contas com poucos requests.

⏱️ User rate limiting

Limita número de requests por IP.

Problemas comuns:

bypass por manipulação de IP
requisições múltiplas por request
lógica inconsistente no backend
🔐 HTTP Basic Authentication

Autenticação simples baseada em:

Authorization: Basic base64(username:password)
Problemas:
envia credenciais repetidamente
vulnerável a MITM (sem HSTS)
sem proteção contra brute-force
suscetível a CSRF em alguns cenários

🧪 Laboratórios estudados

🔹 Username enumeration via different responses
detecção de usernames válidos via diferença de respostas
🔹 Username enumeration via subtly different responses
análise de pequenas variações na resposta HTTP
🔹 Username enumeration via response timing
exploração de diferença de tempo de resposta
🔹 Broken brute-force protection (IP block)
bypass de bloqueio de IP
🔹 Username enumeration via account lock
exploração de lock de conta para enumeração
🔹 Broken brute-force protection (multiple credentials per request)
bypass de rate limit usando múltiplas tentativas
🔹 HTTP Basic Authentication exploitation
abuso de autenticação simples baseada em header

🧰 Ferramentas utilizadas

Burp Suite (Proxy / Intruder / Repeater)
Wordlists de usernames e passwords
Análise de HTTP responses
Browser integrado do Burp

🧠 Principais aprendizados

Autenticação baseada só em senha é fraca
Pequenas diferenças em responses revelam informação sensível
Proteções contra brute-force podem ser mal implementadas
Lógica de backend é mais importante que UI
APIs e login systems precisam de validação consistente

⚔️ Impacto real

Essas falhas podem permitir:

account takeover
acesso a contas admin
enumeração de usuários reais
acesso não autorizado a sistemas internos

🚀 Conclusão

Autenticação não falha por complexidade — falha por lógica mal implementada.

Mesmo sistemas modernos podem ser quebrados quando:

responses diferem minimamente
rate limiting é mal configurado
usernames são previsíveis
senhas seguem padrões humanos
