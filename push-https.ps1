# Script para fazer push com HTTPS usando Git Credential Manager
# Permite push sem SSH configurado

$projectPath = "D:\Pastas de Programação treinamentos\ProjetoAPI\task_api"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Iniciando push VIA HTTPS (sem SSH)..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navega para a pasta do projeto
Set-Location $projectPath
Write-Host "Pasta do projeto: $projectPath" -ForegroundColor Green

# Garante que está na branch main
Write-Host "`nAlternando para branch main..." -ForegroundColor Yellow
git branch -M main

# Mostra status antes do push
Write-Host "`nStatus atual:" -ForegroundColor Yellow
git status

# Configura HTTPS como padrão
Write-Host "`nConfigurando repositório para HTTPS..." -ForegroundColor Yellow
git remote set-url origin https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas.git

# Tenta fazer o push
Write-Host "`nFazendo push para GitHub via HTTPS..." -ForegroundColor Yellow
Write-Host "Nota: Uma janela de autenticação pode aparecer. Use seu GitHub username e token PAT." -ForegroundColor Cyan
Write-Host ""

git push -u origin main

# Verifica resultado
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Push completado com sucesso!" -ForegroundColor Green
    Write-Host "Seu projeto está em: https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas" -ForegroundColor Green
    Write-Host ""
    Start-Process "https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas"
} else {
    Write-Host "`n❌ Erro ao fazer push." -ForegroundColor Red
    Write-Host "Opções:" -ForegroundColor Yellow
    Write-Host "1. Gerar Personal Access Token em: https://github.com/settings/tokens/new" -ForegroundColor Yellow
    Write-Host "2. Usar seu GitHub username + PAT ao ser solicitado" -ForegroundColor Yellow
}
