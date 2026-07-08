🔒 Web Security Labs – PortSwigger Red Team Practice
(mantém o cabeçalho, badges e estrutura geral como antes)
📌 SSRF – Server-Side Request Forgery
🟡 Status: 6/7 laboratórios concluídos
Conceito: Vulnerabilidade que permite ao atacante fazer com que o servidor da aplicação envie requisições arbitrárias para destinos internos ou externos, acessando recursos que não seriam diretamente visíveis ao usuário.
Laboratórios resolvidos:

    Basic SSRF against the local server
        Manipulação de URL para acessar serviços restritos no próprio servidor (localhost)
    Basic SSRF against another back-end system
        Comunicação com máquinas da rede interna, inacessíveis da internet
    SSRF with blacklist-based input filter
        Contorno de restrições através de variações na formatação e codificação de endereços
    SSRF with filter bypass via open redirection
        Combinação com redirecionamento aberto para driblar validações de domínio
    Blind SSRF with out-of-band detection ✅
        Cenário sem retorno de dados visíveis
        Técnica: Detecção via canal fora de banda (OAST)
        Vetor: Cabeçalho HTTP Referer
        Ferramenta: Interactsh
        Resultado: Confirmação por consultas DNS e requisições HTTP no servidor de escuta
    SSRF with whitelist-based input filter ✅ Resolvido agora
        Desafio: A aplicação aceitava apenas URLs contendo o domínio stock.weliketoshop.net (lista branca)
        Problema: Diferença de interpretação entre o validador de entrada e o cliente HTTP do servidor
        Técnica aplicada:
            Uso do caractere @ para inserir "credenciais" fictícias
            Uso de # (fragmento) e codificação dupla para enganar o parser de validação
        Payload final:
        plaintext

http://stock.weliketoshop.net%2523@127.0.0.1/admin

Codificado para envio:
plaintext

        stockApi=http%3A%2F%2Fstock.weliketoshop.net%2523%40127.0.0.1%2Fadmin

        Resultado: Acesso bem-sucedido à interface administrativa interna e exclusão do usuário alvo

Laboratório restante:

    Blind SSRF with Shellshock exploitation

Principais aprendizados:

    Listas brancas não são infalíveis — dependem totalmente de uma análise consistente em todas as etapas
    Diferenças na interpretação de URLs entre validação e requisição = brecha de segurança
    Codificações duplas e recursos padrão da URI (@, #, etc.) são ferramentas comuns de bypass
