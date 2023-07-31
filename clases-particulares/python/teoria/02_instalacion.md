---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Tutorial de instalación de Python

- [Tutorial de instalación de Python](#tutorial-de-instalación-de-python)
  - [Descarga e instalación de Python](#descarga-e-instalación-de-python)
    - [Windows](#windows)
  - [Linux](#linux)
    - [Ubuntu](#ubuntu)
    - [Arch](#arch)
    - [CentOS](#centos)
    - [Verificar instalación](#verificar-instalación)
  - [MacOS](#macos)
    - [Verificar instalación](#verificar-instalación-1)

## Descarga e instalación de Python

### Windows

La descarga de Python en Windows la puedes realizar desde [este enlace](https://www.python.org/downloads/windows/) a su página oficial para asegurar que descargas la última versión estable.
Una vez esté descargado el paquete sólo tendrás que seguir el instalador

## Linux

### Ubuntu

>:pencil: **NOTA**: En Ubuntu, Python generalmente ya está instalado en las versiones recientes.

~~~bash
sudo apt update && sudo apt install python3 python3-pip
~~~

Una vez esté descargado el paquete sólo tendrás que seguir el instalador

### Arch

~~~bash
sudo pacman -Sy python
~~~

Una vez esté descargado el paquete sólo tendrás que seguir el instalador

### CentOS

> :pencil: **NOTA** En CentOS, por defecto, se instala Python 2.x

~~~bash
sudo yum install python3
~~~

Una vez esté descargado el paquete sólo tendrás que seguir el instalador

### Verificar instalación

~~~bash
python --version
python3 --version
~~~

## MacOS

> :warning: **ADVERTENCIA** en este caso voy a utilizar [Homebrew](https://brew.sh/) para instalar los paquetes necesarios
>
> :pencil: **NOTA** macOS ya viene con Python 2.x preinstalado

~~~sh
brew install python3
~~~

Una vez esté descargado el paquete sólo tendrás que seguir el instalador

### Verificar instalación

~~~bash
python3 --version
~~~
