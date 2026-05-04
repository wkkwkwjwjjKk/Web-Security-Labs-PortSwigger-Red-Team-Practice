🧪 Lab — 2FA Simple Bypass
🎯 Objetivo

Explorar uma falha na implementação de autenticação em dois fatores (2FA), permitindo acessar a conta de outro usuário sem a necessidade do código de verificação.

Credenciais fornecidas:

Usuário: wiener:peter
Usuário vítima: carlos:montoya
🔍 Análise inicial

Ao realizar login com o usuário wiener, o sistema solicita um código de verificação 2FA enviado por e-mail, indicando que a autenticação em dois fatores está ativa.

Após o login, o usuário é redirecionado para a etapa de verificação do código.

🧪 Processo de exploração
Realizei login na aplicação com minhas credenciais (wiener:peter).
O sistema solicitou o código 2FA enviado por e-mail.
Acessei a funcionalidade de e-mail fornecida pelo laboratório e obtive o código de verificação.
Naveguei até a página da conta (/my-account) e anotei a URL.
Realizei logout da conta.
Em seguida, realizei login com as credenciais da vítima (carlos:montoya).
Quando o sistema solicitou o código 2FA, ao invés de inseri-lo, alterei manualmente a URL no navegador para:
/my-account
💥 Resultado

A aplicação permitiu o acesso direto à conta do usuário carlos sem validação do código 2FA, resultando em bypass completo da autenticação em dois fatores.

O lab foi solucionado com sucesso.

🧠 Causa raiz
O sistema não valida corretamente a conclusão da etapa 2FA antes de permitir acesso a rotas protegidas
A autenticação é baseada apenas no estado de login inicial
Falta de controle de sessão indicando “2FA concluído”
🛡️ Mitigação
Garantir que todas as rotas protegidas verifiquem se o 2FA foi concluído
Implementar flag de sessão como “fully authenticated” apenas após verificação do código
Bloquear acesso direto a endpoints sensíveis sem validação completa
📌 Aprendizado

Este laboratório demonstra como falhas na gestão de fluxo de autenticação permitem bypass completo de 2FA apenas manipulando a navegação da aplicação.
