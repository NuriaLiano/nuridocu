# INTRODUCIÓN A POWERSHELL

## EJERCICIOS BÁSICOS

1. Ver la versión de powershell

    ~~~powershell
    $PSVersionTable
    ~~~

2. Ver directiva de ejecución
    Evita que un usuario ejecute un script sin saberlo

   ~~~powershell
   Get-ExecutionPolicy
   ~~~

3. Mostrar  todos los archivos y carpetas en el directorio actual

    ~~~powershell
    Get-ChildItem
    ~~~

3. Buscar un fichero .txt

    ~~~powershell
    Get-ChildItem -Filter *.txt
    ~~~

4. Mostrar una lista de todos los servicios de Windows en tu equipo.

    ~~~powershell
    Get-Service
    ~~~

5. Filtrar la salida del comando anterior para mostrar solo los servicios que están en estado "Running".

    ~~~powershell
    Get-Service | Where-Object {$_.Status -eq "Running"}
    ~~~

6. Crear una nueva carpeta en tu escritorio llamada "Test".

    ~~~powershell
    New-Item -ItemType Directory -Path C:\Users\username\Desktop\Test
    ~~~

7. Cambia el nombre de la carpeta "Test" a "NewFolder"

    ~~~powershell
    Rename-Item -Path C:\Users\username\Desktop\Test -NewName "NewFolder"
    ~~~

8. Borra la carpeta "NewFolder"

    ~~~powershell
    Remove-Item -Path C:\Users\username\Desktop\NewFolder -Recurse
    ~~~

9.  Muestra información del sistema

    ~~~powershell
    systeminfo
    Get-ComputerInfo
    ~~~

10. Obtener información de un proceso específico.

    ~~~powershell
    Get-Process notepad
    ~~~

11. Obtener información extensa de un proceso específico.

    ~~~powershell
    Get-Process notepad | Select-Object *
    ~~~

12. Cambiar el fondo de pantalla.

    ~~~powershell
    Set-ItemProperty -Path 'HKCU:\Control Panel\Desktop' -Name Wallpaper -Value 'C:\images\wallpaper.jpg'
    ~~~

13. Copiar archivos de una carpeta a otra.

    ~~~powershell
    Get-ChildItem -Path C:\carpetaorigen | Copy-Item -Destination C:\carpetadestino -Recurse
    ~~~

14. Cambiar permisos de carpeta

    ~~~powershell
    icacls C:\Carpeta /grant "nombredeusuario:(OI)(CI)RX
    ~~~

15. Ejecutar comandos en paralelo.

    ~~~powershell
    Start-Job -ScriptBlock { comando1 } ; Start-Job -ScriptBlock { comando2 } ; Get-Job | Receive-Job
    ~~~

16. Monitorear eventos del sistema.

    ~~~powershell
    Get-WinEvent -LogName Security -FilterXPath "*[System[EventID=4624]]" -Verbose | Select-Object -First 10
    ~~~

17. Crear scripts avanzados

    **datos.csv**
    nombre,edad,ciudad
    Juan,25,Madrid
    María,30,Barcelona
    Pedro,40,Madrid

    1. Lea un archivo CSV y conviértalo en una lista de objetos.

        ~~~powershell
        $datos = Import-Csv -Path .\datos.csv        
        ~~~

    2. Filtrar la lista para incluir solo aquellos objetos que cumplen ciertos criterios.

        ~~~powershell
        $datosFiltrados = $datos | Where-Object { $_.ciudad -eq "Madrid" }
        ~~~

    3. Ejecutar una serie de comandos en los objetos seleccionados.

        ~~~powershell
        foreach ($dato in $datosFiltrados) {
            Write-Host "Nombre: $($dato.nombre), Edad: $($dato.edad)"
        }
        ~~~

    4. Exportar los resultados a un nuevo archivo CSV.

        ~~~powershell
        $datosFiltrados | Export-Csv -Path .\resultados.csv -NoTypeInformation
        ~~~

18. Buscar paquetes con Winget

    ~~~powershell
    winget search Firefox
    ~~~

19. Instalar paquetes con Winget

    ~~~powershell
    winget install Firefox
    ~~~

20. Desinstalar paquetes con Winget

    ~~~powershell
    winget uninstall Firefox
    ~~~

21. Listar paquetes con Winget

    ~~~powershell
    winget list
    ~~~

