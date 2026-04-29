# Lab: User ID Controlled by Request Parameter with Unpredictable User IDs

## Objetivo

Explorar uma vulnerabilidade de controle de acesso onde o ID do usuário é controlado por parâmetro da requisição, mesmo quando os identificadores são não previsíveis, resultando em acesso não autorizado a dados de outros usuários.

---

## Análise

Durante a análise da aplicação, foi identificado que o perfil do usuário era carregado com base em um identificador (`userId`) enviado na requisição.

Embora os IDs não fossem sequenciais ou previsíveis, não havia validação no backend para verificar se o usuário autenticado tinha permissão para acessar o recurso correspondente.

---

## Exploração

Ao interceptar a requisição e substituir o valor do `userId` por identificadores válidos obtidos por outros meios da aplicação, foi possível acessar dados de outros usuários.

Isso confirmou que a segurança não dependia apenas da imprevisibilidade do ID, mas da ausência de controle de autorização.

---

## Impacto

Essa vulnerabilidade pode permitir:

* acesso não autorizado a dados de outros usuários
* vazamento de informações sensíveis
* bypass de controles baseados em IDs não previsíveis
* comprometimento da confidencialidade dos dados

---

## Mitigação

* validar autorização no backend para cada requisição
* não confiar na imprevisibilidade de IDs como mecanismo de segurança
* implementar controle de acesso baseado em identidade (RBAC)
* garantir verificação de permissão para cada recurso acessado

---

## Aprendizado

Este laboratório demonstra que a segurança não deve depender da imprevisibilidade de identificadores, mas sim de controles de acesso robustos e verificados no servidor.
