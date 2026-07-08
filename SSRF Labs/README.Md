# SSRF Labs - PortSwigger Web Security Academy

O objetivo é documentar técnicas de exploração, raciocínio e evolução prática em cenários de Server-Side Request Forgery (SSRF).

---

## 📊 Status Geral

| Lab | Dificuldade | Status |
|-----|------------|--------|
| Basic SSRF against the local server | Apprentice | ✅ Solved |
| Basic SSRF against another back-end system | Apprentice | ✅ Solved |
| Blind SSRF with out-of-band detection | Practitioner | ✅ Solved |
| SSRF with blacklist-based input filter | Practitioner | ✅ Solved |
| SSRF with filter bypass via open redirection vulnerability | Practitioner | ✅ Solved |
| Blind SSRF with Shellshock exploitation | Expert | ❌ Not solved |
| SSRF with whitelist-based input filter | Expert | ❌ Not solved |

---

## 🧠 Overview Técnico

Durante os laboratórios de SSRF, foram explorados diferentes vetores de ataque contra requisições processadas no lado do servidor, incluindo:

- Acesso a recursos e serviços internos restritos (`localhost`, IPs de rede privada)
- Manipulação de URLs enviadas pelo usuário e interpretadas pelo backend
- Bypass de filtros de validação baseados em lista negra (*blacklist*) e lista branca (*whitelist*)
- Encadeamento de vulnerabilidades para ampliar o alcance do ataque
- Detecção e confirmação de SSRF em cenários cegos, sem retorno direto de dados

---

## 🟢 Labs Resolvidos

### 1. Basic SSRF against the local server (Apprentice)

Foi possível explorar um parâmetro vulnerável que aceita URLs arbitrárias, alterando o destino para `localhost`. Isso permitiu acessar serviços e endpoints restritos, disponíveis apenas internamente no servidor.

---

### 2. Basic SSRF against another back-end system (Apprentice)

A falha foi utilizada para se comunicar com sistemas e serviços localizados em rede interna, que não são acessíveis diretamente pela internet externa, demonstrando o risco de reconhecimento e acesso a infraestrutura privada.

---

### 3. SSRF with blacklist-based input filter (Practitioner)

Foi identificado um mecanismo de proteção que bloqueava termos e endereços considerados perigosos, usando uma estratégia de lista negra.

O bypass foi realizado por meio de variações na formatação da URL e codificação de caracteres, explorando diferenças na forma como a aplicação valida e interpreta o endereço final, conseguindo acessar recursos internos mesmo com a restrição.

---

### 4. SSRF with filter bypass via open redirection vulnerability (Practitioner)

A exploração se deu por meio do encadeamento de duas vulnerabilidades: SSRF e Redirecionamento Aberto.

Em vez de inserir o endereço alvo diretamente, utilizou-se o ponto de redirecionamento existente na própria aplicação para contornar o filtro, fazendo com que o servidor seguisse o caminho até o recurso interno desejado.

---

### 5. Blind SSRF with out-of-band detection (Practitioner)

Nesse cenário, a aplicação executa a requisição solicitada, mas **não retorna nenhum conteúdo ou resposta visível** para o usuário — caracterizando o SSRF cego.

Para confirmar a vulnerabilidade, utilizou-se a técnica de detecção por canal fora de banda (*OAST*), por meio da ferramenta gratuita **Interactsh**, que funciona como um servidor de escuta. O vetor de injeção foi o cabeçalho HTTP `Referer`:

**Payload utilizado:**
```http
Referer: http://dxxaivjuswnuqtnyvvesd613cpeklpwu4.oast.fun/

Ao enviar a requisição, foi registrada comunicação no servidor de escuta: foram observadas consultas de DNS e requisições HTTP, comprovando que o servidor da aplicação acessou o endereço externo definido.
🔴 Labs Não Resolvidos / Em Progresso
Blind SSRF with Shellshock exploitation (Expert)
Exploração avançada que combina SSRF cego com a falha Shellshock, permitindo potencialmente a execução remota de comandos no servidor alvo.
Em estudo do funcionamento da falha, dos cabeçalhos HTTP manipuláveis e dos pré-requisitos do ambiente para que o ataque seja bem-sucedido.
SSRF with whitelist-based input filter (Expert)
A aplicação adota uma estratégia mais rigorosa, permitindo apenas endereços que estejam em uma lista de domínios autorizados.
Em investigação de técnicas de contorno, explorando falhas na análise sintática da URL, diferenças de interpretação entre módulos da aplicação e codificações alternativas.
🛠️ Técnicas Estudadas e Aplicadas

    Manipulação de componentes da URL (protocolo, domínio, caminho)
    Bypass de filtros de validação por codificação e formatação alternativa
    Encadeamento de vulnerabilidades (SSRF + Redirecionamento Aberto)
    Mapeamento e acesso a redes internas via SSRF
    Detecção de SSRF cego usando canal fora de banda (OAST)
    Identificação de vetores de injeção: parâmetros de entrada e cabeçalhos HTTP

🧠 Principais Aprendizados

    O SSRF não ocorre apenas em campos de entrada visíveis — pode estar presente também em cabeçalhos e configurações internas
    A segurança depende da forma como a aplicação interpreta e valida URLs, não apenas do que o usuário envia
    Filtros baseados em lista negra são, em geral, mais fáceis de contornar do que os baseados em lista branca
    Em ataques cegos, é necessário usar métodos indiretos para confirmar a existência da falha
    A combinação de vulnerabilidades simples pode resultar em um impacto muito maior do que cada uma isoladamente

📌 Observação
Todos os testes e explorações foram realizados exclusivamente no ambiente controlado e autorizado da PortSwigger Web Security Academy, com finalidade única de estudo e aprendizado em segurança da informação.
Este documento representa um registro de evolução contínua, reunindo laboratórios já concluídos e aqueles que ainda estão em fase de estudo.
