#!/usr/bin/env python3
"""
🤖 Create Repository Structure Script
Cria a nova estrutura de diretórios organizada
"""

import os
from pathlib import Path

class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_status(message, status="info"):
    if status == "success":
        print(f"{Color.GREEN}✅ {message}{Color.END}")
    elif status == "error":
        print(f"{Color.RED}❌ {message}{Color.END}")
    elif status == "info":
        print(f"{Color.BLUE}ℹ️  {message}{Color.END}")

def create_directory(path):
    """Cria diretório se não existir"""
    Path(path).mkdir(parents=True, exist_ok=True)
    print_status(f"Diretório criado/verificado: {path}", "success")

def create_gitkeep(path):
    """Cria arquivo .gitkeep para manter pastas vazias"""
    gitkeep_path = os.path.join(path, ".gitkeep")
    if not os.path.exists(gitkeep_path):
        Path(gitkeep_path).touch()

def main():
    print(f"\n{Color.BLUE}{'='*70}")
    print(f"🤖 CREATE STRUCTURE: Criando Nova Estrutura de Diretórios")
    print(f"{'='*70}{Color.END}\n")
    
    # Nova estrutura
    directories = [
        # Documentação
        "docs",
        
        # 1. Authentication
        "1-Authentication/Password-Based-Login",
        "1-Authentication/Authentication-Vulnerabilities",
        "1-Authentication/2FA-Broken-Logic",
        
        # 2. Injection
        "2-Injection/SQL-Injection",
        "2-Injection/Blind-SQL-Injection",
        "2-Injection/Command-Injection",
        "2-Injection/XXE-Injection",
        
        # 3. Access Control
        "3-Access-Control/IDOR",
        "3-Access-Control/Privilege-Escalation",
        
        # 4. Web Requests
        "4-Web-Requests/CSRF",
        "4-Web-Requests/SSRF",
        "4-Web-Requests/HTTP-Request-Smuggling",
        
        # 5. API Security
        "5-API-Security/API-Security-SSPP",
        "5-API-Security/OAuth-OpenID",
        
        # 6. Advanced
        "6-Advanced/JWT-Authentication",
        "6-Advanced/SSTI",
        "6-Advanced/Insecure-Deserialization",
        "6-Advanced/Business-Logic-Flaws",
        "6-Advanced/Web-Cache-Poisoning",
        
        # 7. File Upload
        "7-File-Upload/File-Upload-Vulnerabilities",
        
        # Scripts
        "scripts",
    ]
    
    print(f"{Color.BLUE}Criando estrutura de diretórios...{Color.END}\n")
    
    for directory in directories:
        create_directory(directory)
        create_gitkeep(directory)
    
    print(f"\n{Color.GREEN}{'='*70}")
    print(f"✅ Estrutura Criada com Sucesso!")
    print(f"{'='*70}{Color.END}\n")
    
    print(f"{Color.YELLOW}Próxima etapa: Mover arquivos existentes para as novas pastas{Color.END}\n")

if __name__ == "__main__":
    main()