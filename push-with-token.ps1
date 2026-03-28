# Script interativo para fazer push com Personal Access Token

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "PUSH via HTTPS com Personal Access Token" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se o PAT foi fornecido como parâmetro
param(
    [string]$Token = ""
)

if ([string]::IsNullOrEmpty($Token)) {
    Write-Host "Para fazer push via HTTPS, você precisa de um Personal Access Token (PAT)." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Como gerar um token:" -ForegroundColor Cyan
    Write-Host "1. Acesse: https://github.com/settings/tokens/new" -ForegroundColor White
    Write-Host "2. Name: API-Tarefas-Push" -ForegroundColor White
    Write-Host "3. Scopes: Marque 'repo'" -ForegroundColor White
    Write-Host "4. Copie o token (começa com ghp_)" -ForegroundColor White
    Write-Host ""
    
    $Token = Read-Host "Cole seu Personal Access Token"
}

if ([string]::IsNullOrEmpty($Token)) {
    Write-Host "❌ Token não fornecido. Abortando." -ForegroundColor Red
    exit 1
}

$projectPath = "D:\Pastas de Programação treinamentos\ProjetoAPI\task_api"
$username = "itzbrunin"
$repoUrl = "https://$username`:$Token@github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas.git"

Write-Host ""
Write-Host "Configurando repositório..." -ForegroundColor Yellow
Set-Location $projectPath

# Configura o repositório remoto com autenticação
git remote set-url origin "$repoUrl"

Write-Host "Fazendo push..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Push completado com sucesso!" -ForegroundColor Green
    Write-Host "Seu repositório: https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas" -ForegroundColor Green
    
    # Abre o repositório no navegador
    Start-Process "https://github.com/itzbrunin/API-de-Gerenciamento-de-Tarefas"
} else {
    Write-Host ""
    Write-Host "❌ Erro ao fazer push." -ForegroundColor Red
    Write-Host "Verifique se o token está correto e tente novamente." -ForegroundColor Yellow
}
