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

Write-Host "Tor bundle path: $torExe"
Write-Host "Tor config: $torrc"
Write-Host "Verificando puertos locales 9050 y 9051..."
netstat -an | findstr 9050
netstat -an | findstr 9051

if (Get-Command curl.exe -ErrorAction SilentlyContinue) {
    Write-Host "Probando petición HTTP vía Tor SOCKS..."
    curl.exe --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/ -I
} else {
    Write-Host "curl.exe no encontrado; intentando Invoke-WebRequest..."
    try {
        Invoke-WebRequest -Uri https://check.torproject.org/ -Proxy 'socks5h://127.0.0.1:9050' -UseBasicParsing -Method Head
    } catch {
        Write-Host "Error de prueba HTTP con Invoke-WebRequest: $_"
    }
}

