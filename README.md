# portswigger-labs
Web Security Labs, Writeups and Vulnerability Analysis

Command Injection - PortSwigger Labs Writeups
Este repositório contém writeups de laboratórios da PortSwigger Web Security Academy focados em vulnerabilidades de Command Injection.

1. Basic Command Injection
Executar comandos no servidor explorando uma vulnerabilidade de Command Injection.

Durante a análise, observei que o parâmetro stockId era responsável pela consulta de estoque. Ao modificar o parâmetro e inserir operadores de comando, foi possível executar comandos no sistema operacional do servidor, confirmando a vulnerabilidade.

2. Command Injection - Delay
Executar comandos no servidor e provocar atraso na resposta da aplicação.

Durante a análise, observei que o parâmetro email podia ser manipulado. Ao inserir comandos com delay, a resposta da aplicação passou a demorar mais que o normal, confirmando a execução de comandos no servidor.

3. Blind OS Command Injection with Output Redirection
Executar comandos no servidor explorando Blind Command Injection com redirecionamento de saída.

A aplicação não retornava saída direta dos comandos. Ao redirecionar a saída para um arquivo acessível pela aplicação, foi possível confirmar a execução dos comandos no servidor através do navegador.

🧠 Aprendizados

Command Injection (básico e blind)
Técnicas de delay-based detection
Output redirection para validação
Exploração de parâmetros vulneráveis
🛡️ Mitigação
Sanitização de entrada
Evitar execução de comandos diretos no sistema
Uso de APIs seguras
Validação rigorosa de parâmetros

# Web Shell Upload Attacks - PortSwigger Labs Writeups

Este repositório contém uma série de writeups de laboratórios da PortSwigger Web Security Academy focados em vulnerabilidades de upload de arquivos e exploração via Web Shell.

O objetivo dos estudos é aprofundar técnicas de exploração de **Remote Code Execution (RCE)** através de diferentes falhas em mecanismos de upload.

---

## 🔥 1. Remote Code Execution via Web Shell Upload

### Objetivo
Executar comandos remotamente no servidor explorando upload de Web Shell.

### Resumo
A aplicação permitia upload de arquivos sem validação adequada. Após enviar uma Web Shell, foi possível acessá-la via navegador e executar comandos no sistema operacional do servidor.

---

## 🔥 2. Content-Type Restriction Bypass

### Objetivo
Explorar bypass de validação baseada em Content-Type.

### Resumo
A aplicação validava apenas o header Content-Type durante o upload. Ao modificá-lo, foi possível enviar uma Web Shell e executar comandos remotamente.

---

## 🔥 3. Path Traversal Upload

### Objetivo
Explorar upload de arquivos combinado com Path Traversal.

### Resumo
A aplicação permitia controle parcial do caminho de salvamento do arquivo. Utilizando Path Traversal, foi possível armazenar uma Web Shell em diretório acessível e executar comandos no servidor.

---

## 🔥 4. Extension Blacklist Bypass

### Objetivo
Bypass de bloqueio baseado em blacklist de extensões.

### Resumo
A validação de extensões era baseada apenas em lista negra. Ao alterar a extensão do arquivo, foi possível enviar uma Web Shell e obter execução remota de comandos.

---

## 🔥 5. Obfuscated File Extension

### Objetivo
Bypass de validação de extensão via ofuscação.

### Resumo
A aplicação não normalizava corretamente o nome do arquivo. Usando extensão ofuscada, foi possível realizar upload de Web Shell e executar comandos no servidor.

---

## 🧠 Aprendizados

- Técnicas de bypass em filtros de upload
- Execução remota de comandos (RCE)
- Exploração de Web Shells
- Validações inseguras de arquivos
- Importância de sanitização e controle de upload

---

## 🛡️ Mitigações gerais

- Validar tipo real do arquivo (não apenas extensão/header)
- Armazenar uploads fora do diretório web
- Impedir execução de arquivos enviados
- Sanitizar nomes de arquivos
- Aplicar controles de acesso rigorosos

---

## 🎯 Objetivo do repositório

Construir base prática em segurança ofensiva focada em Web Exploitation e preparação para atuação em Red Team.

---

📌 Estudos baseados na PortSwigger Web Security Academy
