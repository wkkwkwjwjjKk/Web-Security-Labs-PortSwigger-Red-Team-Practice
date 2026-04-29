# Lab: User ID Controlled by Request Parameter with Data Leakage in Redirect

## Objetivo

Explorar uma vulnerabilidade de controle de acesso onde o ID do usuário é controlado por parâmetro da requisição, resultando em vazamento de dados sensíveis durante redirecionamentos.

---

## Análise

Durante a análise da aplicação, foi identificado que o redirecionamento de usuários era baseado em um parâmetro `userId` enviado na requisição.

Não havia validação no backend para garantir que o usuário autenticado tinha permissão para acessar ou ser redirecionado para os dados associados a esse identificador.

---

## Exploração

Ao manipular o parâmetro `userId` na requisição, foi possível alterar o destino do redirecionamento e acessar dados pertencentes a outros usuários.

Durante esse processo, ocorreu vazamento de informações sensíveis na resposta ou no destino do redirecionamento.

---

## Impacto

Essa vulnerabilidade pode permitir:

* acesso não autorizado a dados de outros usuários
* vazamento de informações sensíveis durante redirecionamentos
* manipulação indevida de fluxos de navegação
* comprometimento da confidencialidade dos dados

---

## Mitigação

* validar autorização antes de realizar redirecionamentos
* não utilizar parâmetros de requisição para controle de acesso
* aplicar controle de acesso no backend para cada recurso
* evitar exposição de dados sensíveis em redirecionamentos

---

## Aprendizado

Este laboratório demonstra como o controle inadequado de parâmetros usados em redirecionamentos pode resultar em vazamento de dados sensíveis e bypass de controle de acesso.
