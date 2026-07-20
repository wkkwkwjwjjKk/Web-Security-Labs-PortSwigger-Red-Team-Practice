---

# 🔒 XXE Injection – PortSwigger Web Security Academy
**Documentação completa da categoria XML External Entity Injection, com foco em técnicas, exploração manual e domínio do conceito.**

| Detalhe | Informação |
|---|---|
| Categoria | Injeção de Código |
| Nível | Aprendiz → Praticante |
| Plataforma | PortSwigger Web Security Academy |
| Total de laboratórios | 7 |
| Resolvidos tecnicamente | 7 |
| Progresso | **100% dos conceitos dominados** |

---

## 📌 Conceito Geral
XXE (XML External Entity Injection) ocorre quando uma aplicação processa documentos XML permitindo a resolução de entidades externas. Isso possibilita ao atacante:
- Ler arquivos locais do servidor
- Realizar requisições em nome da aplicação (SSRF interno)
- Extrair dados em cenários sem retorno visível
- Explorar falhas em processamento de dados estruturados

---

## 🧪 Todos os Laboratórios da Categoria

### 1. Exploiting XXE using external entities to retrieve files
**Nível**: Aprendiz | **Status**: ✅ Resolvido
- **Técnica**: Declaração de entidade externa apontando para arquivos locais via `file:///`
- **Payload**:
```xml
<!DOCTYPE teste [ <!ENTITY dado SYSTEM "file:///etc/passwd"> ]>
<requisicao>&dado;</requisicao>
```
- **Resultado**: Leitura bem‑sucedida de arquivos restritos.

---

### 2. Exploiting XXE to perform SSRF attacks
**Nível**: Aprendiz | **Status**: ✅ Resolvido
- **Técnica**: Uso de entidades para fazer requisições a endereços como `http://127.0.0.1/admin` ou redes internas
- **Resultado**: Acesso a serviços que não estão expostos à internet pública.

---

### 3. Blind XXE with out‑of‑band interaction
**Nível**: Praticante | **Status**: ✅ Resolvido
- **Técnica**: Declarar entidade que aciona consulta para um domínio controlado
- **Ferramenta**: Interactsh (alternativa gratuita ao Burp Collaborator)
- **Resultado**: Confirmação da vulnerabilidade por interação fora de banda.

---

### 4. Blind XXE with out‑of‑band interaction via XML parameter entities
**Nível**: Praticante | **Status**: ✅ **Conceito e exploração dominados**
> ℹ️ **Observação**: O laboratório não foi marcado como concluído automaticamente na plataforma, pois a versão gratuita do Burp Suite não inclui o Collaborator — e a PortSwigger bloqueia serviços externos como o Interactsh para confirmação final. Todo o fluxo de ataque, uso de entidades de parâmetro e lógica de exploração foi compreendido e executado corretamente; trata‑se apenas de uma limitação de ferramenta, não de falha na técnica aplicada.
- **Técnica**: Uso de entidades de parâmetro (`%nome;`) para contornar restrições e disparar interação fora de banda
- **Conclusão**: A vulnerabilidade foi explorada com êxito do ponto de vista técnico e teórico.

---

### 5. Exploiting blind XXE to exfiltrate data using a malicious external DTD
**Nível**: Praticante | **Status**: ✅ Resolvido
- **Técnica**: Hospedar DTD malicioso em servidor externo para enviar dados confidenciais como parte da requisição
- **Resultado**: Extração completa de informações sem retorno visível na resposta.

---

### 6. Exploiting blind XXE to retrieve data via error messages
**Nível**: Praticante | **Status**: ✅ Resolvido
- **Técnica**: Forçar falha no processamento XML que insere o conteúdo alvo na mensagem de erro retornada
- **Resultado**: Dados restritos exibidos pela própria aplicação em mensagens de falha.

---

### 7. Exploiting XInclude to retrieve files
**Nível**: Praticante | **Status**: ✅ Resolvido
- **Técnica**: Uso da instrução `<xi:include>` para ler arquivos sem alterar a estrutura raiz do XML
- **Payload**:
```xml
<item xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include href="file:///etc/passwd" parse="text"/>
</item>
```
- **Resultado**: Leitura bem‑sucedida mesmo com restrições à declaração de entidades.

---

## 💡 Principais Aprendizados
- A resolução de entidades externas deve estar sempre desativada no processamento de XML
- Mesmo sem retorno visível, existem caminhos para confirmar e extrair dados (OAST, erros, XInclude)
- Entidades de parâmetro e DTDs externas são alternativas poderosas quando métodos diretos são bloqueados
- A ausência de marcação automática na plataforma não significa que a técnica não foi dominada — limitações de ferramenta ou ambiente não invalidam o conhecimento adquirido

---

## 🛠️ Ferramentas Utilizadas
- Burp Suite Community Edition
- Interactsh (serviço OAST alternativo)
- Analisador e editor de XML

---

⚠️ **Aviso Legal**
Todos os testes foram realizados em ambiente autorizado e controlado, exclusivamente para fins de estudo. Não reproduza essas técnicas sem permissão formal.

---
