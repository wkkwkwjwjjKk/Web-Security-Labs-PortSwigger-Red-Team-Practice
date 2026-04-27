# Remote Code Execution via Web Shell Upload

## Objetivo

Explorar uma vulnerabilidade de upload de arquivos para obter execução remota de comandos (RCE) no servidor através de uma Web Shell.

---

## Análise

A aplicação permitia o upload de arquivos sem validação adequada de tipo, conteúdo ou extensão.

Não havia mecanismos eficazes de verificação, o que indicava possibilidade de upload de arquivos maliciosos.

---

## Exploração

Foi realizado o upload de uma Web Shell através do mecanismo de upload da aplicação.

Após o envio, o arquivo foi acessado via navegador, permitindo a execução de comandos no sistema operacional do servidor.

---

## Impacto

Essa vulnerabilidade pode permitir:

* execução remota de comandos (RCE)
* comprometimento total do servidor
* acesso e manipulação de dados sensíveis
* instalação de backdoors

---

## Mitigação

* validação rigorosa de tipo de arquivo
* armazenamento de uploads fora do diretório web
* bloqueio de execução de arquivos enviados
* sanitização de nomes e conteúdo de arquivos
* uso de whitelist de extensões permitidas

---

## Aprendizado

Este laboratório demonstrou como falhas em mecanismos de upload podem levar diretamente à execução remota de comandos no servidor.
