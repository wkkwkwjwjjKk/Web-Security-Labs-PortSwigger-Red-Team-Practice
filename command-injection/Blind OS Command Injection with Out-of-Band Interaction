# Lab: Blind OS Command Injection with Out-of-Band Interaction

## Objetivo

Explorar uma vulnerabilidade de Blind OS Command Injection utilizando interação out-of-band (OAST) para confirmar a execução de comandos no servidor.

---

## Análise

Durante a análise da aplicação, foi identificado que um parâmetro da requisição era processado pelo sistema operacional sem validação adequada.

A aplicação não retornava saída direta dos comandos executados, caracterizando um cenário de Blind Command Injection.

---

## Exploração

Foi utilizada uma técnica de out-of-band interaction, forçando o servidor a iniciar uma conexão externa controlada.

Essa interação permitiu confirmar que o comando foi executado no servidor, mesmo sem retorno visível na resposta da aplicação.

---

## Impacto

Essa vulnerabilidade pode permitir:

* execução remota de comandos sem retorno direto
* confirmação de execução via interação externa
* reconhecimento de infraestrutura interna
* exploração discreta e difícil de detectar

---

## Mitigação

* evitar execução de comandos do sistema operacional com entradas controladas pelo usuário
* validar e sanitizar todas as entradas
* restringir ou monitorar tráfego de saída (egress filtering)
* aplicar princípio do menor privilégio no sistema

---

## Aprendizado

Este laboratório demonstra como técnicas de interação out-of-band permitem confirmar e explorar vulnerabilidades de Blind OS Command Injection mesmo sem resposta direta da aplicação.
