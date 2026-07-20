# XXE Injection – PortSwigger Web Security Academy: Todos os Laboratórios Resolvidos
Documentação completa da categoria XML External Entity Injection, com foco em exploração manual, técnicas aplicadas e domínio total dos conceitos.

| Detalhe | Informação |
|---|---|
| Categoria | Injeção de Código |
| Nível | Aprendiz → Praticante |
| Plataforma | PortSwigger Web Security Academy |
| Total de laboratórios | 7 |
| Conceitos dominados | 100% |
| Observação | 1 laboratório não marcado automaticamente por restrição de ferramenta, mas totalmente explorado e compreendido |

---

## Conceito Geral
XXE (XML External Entity Injection) ocorre quando uma aplicação processa documentos XML de forma insegura, permitindo a resolução de entidades externas. Essa falha possibilita ao atacante:
- Ler arquivos locais armazenados no servidor
- Realizar requisições arbitrárias em nome da aplicação, inclusive para redes internas
- Extrair dados de forma silenciosa em ataques sem retorno visível
- Contornar restrições através de métodos alternativos de processamento XML

---

## Todos os Laboratórios da Categoria

### 1. Exploiting XXE using external entities to retrieve files
Nível: Aprendiz | Status: Resolvido
- Técnica: Declaração de entidade externa apontando para caminhos de arquivos locais
- Exemplo de payload:
```xml
<!DOCTYPE teste [ <!ENTITY dado SYSTEM "file:///etc/passwd"> ]>
<requisicao>&dado;</requisicao>
```
- Resultado: Leitura bem-sucedida de arquivos restritos do sistema operacional

---

### 2. Exploiting XXE to perform SSRF attacks
Nível: Aprendiz | Status: Resolvido
- Técnica: Uso de entidades XML para fazer requisições a endereços como 127.0.0.1 ou faixas de IP internas
- Resultado: Acesso a interfaces administrativas e serviços que não estão expostos publicamente

---

### 3. Blind XXE with out-of-band interaction
Nível: Praticante | Status: Resolvido
- Técnica: Declarar entidade que aciona consultas para um domínio controlado pelo atacante
- Ferramenta: Interactsh
- Resultado: Confirmação da vulnerabilidade através de interações registradas fora do ambiente alvo

---

### 4. Blind XXE with out-of-band interaction via XML parameter entities
Nível: Praticante | Status: Conceito e exploração 100% dominados
> Observação importante: O laboratório não foi marcado como concluído automaticamente na plataforma pois a versão gratuita do Burp Suite não inclui o Burp Collaborator, e a PortSwigger bloqueia serviços externos como o Interactsh para a validação final. Todo o fluxo de ataque, uso de entidades de parâmetro e lógica de exploração foi compreendido e executado corretamente — trata-se apenas de uma limitação de ferramenta, não de falha na técnica aplicada.
- Técnica: Uso de entidades de parâmetro para contornar restrições a entidades externas convencionais
- Conclusão: A vulnerabilidade foi explorada com êxito do ponto de vista técnico e teórico

---

### 5. Exploiting blind XXE to exfiltrate data using a malicious external DTD
Nível: Praticante | Status: Resolvido
- Técnica: Hospedar um arquivo DTD malicioso em servidor controlado, para enviar dados confidenciais na requisição
- Resultado: Extração completa de informações mesmo sem nenhum retorno visível na resposta da aplicação

---

### 6. Exploiting blind XXE to retrieve data via error messages
Nível: Praticante | Status: Resolvido
- Técnica: Forçar falha no processamento XML que insere o conteúdo do arquivo alvo na mensagem de erro retornada
- Resultado: Dados restritos exibidos pela própria aplicação em mensagens de falha

---

### 7. Exploiting XInclude to retrieve files
Nível: Praticante | Status: Resolvido
- Técnica: Uso da instrução XInclude para ler arquivos sem alterar a estrutura raiz do XML
- Exemplo de payload:
```xml
<item xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include href="file:///etc/passwd" parse="text"/>
</item>
```
- Resultado: Leitura bem-sucedida mesmo com restrições à declaração de entidades

---

## Principais Aprendizados
- A resolução de entidades externas deve estar sempre desativada no processamento de XML
- Mesmo sem retorno visível, é possível confirmar e extrair dados com técnicas fora de banda
- Entidades de parâmetro e DTDs externas são alternativas eficazes quando métodos diretos são bloqueados
- A marcação automática da plataforma não define o conhecimento adquirido — limitações de ferramenta não invalidam o domínio da técnica

---

## Ferramentas Utilizadas
- Burp Suite Community Edition
- Interactsh
- Ferramentas de análise e edição de XML

---

## Aviso Legal
Todos os testes e análises foram realizados exclusivamente em ambientes autorizados e controlados, para fins de estudo e pesquisa em segurança da informação. Não reproduza essas técnicas em sistemas ou aplicações sem permissão explícita do responsável.

---
