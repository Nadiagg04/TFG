$base = Split-Path -Parent $MyInvocation.MyCommand.Definition
$torExe = Join-Path $base 'tor\tor.exe'
$torrc = Join-Path $base 'torrc'

if (-Not (Test-Path $torExe)) {
    Write-Error "No se encontró tor.exe en $torExe. Extrae el Expert Bundle en este directorio."
    exit 1
}
if (-Not (Test-Path $torrc)) {
    Write-Error "No se encontró torrc en $torrc. Copia torrc.template a torrc y ajústalo si hace falta."
    exit 1
}

$existing = netstat -an | Select-String ':9050|:9051'
if ($existing) {
    Write-Host "Parece que Tor ya está ejecutándose o los puertos 9050/9051 están ocupados."
    $existing | ForEach-Object { Write-Host $_.Line }
    Write-Host "Si quieres iniciar una nueva instancia, detén la anterior o cambia los puertos en torrc."
    return
}

Write-Host "Iniciando tor.exe con configuración: $torrc"
Start-Process -FilePath $torExe -ArgumentList "-f \"$torrc\"" -WorkingDirectory $base -NoNewWindow -PassThru | Out-Null
Start-Sleep -Seconds 2
Write-Host "Tor se está iniciando. Revisa los puertos 9050/9051 y usa test-tor.ps1 para validar."