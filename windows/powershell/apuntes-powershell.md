# INTRODUCCIÓN A POWERSHELL

## Teoria básica

Los comandos de PowerShell se conocen como cmdlets.

### Comentarios

'#'

### Scope 'Set-ExecutionPolicy'

El argumento **Scope** permite específicar el ámbito de la política de ejecución de scripts que se está estableciendo.

- **Process**: establece la política de ejecución de scripts solo para la sesión actual de Powershell. Es útil si solo deseamos establecer temporalmente la política de ejecución de scripts para la sesión actual.
- **CurrentUser**: establece la política de ejecución de scripts para el usuario actual en el equipo. Es útil si queremos establecer la política de ejecución de scripts para todos los scripts que se ejecuten por el usuario actual.
- **LocalMachine**: establece la política de ejecución de scripts para todas las cuentas de usuario en el equipo. Es util si queremos establecer la politica de ejecución de scripts para todos los scripts que se ejecuten en el equipo
- **Undefined**: establece la política de ejecución de scripts en un nivel indefinido. Es util para establecer la política de ejecución de scripts para un objeto de ámbito personalizado.

### Directivas de ejecucion

Para poder ejecutar nuestros scripts en powershell necesitamos cambiar las directivas de seguridad de nuestro sistema, de manera predeterminada nos viene dado Restricted.

```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

La directiva recomendada por Microsoft es usar RemoteSigned

### Sintaxis y estructura

La estructura de un cmdlet se establece en Verbo-sujeto
los más comunes son

```ps
get-ChildItem
set-Location
```

### Obtener ayuda

Para obtener asistencia actualizada vamos a ejecutar este comando

```ps
 cmdlet Update-Help
```

Para obtener ayuda en PowerShell utilzaremos el cmdlet ``Get-Help``

```ps
Get-Help -Name Get-Help -Full
help -Name Get-Help -Full
help Get-Help -Full
```
