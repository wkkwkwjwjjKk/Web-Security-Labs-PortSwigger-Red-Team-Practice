#!/usr/bin/env python3
"""
🤖 Generate Files Script
Gera arquivos README.md padronizados automaticamente
"""

import os
from pathlib import Path
from datetime import datetime

class Color:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_status(message):
    print(f"{Color.GREEN}✅ {message}{Color.END}")

# Template de README para labs
TEMPLATE_README = '''# 🔐 {title} – PortSwigger Web Security Academy

## 📌 Informações Gerais
- **Plataforma**: PortSwigger Web Security Academy
- **Categoria**: {category}
- **Nível de Dificuldade**: {difficulty}
- **Status**: 🔄 Em Progresso
- **Data**: {date}
- **Ferramentas**: Burp Suite

---

## 🎯 Objetivo do Laboratório

[Descrição do objetivo será adicionada após resolver o lab]

---

## 🔍 Resumo Executivo

[Resumo técnico será adicionado]

---

## 📚 Conceitos Teóricos

### O que é {title}?

[Explicação será adicionada]

### Referências Técnicas

- **OWASP**: [Link]
- **CWE**: [CWE-xxx]
- **RFC**: [RFC xxxx - Se aplicável]
- **PortSwigger**: [{title}](https://portswigger.net/web-security)

---

## 🧪 Exploração Passo a Passo

[Será preenchido após resolução]

---

## 💥 Impacto Técnico

| Aspecto | Risco |
|--------|-------|
| **Confidencialidade** | - |
| **Integridade** | - |
| **Disponibilidade** | - |

---

## 🛡️ Mitigação & Defesa

[Será adicionado]

---

## 🎓 Lições Aprendidas

- [Será adicionado]

---

## 🔗 Referências Completas

- [PortSwigger Academy](https://portswigger.net/web-security)
- [OWASP Top 10](https://owasp.org/Top10/)

---

**Status**: 🔄 Pendente de Resolução
**Última Atualização**: {date}
'''

def generate_readme(title, category, difficulty, output_path):
    """Gera um README.md padronizado"""
    content = TEMPLATE_README.format(
        title=title,
        category=category,
        difficulty=difficulty,
        date=datetime.now().strftime("%B %Y")
    )
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print_status(f"Criado: {output_path}")

def main():
    print(f"\n{Color.BLUE}{'='*70}")
    print(f"🤖 GENERATE FILES: Criando READMEs Padronizados")
    print(f"{'='*70}{Color.END}\n")
    
    # Mapping de labs a criar
    labs = [
        # Command Injection
        {
            "path": "2-Injection/Command-Injection/README.md",
            "title": "Command Injection",
            "category": "OS Command Injection",
            "difficulty": "Practitioner / Expert"
        },
        # File Upload
        {
            "path": "7-File-Upload/File-Upload-Vulnerabilities/README.md",
            "title": "File Upload Vulnerabilities",
            "category": "File Upload",
            "difficulty": "Practitioner / Expert"
        },
        # Access Control
        {
            "path": "3-Access-Control/IDOR/README.md",
            "title": "Access Control & IDOR",
            "category": "Broken Access Control",
            "difficulty": "Apprentice / Practitioner / Expert"
        },
        # XXE
        {
            "path": "2-Injection/XXE-Injection/README.md",
            "title": "XXE Injection",
            "category": "XML External Entity",
            "difficulty": "Practitioner / Expert"
        },
        # SSTI
        {
            "path": "6-Advanced/SSTI/README.md",
            "title": "Server-Side Template Injection",
            "category": "SSTI",
            "difficulty": "Practitioner / Expert"
        },
        # Deserialization
        {
            "path": "6-Advanced/Insecure-Deserialization/README.md",
            "title": "Insecure Deserialization",
            "category": "Deserialization",
            "difficulty": "Expert"
        },
        # Business Logic
        {
            "path": "6-Advanced/Business-Logic-Flaws/README.md",
            "title": "Business Logic Flaws",
            "category": "Business Logic Vulnerabilities",
            "difficulty": "Practitioner / Expert"
        },
        # HTTP Request Smuggling
        {
            "path": "4-Web-Requests/HTTP-Request-Smuggling/README.md",
            "title": "HTTP Request Smuggling",
            "category": "HTTP Request Smuggling",
            "difficulty": "Practitioner / Expert"
        },
    ]
    
    for lab in labs:
        generate_readme(
            title=lab["title"],
            category=lab["category"],
            difficulty=lab["difficulty"],
            output_path=lab["path"]
        )
    
    print(f"\n{Color.GREEN}{'='*70}")
    print(f"✅ READMEs Padronizados Criados!")
    print(f"{'='*70}{Color.END}\n")

if __name__ == "__main__":
    main()