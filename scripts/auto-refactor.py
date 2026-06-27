#!/usr/bin/env python3
"""
🤖 Auto-Refactor Script
Automaticamente padroniza a estrutura e nomenclatura do repositório
"""

import os
import shutil
import subprocess
from pathlib import Path

# Cores para terminal
class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_status(message, status="info"):
    """Imprime mensagens formatadas"""
    if status == "success":
        print(f"{Color.GREEN}✅ {message}{Color.END}")
    elif status == "error":
        print(f"{Color.RED}❌ {message}{Color.END}")
    elif status == "warning":
        print(f"{Color.YELLOW}⚠️  {message}{Color.END}")
    elif status == "info":
        print(f"{Color.BLUE}ℹ️  {message}{Color.END}")

def run_git_command(cmd):
    """Executa comando git e retorna resultado"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)

def rename_folder(old_name, new_name):
    """Renomeia pasta usando git mv"""
    print_status(f"Renomeando '{old_name}' → '{new_name}'", "info")
    success, msg = run_git_command(f'git mv "{old_name}" "{new_name}"')
    if success:
        print_status(f"Pasta renomeada", "success")
        return True
    else:
        print_status(f"Erro ao renomear: {msg}", "error")
        return False

def delete_file(filename):
    """Deleta arquivo usando git rm"""
    if os.path.exists(filename):
        print_status(f"Deletando arquivo: {filename}", "info")
        success, msg = run_git_command(f'git rm "{filename}"')
        if success:
            print_status(f"Arquivo deletado", "success")
            return True
        else:
            print_status(f"Erro ao deletar: {msg}", "warning")
            return False
    else:
        print_status(f"Arquivo não encontrado: {filename}", "warning")
        return False

def main():
    """Script principal"""
    print(f"\n{Color.BLUE}{'='*70}")
    print(f"🤖 AUTO-REFACTOR: Padronizando Repositório")
    print(f"{'='*70}{Color.END}\n")
    
    # Lista de renomeações
    renames = [
        ("CSRF ", "CSRF"),
        ("JWT Authentication ", "JWT-Authentication"),
        ("2FA Broken Logic", "2FA-Broken-Logic"),
        ("SQL_Injection", "SQL-Injection"),
    ]
    
    print(f"{Color.BLUE}ETAPA 1: Renomeando Pastas{Color.END}\n")
    for old_name, new_name in renames:
        if os.path.exists(old_name):
            rename_folder(old_name, new_name)
        else:
            print_status(f"Pasta '{old_name}' não encontrada (talvez já foi renomeada)", "warning")
    
    print(f"\n{Color.BLUE}ETAPA 2: Deletando Arquivos Desnecessários{Color.END}\n")
    
    # Procurar por screenshots na pasta SQL-Injection
    screenshot_pattern = "SQL-Injection/Screenshot*"
    for file in Path("SQL-Injection/").glob("Screenshot*"):
        delete_file(str(file))
    
    print(f"\n{Color.BLUE}ETAPA 3: Commit e Push{Color.END}\n")
    
    # Fazer commit
    print_status("Fazendo commit das mudanças", "info")
    success, msg = run_git_command('git commit -m "refactor: standardize folder naming and remove unnecessary files"')
    if success:
        print_status("Commit realizado", "success")
        
        # Fazer push
        print_status("Fazendo push para o repositório remoto", "info")
        success, msg = run_git_command("git push origin main")
        if success:
            print_status("Push realizado com sucesso!", "success")
        else:
            print_status(f"Erro no push: {msg}", "warning")
    else:
        if "nothing to commit" in msg:
            print_status("Nenhuma mudança para commit", "info")
        else:
            print_status(f"Erro no commit: {msg}", "warning")
    
    print(f"\n{Color.GREEN}{'='*70}")
    print(f"✅ Refatoração Concluída!")
    print(f"{'='*70}{Color.END}\n")

if __name__ == "__main__":
    main()