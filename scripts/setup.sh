#!/bin/bash

# 🤖 Setup Script - Automatiza todo o processo
# Este script executa todos os passos automaticamente

set -e  # Parar em erro

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}🤖 AUTO-SETUP: Repositório${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Verificar se estamos no repositório correto
if [ ! -f "README.md" ]; then
    echo -e "${RED}❌ Erro: Execute este script na raiz do repositório${NC}"
    exit 1
fi

# Passo 1: Refatorar nomes de pastas
echo -e "${BLUE}📋 PASSO 1: Refatorando Nomes de Pastas...${NC}\n"
python3 scripts/auto-refactor.py

# Passo 2: Criar nova estrutura
echo -e "\n${BLUE}📁 PASSO 2: Criando Nova Estrutura de Diretórios...${NC}\n"
python3 scripts/create-structure.py

# Passo 3: Gerar arquivos padronizados
echo -e "\n${BLUE}📄 PASSO 3: Gerando READMEs Padronizados...${NC}\n"
python3 scripts/generate-files.py

# Passo 4: Padronizar documentação existente
echo -e "\n${BLUE}✏️  PASSO 4: Padronizando Documentação Existente...${NC}\n"
python3 scripts/standardize-docs.py

# Passo 5: Resumo final
echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}✅ SETUP COMPLETO!${NC}"
echo -e "${GREEN}========================================${NC}\n"

echo -e "${YELLOW}📝 Próximos passos:${NC}"
echo "1. Revisar arquivos gerados"
echo "2. Fazer commit: git add -A && git commit -m 'refactor: complete repository standardization'"
echo "3. Fazer push: git push origin main"
echo ""
