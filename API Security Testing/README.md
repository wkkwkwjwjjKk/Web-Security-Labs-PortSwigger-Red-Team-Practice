🔐 API Security Testing – PortSwigger Web Security Academy
👨‍💻 Sobre este repositório

🎯 Objetivo

Aprender na prática:

Reconhecimento de APIs
Identificação de endpoints e parâmetros ocultos
Exploração de APIs REST
Mass Assignment
Manipulação de requests com Burp Suite
Impacto real de falhas em lógica de backend

🧪 Laboratórios resolvidos

🔹 API Recon & Endpoint Discovery

Estudo de como APIs expõem superfícies de ataque através de:

/api/
/swagger
/openapi.json
JavaScript client-side endpoints

📌 Técnicas usadas:

Burp Suite Proxy
Burp Repeater
Burp Intruder
Análise de JavaScript

🔹 Hidden Parameters & API Fuzzing

Identificação de parâmetros não documentados através de:

Responses GET
Fuzzing de endpoints
Wordlists de parâmetros comuns
Análise de objetos JSON retornados

📌 Exemplo de aprendizado:

Parâmetros retornados pela API podem ser reutilizados como entrada.

🔹 Mass Assignment Vulnerability
📌 Conceito

Mass assignment ocorre quando a API automaticamente associa dados enviados pelo cliente a objetos internos sem validação adequada.

⚠️ Exemplo de falha
{
  "email": "user@email.com",
  "isAdmin": true
}

Se o backend aceitar isso sem validação:

👉 pode ocorrer escalonamento de privilégio

💣 Exploração prática

Identificação de campo oculto:

"chosen_discount": {
  "percentage": 0
}

Exploração:

{
  "chosen_discount": {
    "percentage": 100
  },
  "chosen_products": [
    {
      "product_id": "1",
      "quantity": 1
    }
  ]
}

🎯 Resultado

desconto aplicado indevidamente
compra concluída sem saldo
exploração bem-sucedida da API

🔹 API Endpoint Manipulation

Testes realizados em:

métodos HTTP (GET, POST, PATCH, DELETE)
alteração de Content-Type
endpoints ocultos
comportamento inconsistente entre endpoints

🧰 Ferramentas utilizadas

Burp Suite (Proxy, Repeater, Intruder)

Browser integrado do Burp

PortSwigger Web Security Academy

Análise manual de requests HTTP

🧠 Principais aprendizados

APIs expõem lógica interna diretamente ao cliente
JSON mal validado pode alterar comportamento crítico do backend
Endpoints ocultos são frequentemente reutilizados internamente
Mass assignment é uma falha comum em frameworks modernos
Observação de responses é tão importante quanto requests

⚔️ Impacto real

Essas falhas podem levar a:

alteração de preços
bypass de autenticação
privilege escalation
manipulação de pedidos
vazamento de dados interno

🚀 Conclusão

API Security não é apenas teoria — é sobre entender como aplicações realmente processam dados e como pequenas falhas de validação podem ser exploradas em impactos críticos.
