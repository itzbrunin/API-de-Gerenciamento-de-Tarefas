# 🚀 Como fazer Push sem SSH (usando HTTPS)

Se você não quer usar SSH, pode fazer o push usando **HTTPS com Personal Access Token (PAT)**.

## Opção 1: Push Automático com Script (Mais Fácil)

### Passo 1: Gerar Token no GitHub

1. Acesse: https://github.com/settings/tokens/new
2. Preencha:
   - **Note**: `API-Tarefas-Push`
   - **Expiration**: 30 dias (ou mais)
   - **Scopes**: Marque apenas **`repo`**
3. Clique em **"Generate token"**
4. **COPIE o token** (aparece como `ghp_xxxxxxxxxxxxx`)

### Passo 2: Executar o Script

No PowerShell, navegue até a pasta do projeto e execute:

```powershell
cd "D:\Pastas de Programação treinamentos\ProjetoAPI\task_api"
.\push-with-token.ps1
```

Quando pedir, cole o token que você copiou.

### Resultado
✅ Seu projeto será enviado para GitHub automaticamente!

---

## Opção 2: Push Manual com Comando (Mais Controle)

Se preferir fazer manualmente:

```powershell
cd "D:\Pastas de Programação treinamentos\ProjetoAPI\task_api"

# Configure com seu token
$token = "ghp_xxxxxxxxxxxxx"  # Substitua pelo seu token
git remote set-url origin "https://itzbrunin:$token@github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas.git"

# Faça o push
git push -u origin main
```

---

## Opção 3: Usar Git Credential Manager (Mais Fácil, Sem Expor Token)

```powershell
# Configure para usar credential manager
git config --global credential.helper manager

# Faça o push normalmente (Git vai pedir autenticação)
cd "D:\Pastas de Programação treinamentos\ProjetoAPI\task_api"
git push -u origin main
```

Quando pedir autenticação, use:
- **Username**: `itzbrunin`
- **Password**: Cole seu Personal Access Token

---

## Diferenças entre Métodos

| Método | Segurança | Facilidade | Requer Token Exposto |
|--------|-----------|-----------|----------------------|
| Script automático | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Temporariamente |
| Manual com token | ⭐⭐ | ⭐⭐⭐ | ⚠️ Sim |
| Credential Manager | ⭐⭐⭐⭐ | ⭐⭐⭐ | Não |

---

## Verificação

Após fazer o push, acesse:
```
https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas
```

Você deve ver seus commits e arquivos no repositório.

---

## Troubleshooting

**Erro: "Authentication failed"**
- Verifique se o token está correto
- Verifique se o token não expirou
- Verifique se você marcou a scope `repo` ao gerar o token

**Erro: "Repository not found"**
- Verifique o nome do repositório
- Verifique se você tem acesso ao repositório
- Verifique se o repositório existe no GitHub

**Erro: "fatal: could not read from remote repository"**
- Verifique sua conexão com a internet
- Verifique se a URL está correta
