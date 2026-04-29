# Lab: Insecure Direct Object References (IDOR)

## Objetivo

Explorar uma vulnerabilidade de controle de acesso onde objetos são acessados diretamente por identificadores previsíveis, permitindo acesso não autorizado a recursos de outros usuários.

---

## Análise

Durante a análise da aplicação, foi identificado que recursos como dados de usuários e objetos do sistema eram acessados diretamente por meio de IDs enviados na requisição.

Não havia validação no backend para verificar se o usuário tinha permissão para acessar o objeto solicitado.

---

## Exploração

Ao modificar o identificador do objeto na requisição, foi possível acessar dados pertencentes a outros usuários.

Isso confirmou a ausência de controle de acesso adequado sobre objetos referenciados diretamente.

---

## Impacto

Essa vulnerabilidade pode permitir:

* acesso não autorizado a dados de outros usuários
* vazamento de informações sensíveis
* manipulação de recursos alheios
* comprometimento da privacidade e integridade dos dados

---

## Mitigação

* validar permissões de acesso a cada objeto no backend
* evitar exposição direta de identificadores previsíveis
* implementar controle de acesso baseado em autorização por recurso
* usar identificadores não previsíveis quando apropriado

---

## Aprendizado

Este laboratório demonstra como a falta de verificação de autorização em objetos referenciados diretamente pode levar a vazamento de dados e acesso indevido entre usuários.
