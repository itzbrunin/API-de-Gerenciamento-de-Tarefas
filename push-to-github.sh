#!/bin/bash
# Script para fazer push do projeto para GitHub via Git Bash

PROJECT_PATH="D:\Pastas de Programação treinamentos\ProjetoAPI\task_api"
REPO_URL="git@github.com:itzbrunin/API-de-Gerenciamento-de-Tarefas.git"

echo "========================================"
echo "Iniciando push do projeto para GitHub..."
echo "========================================"
echo ""

# Navega para a pasta do projeto
cd "$PROJECT_PATH"
echo "Pasta do projeto: $PROJECT_PATH"

# Verifica status do git
echo ""
echo "Verificando status do repositório..."
git status
echo ""

# Tenta fazer o push
echo "Fazendo push para GitHub..."
git push -u origin main

# Verifica se o push foi bem-sucedido
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Push completado com sucesso!"
    echo "Seu projeto está agora em: https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas"
else
    echo ""
    echo "❌ Erro ao fazer push. Verificar erro acima."
    echo "Se o erro for de autenticação, tente adicionar a chave SSH ao GitHub primeiro."
fi
