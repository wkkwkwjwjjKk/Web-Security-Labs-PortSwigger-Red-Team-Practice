# Blind OS Command Injection with Output Redirection

## Objetivo

Explorar uma vulnerabilidade de Blind Command Injection utilizando redirecionamento de saída para confirmar a execução de comandos no servidor.

---

## Análise

A aplicação não retornava a saída direta dos comandos executados, dificultando a validação da vulnerabilidade.

No entanto, foi identificado que o parâmetro vulnerável permitia a execução de comandos no sistema operacional.

---

## Exploração

Como a aplicação não exibia o resultado dos comandos, foi utilizado redirecionamento de saída para gravar o resultado em um arquivo acessível pela aplicação.

Após a execução, foi possível acessar o arquivo via navegador e confirmar que o comando havia sido executado no servidor.

---

## Impacto

Essa vulnerabilidade pode permitir execução remota de comandos sem retorno direto, podendo ser explorada para:

* execução arbitrária de comandos
* exfiltração de dados via arquivos
* reconhecimento do sistema
* comprometimento do servidor

---

## Mitigação

* validação e sanitização de entradas
* evitar execução de comandos via shell
* desabilitar escrita em diretórios acessíveis via web
* uso de APIs seguras para execução de processos

---

## Aprendizado

Este laboratório demonstrou técnicas de exploração de Blind Command Injection, onde a ausência de resposta direta não impede a confirmação da execução de comandos.
