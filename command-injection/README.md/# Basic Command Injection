# Basic Command Injection

## Objetivo

Explorar uma vulnerabilidade de Command Injection no parâmetro `stockId`, permitindo a execução de comandos no sistema operacional do servidor.

---

## Análise

Durante os testes, foi observado que o parâmetro `stockId` era utilizado diretamente em uma operação de consulta no backend.

Não foi identificada validação ou sanitização adequada da entrada, indicando possível vulnerabilidade de execução de comandos.

---

## Exploração

Ao inserir operadores de comando no parâmetro `stockId`, foi possível encadear comandos adicionais ao processo original da aplicação.

Isso resultou na execução de comandos no sistema operacional do servidor, confirmando a presença da vulnerabilidade de Command Injection.

---

## Impacto

Essa vulnerabilidade pode permitir que um atacante execute comandos arbitrários no servidor, levando a:

* comprometimento do sistema
* acesso não autorizado a dados
* possível controle total do servidor

---

## Mitigação

* Sanitização e validação rigorosa de entradas
* Evitar execução direta de comandos do sistema operacional
* Uso de APIs seguras em vez de chamadas de shell
* Princípio do menor privilégio

---

## Aprendizado

Este laboratório demonstrou como a falta de validação em parâmetros simples pode resultar em execução remota de comandos no servidor.
