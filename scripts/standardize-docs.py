#!/usr/bin/env python3
"""
🤖 Standardize Docs Script
Aplica template padrão aos documentos existentes
"""

import os
import re
from pathlib import Path

class Color:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    END = '\033[0m'

def print_status(message, status="success"):
    if status == "success":
        print(f"{Color.GREEN}✅ {message}{Color.END}")
    elif status == "info":
        print(f"{Color.BLUE}ℹ️  {message}{Color.END}")
    elif status == "warning":
        print(f"{Color.YELLOW}⚠️  {message}{Color.END}")

def add_section_if_missing(content, section_name, section_content):
    """Adiciona seção se não existir"""
    if f"## {section_name}" not in content and f"# {section_name}" not in content:
        return content + f"\n\n{section_content}"
    return content

def standardize_references(content):
    """Adiciona seção de referências padronizadas se não existir"""
    if "## 🔗 Referências" not in content and "## Referências" not in content:
        references = """
## 🔗 Referências Completas

- [PortSwigger Academy](https://portswigger.net/web-security)
- [OWASP Top 10](https://owasp.org/Top10/)
- [CWE](https://cwe.mitre.org/)
"""
        return content + references
    return content

def standardize_impact_table(content):
    """Adiciona tabela de impacto se não existir"""
    if "Confidencialidade" not in content and "Integridade" not in content:
        impact = """
## 💥 Impacto Técnico

| Aspecto | Risco |
|--------|-------|
| **Confidencialidade** | - |
| **Integridade** | - |
| **Disponibilidade** | - |
"""
        # Inserir antes das referências
        if "## 🔗 Referências" in content:
            return content.replace("## 🔗 Referências", impact + "\n## 🔗 Referências")
        return content + impact
    return content

def main():
    print(f"\n{Color.BLUE}{'='*70}")
    print(f"🤖 STANDARDIZE DOCS: Aplicando Template Padrão")
    print(f"{'='*70}{Color.END}\n")
    
    # Encontrar todos os README.md
    readme_files = list(Path(".").rglob("README.md"))
    
    print_status(f"Encontrados {len(readme_files)} arquivos README.md", "info")
    
    for readme_path in readme_files:
        # Skip docs e scripts
        if "docs" in str(readme_path) or "scripts" in str(readme_path):
            continue
        
        print_status(f"Processando: {readme_path}")
        
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Aplicar padronizações
            content = standardize_references(content)
            content = standardize_impact_table(content)
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
        except Exception as e:
            print_status(f"Erro ao processar {readme_path}: {e}", "warning")
    
    print(f"\n{Color.GREEN}{'='*70}")
    print(f"✅ Documentação Padronizada!")
    print(f"{'='*70}{Color.END}\n")

if __name__ == "__main__":
    main()