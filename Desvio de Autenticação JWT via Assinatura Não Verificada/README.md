# Laboratório: Desvio de Autenticação JWT via Assinatura Não Verificada

**PortSwigger Web Security Academy**  
**Dificuldade:** Aprendiz (Apprentice)

## 🎯 Objetivo

Explorar uma falha crítica de implementação de JWT onde o servidor **não verifica a assinatura** do token.  
O objetivo é modificar o token de sessão para obter acesso ao painel de administração (`/admin`) e excluir o usuário `carlos`.

---

## 🔧 Ferramentas Utilizadas

- **Burp Suite Community Edition**
- Navegador (Firefox/Chrome)
- jwt.io (opcional)

---

## 📝 Descrição da Vulnerabilidade

O aplicativo utiliza JWT para gerenciar sessões. No entanto, o back-end **não valida a assinatura** dos tokens recebidos. Isso permite que um atacante modifique claims sensíveis (como `sub`, `role`, etc.) e ainda assim seja aceito pelo servidor.

---

## ✅ Solução Passo a Passo

### 1. Login na aplicação
- Acesse o laboratório e faça login com as credenciais:
  - **Usuário:** `wiener`
  - **Senha:** `peter`

### 2. Captura do JWT
- No Burp Suite, vá em **Proxy → HTTP history**.
- Localize a requisição `GET /my-account` realizada após o login.
- Observe que o cookie `session` é um **JWT** (ex: `eyJ...`).

### 3. Envio para o Repeater
- Clique com o botão direito na requisição → **Send to Repeater**.

### 4. Teste de acesso ao painel admin
- Altere o caminho da requisição de `/my-account` para `/admin`.
- Envie a requisição.
- Você receberá uma resposta de acesso negado, pois o usuário atual (`wiener`) não é administrador.

### 5. Modificação do JWT (Parte Principal)

- No Repeater, selecione o valor completo do cookie `session`.
- No painel **Inspector** (lado direito), clique na aba **JWT**.
- Na seção **Payload**, altere:
  ```json
  "sub": "wiener"
  ```
  para
  ```json
  "sub": "administrator"
  ```

- Clique em **Apply changes**.

### 6. Acesso ao Painel de Administração
- Envie novamente a requisição com o caminho `/admin`.
- Agora você terá acesso completo ao painel de administração.

### 7. Exclusão do usuário Carlos
- Na resposta da página `/admin`, identifique a URL de exclusão:
  ```
  /admin/delete?username=carlos
  ```
- Envie uma requisição **GET** para essa URL.
- O laboratório será resolvido.

---

## 💡 Observações Importantes

- Como o servidor **não verifica a assinatura**, qualquer modificação no payload é aceita.
- Técnicas alternativas (não necessárias neste lab):
  - Alterar o algoritmo para `alg: none`
  - Adicionar claims como `"role": "administrator"` ou `"admin": true`

---

## 📚 Aprendizados

- JWTs não são seguros apenas por serem criptografados. A **verificação da assinatura** é essencial.
- Claims como `sub`, `role`, `admin`, etc., não devem ser confiáveis se a assinatura não for validada.
- Sempre valide a assinatura no servidor (usando bibliotecas atualizadas e chaves fortes).

---

## 🛡️ Recomendações de Correção

- Implementar verificação rigorosa da assinatura do JWT.
- Utilizar algoritmos fortes (`RS256`, `ES256`).
- Evitar claims sensíveis que possam ser facilmente manipulados.
- Implementar blacklist de tokens e controle de expiração (`exp`).

---

**Laboratório resolvido com sucesso!** ✅

---

**Quer que eu adicione seção de screenshots ou versão em inglês também?** Posso ajustar o write-up conforme sua preferência.
