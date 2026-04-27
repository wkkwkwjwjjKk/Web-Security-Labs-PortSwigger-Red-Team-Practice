# Obfuscated File Extension

## Objetivo

Explorar uma vulnerabilidade de upload de arquivos onde a validação de extensão pode ser contornada por meio de ofuscação, permitindo o envio de uma Web Shell e execução remota de comandos (RCE).

---

## Análise

A aplicação realizava validação do nome do arquivo, porém não aplicava normalização adequada antes da verificação da extensão.

Isso permitia inconsistências no tratamento do nome do arquivo, abrindo espaço para bypass da validação.

---

## Exploração

Foi utilizada uma extensão ofuscada no nome do arquivo enviado, contornando a validação da aplicação.

Com isso, a Web Shell foi enviada com sucesso e acessada via navegador, permitindo execução de comandos no servidor.

---

## Impacto

Essa vulnerabilidade pode permitir:

* execução remota de comandos (RCE)
* bypass de validações de upload
* armazenamento de arquivos maliciosos no servidor
* comprometimento total da aplicação

---

## Mitigação

* normalizar nomes de arquivos antes da validação
* evitar validação apenas por extensão
* utilizar whitelist de extensões permitidas
* armazenar uploads fora do diretório web
* impedir execução de arquivos enviados

---

## Aprendizado

Este laboratório demonstrou como a falta de normalização de entrada em mecanismos de upload pode permitir bypass de validação e resultar em execução remota de comandos no servidor.
