# Lab: Unprotected Admin Functionality

## Objetivo

Explorar uma vulnerabilidade de controle de acesso (Broken Access Control) em funcionalidades administrativas expostas sem autenticação.

---

## Análise

Durante a análise da aplicação, foi identificada uma funcionalidade administrativa acessível diretamente via URL, sem qualquer tipo de autenticação ou verificação de privilégios.

Isso indica ausência de controle de acesso adequado no backend.

---

## Exploração

Ao acessar diretamente o endpoint administrativo, foi possível utilizar funcionalidades restritas sem necessidade de login como administrador.

Não foi necessário bypass ou manipulação de sessão, pois o recurso estava completamente exposto.

---

## Impacto

Essa vulnerabilidade pode permitir:

* acesso não autorizado a painel administrativo
* execução de ações críticas no sistema
* manipulação ou exclusão de dados sensíveis
* comprometimento total da aplicação, dependendo do nível de privilégio exposto

---

## Mitigação

* proteger endpoints administrativos com autenticação
* implementar controle de acesso baseado em papéis (RBAC)
* validar permissões no backend, não apenas no frontend
* evitar exposição de URLs administrativas previsíveis

---

## Aprendizado

Este laboratório demonstra como a ausência de controle de acesso em funcionalidades administrativas pode levar a comprometimento direto da aplicação sem necessidade de credenciais.
