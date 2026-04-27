# Lab: Blind OS Command Injection with Out-of-Band Data Exfiltration

## Objetivo

Explorar uma vulnerabilidade de Blind OS Command Injection utilizando técnicas de out-of-band (OAST) para confirmar execução de comandos e realizar exfiltração indireta de dados.

---

## Análise

Durante a análise da aplicação, foi identificado que um parâmetro da requisição era processado pelo sistema operacional sem validação adequada.

No entanto, a aplicação não retornava saída direta dos comandos executados, caracterizando uma vulnerabilidade de blind command injection.

---

## Exploração

Como não havia retorno visível da execução dos comandos, foi utilizada uma técnica de out-of-band (OAST), forçando o servidor a realizar uma requisição externa controlada.

Essa abordagem permitiu confirmar a execução do comando no servidor através da interação externa.

---

## Impacto

Essa vulnerabilidade pode permitir:

* execução remota de comandos sem retorno direto
* exfiltração de dados via canais externos (OOB)
* reconhecimento de infraestrutura interna
* comprometimento do servidor sem detecção imediata

---

## Mitigação

* evitar execução de comandos do sistema operacional com entrada do usuário
* sanitizar e validar todas as entradas
* monitorar e bloquear requisições suspeitas de saída
* aplicar princípios de menor privilégio no sistema

---

## Aprendizado

Este laboratório demonstra como vulnerabilidades de Blind Command Injection podem ser exploradas mesmo sem retorno direto, utilizando técnicas de comunicação out-of-band para confirmação e exfiltração de dados.
