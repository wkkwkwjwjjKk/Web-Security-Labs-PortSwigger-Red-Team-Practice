# Lab: User Role Can Be Modified in User Profile

## Objetivo

Explorar uma vulnerabilidade de controle de acesso onde o papel (role) do usuário pode ser modificado diretamente através do perfil.

---

## Análise

Durante a análise da funcionalidade de perfil do usuário, foi identificado que o campo de “role” estava exposto e podia ser alterado diretamente na requisição.

A aplicação não realizava validação adequada para impedir a modificação de privilégios.

---

## Exploração

Ao interceptar a requisição de atualização do perfil, foi possível modificar o valor do campo de role para um nível de privilégio superior.

Após a alteração, o usuário passou a ter acesso a funcionalidades restritas de administrador.

---

## Impacto

Essa vulnerabilidade pode permitir:

* elevação de privilégio (Privilege Escalation)
* acesso a funcionalidades administrativas
* manipulação de dados sensíveis
* comprometimento total da aplicação dependendo do nível de acesso obtido

---

## Mitigação

* não permitir que o usuário controle campos de privilégio
* validar alterações de perfil no backend
* implementar controle de acesso baseado em papéis (RBAC)
* tratar campos sensíveis como “server-side only”

---

## Aprendizado

Este laboratório demonstra como a exposição e manipulação de campos sensíveis em requisições pode levar à elevação de privilégio e comprometimento da aplicação.
