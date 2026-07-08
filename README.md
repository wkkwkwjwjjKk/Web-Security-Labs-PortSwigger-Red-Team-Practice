Perfeito! Vou primeiro **melhorar e unificar seu write-up principal**, organizando tudo o que você já tem — incluindo o **SSRF que resolveu hoje**, o Command Injection que você já domina e mantendo toda a estrutura profissional do seu repositório.

Depois, quando você confirmar, eu passo o plano de estudo alinhado exatamente com o seu nível.

---

# 🔒 Web Security Labs – PortSwigger Red Team Practice

[![Progress](https://img.shields.io/badge/Progress-75%25-brightgreen?style=flat-square)](https://github.com/wkkwkwjwjjKk/Web-Security-Labs-PortSwigger-Red-Team-Practice)
[![Labs](https://img.shields.io/badge/Labs-15%2F20-blue?style=flat-square)](https://github.com/wkkwkwjwjjKk/Web-Security-Labs-PortSwigger-Red-Team-Practice)
[![Status](https://img.shields.io/badge/Status-Active-green?style=flat-square)](https://github.com/wkkwkwjwjjKk/Web-Security-Labs-PortSwigger-Red-Team-Practice)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](./LICENSE)

Documentação completa de **laboratórios práticos** de segurança ofensiva web, com foco em exploração manual, análise de vulnerabilidades e desenvolvimento de raciocínio de ataque.

> **Nível**: Intermediário → Avançado | **Plataforma**: PortSwigger Web Security Academy | **Idioma**: Português (PT-BR)

---

## 📊 Status Geral do Repositório

```
████████████░░░░░░░░░░ 75% Completo (15/20 laboratórios documentados)
```

| Status | Quantidade | Percentual |
|--------|-----------|-----------|
| ✅ **Concluído** | 13 | 65% |
| 🟡 **Em Andamento** | 2 | 10% |
| 🔴 **Não Iniciado** | 5 | 25% |

---

## 🚀 Comece Rápido

### Por Nível de Conhecimento

**🟢 Iniciante**
```
1. Autenticação e controle de acesso
2. SQL Injection básica
3. Conceitos de requisições HTTP
```
**Tempo estimado**: ~4 horas

**🟠 Intermediário**
```
1. Injeções avançadas: SQLi cega, SSRF, Command Injection
2. Manipulação de cabeçalhos e parâmetros
3. Técnicas OAST para detecção sem retorno
```
**Tempo estimado**: ~15 horas

**🔴 Avançado**
```
1. XXE, SSTI e Desserialização
2. Análise de lógica de negócio
3. Exploração de APIs
```
**Tempo estimado**: ~20 horas

---

## 🎓 Categorias e Laboratórios

### 🟢 Autenticação e Controle de Acesso
✅ **Status**: 100% concluído
- Enumeração de usuários
- Bypass de limites de tentativas
- Contornos em fluxo de 2FA
- Vulnerabilidades em OAuth e OpenID Connect
- Escalonamento de privilégios e IDOR

---

### 🟡 Injeção de Código e Comandos

#### 📌 SQL Injection
✅ **Status**: 9/9 laboratórios concluídos
- Injeção simples com `UNION`
- Extração de dados e enumeração de esquemas
- SQLi cega por condição booleana e tempo de resposta
- Bypass de filtros e WAF
- Injeção em formatos XML e JSON

#### 📌 SSRF – Server-Side Request Forgery
🟡 **Status**: 5/7 laboratórios concluídos

**Conceito**: Vulnerabilidade que permite ao atacante fazer com que o servidor da aplicação envie requisições arbitrárias para destinos internos ou externos, acessando recursos que não seriam diretamente visíveis ao usuário.

**Laboratórios resolvidos**:
1. **Basic SSRF against the local server**
   - Manipulação de URL para acessar serviços restritos no próprio servidor (`localhost`)
2. **Basic SSRF against another back-end system**
   - Comunicação com máquinas da rede interna, inacessíveis da internet
3. **SSRF with blacklist-based input filter**
   - Contorno de restrições através de variações na formatação e codificação de endereços
4. **SSRF with filter bypass via open redirection**
   - Combinação com redirecionamento aberto para driblar validações de domínio
5. **Blind SSRF with out-of-band detection** ✅ *Resolvido hoje*
   - Cenário sem retorno de dados visíveis
   - **Técnica utilizada**: Detecção via canal fora de banda (OAST)
   - **Vetor**: Cabeçalho HTTP `Referer`
   - **Ferramenta**: Interactsh (alternativa gratuita ao Burp Collaborator)
   - **Resultado**: Confirmação da vulnerabilidade por meio de consultas DNS e requisições HTTP registradas no servidor de escuta

**Laboratórios em andamento**:
- Blind SSRF with Shellshock exploitation
- SSRF with whitelist-based input filter

#### 📌 Command Injection
✅ **Status**: 100% concluído

**Conceito**: Ocorre quando a aplicação envia entrada do usuário diretamente para o interpretador de comandos do sistema operacional, sem tratamento ou validação adequada, permitindo execução arbitrária de instruções.

**Laboratórios resolvidos**:
1. **Basic Command Injection**
   - Inserção de separadores de comando (`;`, `&`, `|`, `&&`) para encadear instruções
   - Confirmação direta através da saída retornada na resposta
2. **Blind OS Command Injection with Time Delays**
   - Detecção por alteração no tempo de resposta usando o comando `sleep`
3. **Blind OS Command Injection with Out-of-Band Exfiltration**
   - Cenário sem retorno visível
   - **Técnica**: Uso de servidor externo controlado (OAST)
   - **Funcionamento**: O comando injetado força o servidor a fazer uma requisição para um domínio do atacante
   - **Resultado**: A interação recebida confirma a execução, mesmo sem qualquer evidência na tela da aplicação

**Principais aprendizados**:
- Falta de retorno visível não significa ausência de vulnerabilidade
- Técnicas OAST são essenciais para exploração em cenários cegos
- É possível confirmar e até extrair dados sem contato direto com o alvo

---

### 🟢 Manipulação de Requisições e Fluxos
✅ **Status**: 100% concluído
- CSRF básico e com contorno de validações
- Poluição de parâmetros e mass assignment
- Vulnerabilidades em tokens JWT e mecanismos de sessão

---

### 🔴 Tópicos a Iniciar
- **XXE Injection**: Exploração de processamento XML
- **SSTI**: Injeção em mecanismos de template
- **Desserialização Insegura**
- Falhas em lógica de negócio
- Vulnerabilidades em APIs

---

## 🛠️ Ferramentas Utilizadas
- **Burp Suite Community Edition**: Proxy, interceptação e envio de requisições
- **Interactsh**: Serviço OAST gratuito para detecção cega
- **Ferramentas do navegador**: Depurador e análise de rede
- **Utilitários de linha de comando**: `curl`, `nslookup`, `ping`

---

## 📚 Referências
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [OWASP Top 10](https://owasp.org/Top10/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [HackTricks](https://book.hacktricks.xyz/)

---

## ⚠️ Aviso Legal
Todos os testes foram realizados **exclusivamente em ambientes autorizados e controlados**, para fins de estudo e pesquisa em segurança da informação. Não utilize as técnicas descritas em sistemas que você não possua permissão explícita.

---

---
