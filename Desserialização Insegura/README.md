
---

#### 📌 Desserialização Insegura
✅ **Status**: 10/10 laboratórios resolvidos — 100% concluído

**Conceito**:
A desserialização é o processo de reconstruir objetos de programa a partir de dados que foram enviados pela rede ou armazenados. Quando a aplicação confia cegamente em dados serializados enviados pelo usuário e os reconstrói sem validação, o atacante pode **modificar o objeto, alterar lógica de permissões ou injetar estruturas maliciosas**, chegando até a execução remota de comandos.

A vulnerabilidade existe porque o servidor trata os dados serializados como confiáveis — aceita qualquer estrutura que ele consiga reconstruir, sem perguntar se o usuário tinha permissão para alterá-la.

---

**Laboratórios resolvidos e explorados**:

### 🟢 Apprentice — Modifying serialized objects ✅
- **Cenário**: A aplicação armazena dados do usuário em um objeto PHP serializado dentro do cookie de sessão, codificado em Base64 e URL.
- **Exploração**: Decodificação do cookie → alteração do atributo `admin` de `b:0` (falso) para `b:1` (verdadeiro) → recodificação e substituição no cookie → acesso ao painel administrativo → exclusão do usuário alvo.
- **Aprendizado básico**: Dados serializados confiáveis pelo cliente permitem alteração direta de permissões e regras de negócio.

### 🟡 Practitioner — Modifying serialized data types ✅
- **Cenário**: A validação de acesso comparava um valor de entrada com um valor do objeto serializado usando comparação fraca (`==` em PHP), que ignora tipos de dados.
- **Exploração**: Alteração do tipo de dado de string para inteiro no objeto serializado, fazendo com que a comparação retornasse "verdadeiro" mesmo com valores diferentes.
- **Aprendizado**: A lógica de comparação pode ser enganada manipulando não só o valor, mas o **tipo de dado** dentro do objeto.

### 🟡 Practitioner — Using application functionality to exploit insecure deserialization ✅
- **Cenário**: Não havia uma "função de ataque" direta, mas a aplicação possuía métodos que podiam ser invocados ao desserializar um objeto manipulado.
- **Exploração**: Injeta-se um objeto que, ao ser reconstruído, aciona métodos já existentes na própria aplicação que causam impacto — exclusão de arquivos, limpeza de diretórios, etc.
- **Aprendizado**: Nem sempre é preciso injetar código novo; muitas vezes basta "apontar" a desserialização para funções que a aplicação já possui.

### 🟡 Practitioner — Arbitrary object injection in PHP ✅
- **Cenário**: A aplicação aceita objetos de qualquer classe ao desserializar, sem restrição. O código-fonte dispõe de classes "de ajuda" que realizam ações perigosas.
- **Exploração**: Criação e injeção de um objeto de classe diferente da original, que ao ser desserializado executa ações predefinidas pelo desenvolvedor.
- **Aprendizado**: Desserialização sem lista branca de classes permite injetar objetos arbitrários e desencadear fluxos de código não previstos.

### 🟡 Practitioner — Exploiting Java deserialization with Apache Commons ✅
- **Cenário**: Aplicação em Java que desserializa dados de usuários, com a biblioteca `Apache Commons Collections` presente no servidor.
- **Exploração**: Uso de "cadeias de artefatos" (gadget chains) conhecidas — objetos que, ao serem reconstruídos, encadeiam chamadas de métodos até chegar à execução arbitrária de comandos do sistema.
- **Aprendizado**: Bibliotecas populares podem conter sequências de código que, quando acionadas por desserialização, levam diretamente a RCE.

### 🟡 Practitioner — Exploiting PHP deserialization with a pre-built gadget chain ✅
- **Cenário**: Aplicação PHP com um conjunto de classes e métodos que formam uma cadeia de exploração conhecida.
- **Exploração**: Uso de ferramentas (como o `PHPGGC`) para gerar o objeto serializado malicioso pronto, que dispara comandos do sistema ao ser desserializado.
- **Aprendizado**: Cadeias de artefatos já conhecidas podem ser reutilizadas — o trabalho resume-se a identificar bibliotecas/frameworks presentes e gerar o payload correspondente.

### 🟡 Practitioner — Exploiting Ruby deserialization using a documented gadget chain ✅
- **Cenário**: Aplicação em Ruby que desserializa dados enviados pelo usuário via `Marshal.load`.
- **Exploração**: Identificação de padrões conhecidos na documentação e bibliotecas do ecossistema Ruby → construção do objeto que executa comandos ao ser reconstruído.
- **Aprendizado**: Cada linguagem tem seus padrões e vetores de desserialização — mas o princípio de exploração é o mesmo.

### 🔴 Expert — Developing a custom gadget chain for Java deserialization ✅
- **Cenário**: Sem bibliotecas conhecidas e sem ferramentas prontas — é preciso analisar o código-fonte fornecido e montar a cadeia de exploração do zero.
- **Exploração**: Estudo da ordem de execução de métodos → identificação de ponto de entrada na desserialização → encadeamento de chamadas até alcançar execução de comandos.
- **Aprendizado**: Quando não há payloads prontos, a desserialização explora o fluxo normal do código — basta saber conectar os métodos na ordem certa.

### 🔴 Expert — Developing a custom gadget chain for PHP deserialization ✅
- **Cenário**: Código-fonte fornecido com classes e métodos aparentemente inofensivos; sem cadeias conhecidas.
- **Exploração**: Análise de magia do PHP (`__destruct`, `__toString`, `__call`) → descobrindo como um objeto pode invocar outro e assim por diante, formando uma cadeia que termina em execução de comando.
- **Aprendizado**: Os métodos mágicos são o ponto de partida da desserialização — eles são executados automaticamente pelo sistema sem que o desenvolvedor precise chamá-los explicitamente.

### 🔴 Expert — Using PHAR deserialization to deploy a custom gadget chain ✅
- **Cenário**: A desserialização direta está bloqueada, mas a aplicação lê arquivos enviados pelo usuário e permite acesso a arquivos no formato `.phar`.
- **Exploração**: Criação de um arquivo PHAR malicioso cujos metadados contêm o objeto serializado preparado → quando a aplicação lê o arquivo com funções como `file_exists` ou `getimagesize`, o PHP desserializa automaticamente o conteúdo e dispara a cadeia.
- **Aprendizado**: Desserialização não ocorre só em cookies e parâmetros — formatos de arquivo como PHAR desserializam automaticamente ao serem lidos, abrindo um vetor alternativo de ataque.

---

## ✅ Principais Aprendizados da Categoria
- **Confiança cega é o problema raiz**: o servidor reconstrói objetos sem validar quem criou ou alterou
- **A exploração evolui em níveis**: de simples troca de valor (`b:0` → `b:1`) até montar cadeias inteiras de métodos a partir de código-fonte
- **Não é preciso injetar código novo**: na maioria das vezes, a desserialização apenas "conecta" funções que já existem na aplicação
- **Bibliotecas e formatos de arquivo podem esconder vetores inteiros**: PHAR, Apache Commons, Marshal — todos desserializam dados automaticamente
- **O princípio é o mesmo em qualquer linguagem**: identificar o ponto de entrada → manipular o objeto → aproveitar o fluxo de métodos para alcançar impacto

---

✅ **Conclusão**: Categoria 100% dominada — desde a alteração de um atributo até o desenvolvimento de cadeias de exploração totalmente personalizadas, sem ferramentas prontas.

---
