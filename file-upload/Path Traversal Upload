# Path Traversal Upload

## Objetivo

Explorar uma vulnerabilidade de upload de arquivos combinada com Path Traversal para armazenar uma Web Shell em diretório acessível e obter execução remota de comandos (RCE).

---

## Análise

A aplicação permitia controle parcial do caminho de salvamento dos arquivos enviados.

Não havia validação adequada para impedir manipulação do diretório de destino.

---

## Exploração

Foi explorada a técnica de Path Traversal durante o upload do arquivo, permitindo alterar o diretório de destino.

Com isso, a Web Shell foi armazenada em um diretório acessível via navegador, possibilitando a execução de comandos no servidor.

---

## Impacto

Essa vulnerabilidade pode permitir:

* execução remota de comandos (RCE)
* escrita de arquivos em diretórios sensíveis
* comprometimento total do servidor
* exposição de dados e recursos internos

---

## Mitigação

* normalização e validação do caminho de upload
* bloqueio de sequências como `../`
* armazenamento de arquivos fora do diretório web
* uso de nomes de arquivo gerados pelo servidor
* controle rígido de permissões de escrita

---

## Aprendizado

Este laboratório demonstrou como a combinação de upload de arquivos com Path Traversal pode resultar em comprometimento total do servidor através de execução remota de comandos.
