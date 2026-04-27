# Lab: User ID Controlled by Request Parameter with Password Disclosure

## Objetivo

Explorar uma vulnerabilidade de controle de acesso onde o ID do usuário é controlado por parâmetro da requisição, resultando na exposição de informações sensíveis de outros usuários, incluindo credenciais.

---

## Análise

Durante a análise da aplicação, foi identificado que o perfil do usuário era carregado com base em um parâmetro `userId` enviado na requisição.

Não havia validação no backend para garantir que o usuário autenticado possuía permissão para acessar os dados associados a esse identificador.

---

## Exploração

Ao modificar o parâmetro `userId` na requisição, foi possível acessar o perfil de outros usuários.

Em alguns casos, a resposta da aplicação incluía informações sensíveis, como credenciais ou dados equivalentes a senha.

---

## Impacto

Essa vulnerabilidade pode permitir:

* acesso não autorizado a dados de outros usuários
* exposição de credenciais sensíveis
* comprometimento de contas de usuários
* violação de confidencialidade e integridade dos dados

---

## Mitigação

* não confiar em parâmetros da requisição para controle de acesso
* validar autorização no backend para cada recurso acessado
* aplicar controle de acesso baseado na identidade autenticada (RBAC)
* evitar retorno de dados sensíveis como senhas em qualquer resposta

---

## Aprendizado

Este laboratório demonstra como falhas de controle de acesso em parâmetros manipuláveis podem levar a exposição crítica de dados sensíveis e comprometimento de contas de usuários.
