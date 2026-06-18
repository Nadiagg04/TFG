# Tor Expert Bundle Setup

Este directorio almacena la configuración para usar Tor Expert Bundle con el notebook.

## Pasos

1. Descarga el Tor Expert Bundle 64-bit desde la web oficial de Tor:
   - https://www.torproject.org/download/
   - Busca "Tor Expert Bundle" y descarga la versión para Windows.

2. Copia el ZIP descargado a `tor-bundle` y extráelo allí.

3. Crea el directorio de datos (si no existe):
```powershell
mkdir .\tor-bundle\data
```

4. Crea el archivo `tor-bundle\torrc` a partir de `tor-bundle\torrc.template`.

5. Inicia Tor con el archivo de configuración:
```powershell
cd .\tor-bundle
Start-Process -FilePath .\tor\Tor.exe -ArgumentList "-f .\torrc" -NoNewWindow
```

6. Verifica que Tor escucha en los puertos locales esperados:
```powershell
netstat -an | findstr 9050
netstat -an | findstr 9051
```

7. Ejecuta el notebook y asegúrate de que la configuración usa:
- `TOR_PROXY = socks5://127.0.0.1:9050`
- `TOR_CONTROL_PORT = 9051`

## Notas

- Si usas `TOR_CONTROL_PORT = 9051`, el `ControlPort` debe estar habilitado en `torrc`.
- Si necesitas autenticación, agrega `HashedControlPassword` o `CookieAuthentication` según tu configuración.
