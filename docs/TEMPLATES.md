# 📝 Template Padrão para Write-ups

Use este template para documentar todos os laboratórios de forma consistente.

---

## 🔐 [NOME DO LAB] – PortSwigger Web Security Academy

### 📌 Informações Gerais
- **Plataforma**: PortSwigger Web Security Academy
- **Categoria**: [Nome da Categoria]
- **Nível de Dificuldade**: Apprentice / Practitioner / Expert
- **Status**: ✅ Resolvido
- **Data**: [Mês/Ano]
- **Ferramentas**: Burp Suite, [outras ferramentas]

---

## 🎯 Objetivo do Laboratório

[Uma frase descrevendo o que é preciso conseguir]

**Exemplo**: "Explorar uma falha na validação de token CSRF para alterar o e-mail de outro usuário."

---

## 🔍 Resumo Executivo (30 segundos)

[3-4 linhas resumindo: qual a falha, como explorar, qual o impacto]

**Exemplo**: "Este lab explora a falta de validação do parâmetro `state` em OAuth. O estado não é ligado à sessão do usuário, permitindo fixar seu valor e forçar a vinculação com contas de outras pessoas via CSRF."

---

## 📚 Conceitos Teóricos

### O que é [Vulnerabilidade]?

[Explicação técnica clara do problema]

### Por que acontece?

[Causa raiz: má implementação, lógica errada, etc.]

### Qual é o impacto?

- [Impacto 1]
- [Impacto 2]
- [Impacto 3]

### Referências Técnicas

- **OWASP**: [Link - ex: OWASP CSRF](https://owasp.org/www-community/attacks/csrf)
- **CWE**: [CWE-352 - Cross-Site Request Forgery (CSRF)](https://cwe.mitre.org/data/definitions/352.html)
- **RFC**: [RFC 6265 - HTTP State Management Mechanism](https://datatracker.ietf.org/doc/html/rfc6265) (se aplicável)
- **CVE**: [CVE-YYYY-XXXXX](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-YYYY-XXXXX) (se houver histórico)

---

## 🧪 Exploração Passo a Passo

### Passo 1: Reconhecimento

[O que observar, capturar, analisar]

**Requisição interceptada:**
```http
GET /endpoint HTTP/1.1
Host: lab-id.web-security-academy.net
Cookie: session=...
```

**Resultado observado**: [O que você vê na resposta]

---

### Passo 2: Identificação da Falha

[Como você confirma a vulnerabilidade]

**Payload de teste**:
```
[payload específico]
```

**Resposta recebida**:
```
[resposta que comprova a falha]
```

**Conclusão**: [Por que isso confirma a vulnerabilidade]

---

### Passo 3: Desenvolvimento do Exploit

[Como criar a exploração real]

**Payload final**:
```html
[código do exploit completo]
```

**Explicação linha por linha**: 
- Linha 1: [o que faz]
- Linha 2: [o que faz]
- [...]

---

### Passo 4: Validação

[Como confirmar que funcionou]

**Resultado final**: [O que você conseguiu (admin access, dados extraídos, etc)]

---

## 💥 Impacto Técnico

| Aspecto | Risco | Justificativa |
|--------|-------|---------------|
| **Confidencialidade** | Alto / Médio / Baixo | [Por quê pode vazar dados] |
| **Integridade** | Alto / Médio / Baixo | [Por quê pode modificar dados] |
| **Disponibilidade** | Alto / Médio / Baixo | [Por quê pode derrubar serviço] |
| **Privilégios Necessários** | Nenhum / Usuário autenticado / Admin | [Quem consegue explorar] |
| **Tipo de Ataque** | Ativo / Passivo | [Como é executado] |

---

## 🛡️ Mitigação & Defesa

### ❌ Implementação Vulnerável

```php
// ERRADO - não valida CSRF token
if ($method === 'POST') {
    updateEmail($_POST['email']);
}
```

**Problema**: [Por que é inseguro]

---

### ✅ Implementação Segura

```php
// CORRETO - valida CSRF token E método
if ($method === 'POST') {
    validateCSRFToken($_POST['csrf']);
    validateRequestOrigin($_SERVER['HTTP_ORIGIN']);
    updateEmail($_POST['email']);
}
```

**Melhoria**: [Por que agora é seguro]

---

### Princípios de Defesa (checklist)

- [ ] [Princípio 1 - ex: Sempre usar CSRF tokens únicos por sessão]
- [ ] [Princípio 2 - ex: Validar Origin e Referer headers]
- [ ] [Princípio 3 - ex: Usar SameSite cookie attribute]
- [ ] [Princípio 4]

---

## 🎓 Lições Aprendidas

### Insight 1
[Conhecimento prático adquirido]

### Insight 2
[Conexão com outro tipo de ataque]

### Insight 3
[Mentalidade de pentester - como aplicar em outros contextos]

### Aplicação em Bug Bounty
[Como usar isso em cenários reais de teste]

---

## 🔗 Referências Completas

- [PortSwigger Academy - Tema](https://portswigger.net/web-security/[topic])
- [OWASP Top 10 - Categoria](https://owasp.org/Top10/)
- [RFC XXXX - Especificação](https://datatracker.ietf.org/doc/html/rfc[número])
- [CWE-XXX - Descrição](https://cwe.mitre.org/data/definitions/[número].html)
- [Artigo de Pesquisa - Título](https://link-para-artigo)
- [Blog/Writeup - Título](https://link-para-writeup)

---

## 📎 Anexos (Opcional)

### Screenshots Capturados

[Se houver imagens importantes demonstrando a exploração]

### Scripts Auxiliares

[Link ou código de ferramentas criadas para automatizar a exploração]

### Wordlists Usadas

[Se houver, liste qual e onde foi obtida]

### Ferramentas Externas

[Burp extensões, scripts Python, etc]

---

## ⏱️ Tempo Total

- **Reconhecimento**: X min
- **Análise**: X min
- **Exploração**: X min
- **Validação**: X min
- **Documentação**: X min
- **Total**: XX min

---

## 📊 Checklist de Qualidade

- [ ] Título claro e descritivo
- [ ] Resumo executivo conciso (<100 palavras)
- [ ] Conceitos teóricos explicados para iniciantes
- [ ] Payload e código comentado
- [ ] Passo a passo é reproduzível
- [ ] Referências técnicas incluídas
- [ ] Mitigação com código de exemplo
- [ ] Impacto claramente comunicado
- [ ] Lições aprendidas relevantes

---

**Autor**: [Seu Nome]  
**Data de Resolução**: [DD/MM/YYYY]  
**Status**: ✅ Documentado  
**Qualidade**: [★★★★★]
