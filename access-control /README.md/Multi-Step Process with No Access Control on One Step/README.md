# Lab: Multi-Step Process with No Access Control on One Step

## Objetivo

Explorar uma vulnerabilidade de controle de acesso em um processo multi-etapas, onde uma das etapas não possui verificação de autorização adequada.

---

## Análise

Durante a análise da funcionalidade, foi identificado que o fluxo da aplicação era composto por múltiplas etapas sequenciais.

No entanto, uma das etapas críticas não realizava verificação de permissões no backend, permitindo acesso indevido.

---

## Exploração

Ao interagir diretamente com a etapa vulnerável do processo, foi possível contorná-la sem passar pelas validações esperadas.

Isso permitiu executar ações restritas sem possuir os privilégios necessários para aquela etapa específica.

---

## Impacto

Essa vulnerabilidade pode permitir:

* bypass de controles de autorização em fluxos críticos
* execução de ações não autorizadas
* manipulação indevida de processos multi-etapas
* comprometimento da lógica de negócio da aplicação

---

## Mitigação

* validar permissões em todas as etapas do processo
* não assumir segurança baseada em fluxo sequencial
* aplicar controle de acesso no backend para cada ação
* evitar dependência de estado da aplicação para autorização

---

## Aprendizado

Este laboratório demonstra que processos multi-etapas podem ser vulneráveis quando a autorização não é aplicada consistentemente em todas as fases.
