# Extension Blacklist Bypass

## Objetivo

Explorar uma vulnerabilidade de upload de arquivos baseada em blacklist de extensões, com o objetivo de contornar a validação e obter execução remota de comandos (RCE) através de uma Web Shell.

---

## Análise

A aplicação realizava validação de arquivos baseada apenas em uma lista negra de extensões proibidas.

Esse tipo de abordagem é frágil, pois não considera variações de extensão ou técnicas de ofuscação.

---

## Exploração

Foi realizada a manipulação da extensão do arquivo enviado, permitindo contornar a blacklist implementada.

Com isso, a Web Shell foi enviada com sucesso e acessada via navegador, possibilitando a execução de comandos no servidor.

---

## Impacto

Essa vulnerabilidade pode permitir:

* execução remota de comandos (RCE)
* upload de arquivos maliciosos
* bypass de mecanismos de segurança
* comprometimento total do servidor

---

## Mitigação

* evitar uso exclusivo de blacklist
* implementar whitelist de extensões permitidas
* validar tipo real do arquivo (MIME + magic bytes)
* armazenar uploads fora do diretório web
* impedir execução de arquivos enviados

---

## Aprendizado

Este laboratório demonstrou como mecanismos de segurança baseados apenas em blacklist podem ser facilmente contornados, resultando em comprometimento do sistema através de upload de Web Shell.
