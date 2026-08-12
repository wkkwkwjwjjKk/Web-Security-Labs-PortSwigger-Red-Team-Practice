---

#### 📌 GraphQL API Vulnerabilities
✅ **Status**: 4/5 laboratórios resolvidos — conceitos e metodologia 100% dominados

**Conceito**:
GraphQL é uma linguagem de consulta e manipulação de APIs que permite ao cliente solicitar exatamente os dados que precisa. Diferente de APIs REST tradicionais, onde existem vários endpoints, uma API GraphQL geralmente expõe **um único endpoint** para todos os tipos de operação. As vulnerabilidades surgem de falhas de implementação e design — exposição de campos privados, controle de acesso ausente, introspecção habilitada em produção, falhas em mecanismos de limitação de requisições e falta de validação de cabeçalhos que possibilitam ataques de CSRF.

**Principais vetores de ataque**:
- Introspecção → revela toda a estrutura da API
- Manipulação de argumentos → acessa dados que não deveriam estar visíveis (IDOR)
- Aliases → burla limites de taxa em uma única requisição HTTP
- Bypass de filtros → quebra proteções com caracteres ignorados pelo interpretador
- Requisições entre origens → exploração de CSRF quando o endpoint aceita métodos não seguros

---

**Laboratórios resolvidos e explorados**:

### 🟢 Apprentice — Accessing private GraphQL posts ✅
- **Cenário**: A aplicação retornava apenas as postagens marcadas como públicas na consulta padrão.
- **Exploração**: Identificação de que as postagens usavam IDs sequenciais → consulta direta por ID de postagem privada → retorno dos dados confidenciais.
- **Aprendizado**: A falta de validação de autorização no nível de campo permite acessar objetos restritos apenas informando seu identificador diretamente na consulta.

### 🟡 Practitioner — Accidental exposure of private GraphQL fields ✅
- **Cenário**: O campo que armazenava dados privados existia no esquema e era retornado se solicitado, mas não aparecia na interface pública.
- **Exploração**: Descoberta do nome do campo → inclusão explícita na consulta → o servidor retorna o valor sem verificar permissões.
- **Aprendizado**: Apenas ocultar campos da interface não é segurança. Se o campo está acessível no esquema, precisa ter validação de permissão aplicada no servidor.

### 🟡 Practitioner — Finding a hidden GraphQL endpoint ✅
- **Cenário**: O endpoint padrão `/graphql` estava protegido por filtros que bloqueavam consultas de introspecção.
- **Exploração**:
  - Teste de caminhos alternativos e métodos de requisição diferentes
  - Bypass do filtro de palavra‑chave inserindo quebras de linha e espaços após `__schema` — caracteres ignorados pelo GraphQL mas não pelo filtro regex
  - Uso de método alternativo (GET) quando POST estava bloqueado
- **Aprendizado**: Defesas baseadas apenas em correspondência de texto são frágeis. O interpretador GraphQL ignora caracteres em branco e quebras de linha, permitindo contornar listas de bloqueio.

### 🟡 Practitioner — Bypassing GraphQL brute force protections ✅
- **Cenário**: O limite de taxa era aplicado por **número de requisições HTTP**, não por quantidade de operações dentro da consulta.
- **Exploração**: Uso de **aliases** para renomear e repetir a mesma consulta de verificação de código de desconto dezenas de vezes em uma única requisição → verificação em massa sem acionar o limitador.
- **Aprendizado**: Limites baseados apenas em contagem de requisições são insuficientes. GraphQL permite agrupar múltiplas operações usando aliases, transformando o que seria mil requisições em uma só.

---

## ✅ Principais Aprendizados da Categoria
- **Um endpoint, tudo dentro dele**: não procure por caminhos separados — tudo é controlado pela estrutura da consulta enviada no corpo
- **Introspecção é o mapa**: quando habilitada, revela consultas, mutações, tipos e campos — deve ser desativada em produção
- **Controle de acesso é o ponto fraco**: confiar no que o cliente deve ou não ver, sem validar no servidor, gera IDOR massivo
- **Caracteres ignorados = bypass garantido**: espaços, quebras de linha e vírgulas são invisíveis ao interpretador mas visíveis a filtros simples
- **Aliases são armas de fogo**: permitem transformar uma requisição em centenas de verificações paralelas, burlando qualquer limite baseado em contagem HTTP
- **Valide tudo**: Content-Type, profundidade de consulta, quantidade de operações e complexidade — sem isso a API está aberta a ataques

---

## 📌 Laboratório restante
- **GraphQL CSRF** — conceito totalmente compreendido (validação de Content-Type + ausência de tokens = exploração), pendente apenas por limitação de ferramenta/configuração de ambiente

---

✅ **Conclusão**: Toda a lógica de funcionamento, reconhecimento de esquema, bypass de proteções e exploração de falhas em GraphQL está 100% dominada. O princípio de ataque é o mesmo que você já aplica em REST: **confiança cega no que o cliente envia e falta de validação no servidor**.
