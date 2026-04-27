# Command Injection - Delay

## Objetivo

Explorar uma vulnerabilidade de Command Injection no parâmetro `email`, utilizando técnicas de delay para confirmar a execução de comandos no servidor.

---

## Análise

Durante os testes, foi observado que o parâmetro `email` era processado diretamente pela aplicação sem validação adequada.

Isso indicava possível execução de comandos no sistema operacional a partir da entrada do usuário.

---

## Exploração

Foram inseridos comandos com técnicas de delay no parâmetro `email`.

Após a injeção, foi observado aumento no tempo de resposta da aplicação, indicando que os comandos foram executados no servidor.

---

## Impacto

Esse tipo de vulnerabilidade pode permitir execução remota de comandos, possibilitando:

* reconhecimento do sistema
* execução de comandos arbitrários
* comprometimento do servidor

---

## Mitigação

* validação e sanitização de entradas
* evitar execução de comandos via shell
* uso de funções seguras da linguagem
* princípio do menor privilégio

---

## Aprendizado

Este laboratório demonstrou como técnicas de time-based detection podem ser utilizadas para identificar Command Injection mesmo quando não há retorno direto da execução.

