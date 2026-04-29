# Content-Type Restriction Bypass

## Objetivo

Explorar uma vulnerabilidade de bypass de validação baseada apenas no header `Content-Type`, permitindo o upload de uma Web Shell e execução remota de comandos (RCE).

---

## Análise

A aplicação realizava validação de arquivos de upload com base exclusivamente no header `Content-Type`.

Não havia verificação do conteúdo real do arquivo, extensão ou outros mecanismos de validação mais robustos.

---

## Exploração

Foi identificado que ao modificar o valor do header `Content-Type`, era possível contornar a validação da aplicação.

Com isso, uma Web Shell foi enviada com sucesso e posteriormente acessada via navegador, permitindo execução de comandos no servidor.

---

## Impacto

Essa vulnerabilidade pode permitir:

* execução remota de comandos (RCE)
* upload de arquivos maliciosos
* comprometimento total do servidor
* acesso não autorizado a dados sensíveis

---

## Mitigação

* não confiar apenas no header `Content-Type`
* validar tipo real do arquivo (magic bytes)
* usar whitelist de extensões permitidas
* armazenar uploads fora do diretório web
* impedir execução de arquivos enviados

---

## Aprendizado

Este laboratório demonstrou como validações baseadas apenas em headers HTTP podem ser facilmente contornadas, levando a falhas críticas de segurança em mecanismos de upload.
