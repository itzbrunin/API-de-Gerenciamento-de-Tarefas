# Script para fazer push do projeto para GitHub
# Execute este arquivo após adicionar a chave SSH ao GitHub

$projectPath = "D:\Pastas de Programação treinamentos\ProjetoAPI\task_api"
$repoUrl = "git@github.com:itzbrunin/API-de-Gerenciamento-de-Tarefas.git"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Iniciando push do projeto para GitHub..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navega para a pasta do projeto
Set-Location $projectPath
Write-Host "Pasta do projeto: $projectPath" -ForegroundColor Green

# Verifica status do git
Write-Host "`nVerificando status do repositório..." -ForegroundColor Yellow
git status
Write-Host ""

# Tenta fazer o push
Write-Host "Fazendo push para GitHub..." -ForegroundColor Yellow
git push -u origin main

# Verifica se o push foi bem-sucedido
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Push completado com sucesso!" -ForegroundColor Green
    Write-Host "Seu projeto está agora em: https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas" -ForegroundColor Green
} else {
    Write-Host "`n❌ Erro ao fazer push. Verificar erro acima." -ForegroundColor Red
    Write-Host "Se o erro for de autenticação, tente adicionar a chave SSH ao GitHub primeiro." -ForegroundColor Yellow
}
