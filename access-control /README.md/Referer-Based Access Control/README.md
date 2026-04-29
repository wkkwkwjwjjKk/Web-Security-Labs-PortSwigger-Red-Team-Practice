# Lab: Referer-Based Access Control

## Objetivo

Explorar uma vulnerabilidade de controle de acesso baseada no header `Referer`, permitindo bypass de restrições de acesso a funcionalidades protegidas.

---

## Análise

Durante a análise da aplicação, foi identificado que o controle de acesso a determinadas funcionalidades era baseado no header HTTP `Referer`.

A aplicação utilizava esse valor para determinar se o usuário poderia acessar determinados recursos, sem validação adicional no backend.

---

## Exploração

Ao manipular ou reproduzir o header `Referer`, foi possível contornar a verificação de acesso e acessar funcionalidades restritas.

Isso demonstrou que a autorização estava sendo feita com base em um dado controlado pelo cliente.

---

## Impacto

Essa vulnerabilidade pode permitir:

* bypass de controle de acesso
* acesso não autorizado a funcionalidades restritas
* manipulação de fluxos de navegação protegidos
* comprometimento da lógica de autorização da aplicação

---

## Mitigação

* nunca utilizar o header `Referer` como mecanismo de controle de acesso
* validar permissões no backend para cada requisição
* implementar controle de acesso baseado em identidade (RBAC)
* evitar dependência de headers controlados pelo cliente

---

## Aprendizado

Este laboratório demonstra que headers HTTP como `Referer` não devem ser utilizados para decisões de segurança, pois podem ser facilmente manipulados pelo cliente.
