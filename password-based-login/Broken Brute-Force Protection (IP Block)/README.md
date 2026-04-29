🧪 Lab: Broken Brute-Force Protection (IP Block)
🎯 Objetivo

Explorar falhas no mecanismo de proteção contra força bruta baseado em bloqueio de IP, permitindo bypass e tentativa de múltiplas credenciais.

🧠 Resumo

A aplicação implementava um sistema de bloqueio de IP após múltiplas tentativas de login falhas.

No entanto, esse mecanismo podia ser contornado, permitindo continuar os ataques de brute force sem ser bloqueado.

🔍 Metodologia
1. Testes iniciais
Foram realizadas tentativas de login com credenciais inválidas
Após algumas falhas, o IP foi bloqueado
A aplicação passou a impedir novas tentativas
2. Identificação da falha
O bloqueio de IP não era aplicado de forma consistente
Alternando requisições com credenciais válidas e inválidas, o bloqueio podia ser “resetado”
Isso permitiu contornar a proteção
3. Exploração (brute force)
Uso do Burp Suite Intruder
Estratégia de ataque com controle de tentativas
Intercalamento de requisições para evitar bloqueio
Identificação de credenciais válidas
⚙️ Ferramentas
Burp Suite
Intruder
Wordlist de senhas
🧩 Insight principal

Mecanismos de bloqueio baseados apenas em IP podem ser facilmente contornados se não forem implementados corretamente.

Isso pode permitir:

ataques de força bruta contínuos
bypass de rate limiting
comprometimento de contas
📌 Aprendizados
Proteções baseadas apenas em IP são frágeis
Rate limiting precisa considerar sessão/usuário além do IP
Automação pode explorar falhas de lógica em proteção
Segurança de autenticação exige múltiplas camadas
🚀 Conclusão

O lab demonstra como uma implementação fraca de bloqueio por IP pode ser contornada, permitindo ataques de força bruta mesmo com mecanismos de proteção ativos.
