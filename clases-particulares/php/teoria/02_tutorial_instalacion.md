---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Tutorial de instalación de PHP

- [Tutorial de instalación de PHP](#tutorial-de-instalación-de-php)
  - [Instalación en servidor/pc para desarrollo (SOLO PHP)](#instalación-en-servidorpc-para-desarrollo-solo-php)
  - [Windows](#windows)
  - [Linux](#linux)
    - [Ubuntu](#ubuntu)
    - [Arch](#arch)
    - [CentOS](#centos)
    - [Verificar instalación](#verificar-instalación)
  - [MacOS](#macos)
    - [Verificar instalación](#verificar-instalación-1)
  - [Instalación en servidor/pc para desarrollo con XAMPP/LAMP](#instalación-en-servidorpc-para-desarrollo-con-xampplamp)
  - [Windows](#windows-1)
    - [Instalar XAMPP](#instalar-xampp)
    - [Iniciar y parar servicios](#iniciar-y-parar-servicios)
    - [Cambiar puertos (opcional)](#cambiar-puertos-opcional)
  - [Linux](#linux-1)
    - [Ubuntu](#ubuntu-1)
      - [Instalar LAMPP](#instalar-lampp)
      - [Iniciar y parar LAMPP](#iniciar-y-parar-lampp)
      - [Cambiar puertos (opcional)](#cambiar-puertos-opcional-1)
  - [Instalación en servidor para producción](#instalación-en-servidor-para-producción)
    - [1. Actualizar el sistema](#1-actualizar-el-sistema)
    - [2. Instalar Apache](#2-instalar-apache)
    - [3. Instalar PHP](#3-instalar-php)
    - [4. Instalar MySQL](#4-instalar-mysql)
    - [5. Iniciar y habilitar servicios](#5-iniciar-y-habilitar-servicios)
    - [6. Configurar MySQL](#6-configurar-mysql)
    - [7. Verificar la instalación](#7-verificar-la-instalación)

## Instalación en servidor/pc para desarrollo (SOLO PHP)

## Windows

## Linux

### Ubuntu

~~~bash
sudo apt update && sudo apt install php libapache2-mod-php
~~~

### Arch

~~~bash
sudo pacman -S php
~~~

### CentOS

~~~bash
sudo yum install php
~~~

### Verificar instalación

~~~bash
php -v
~~~

## MacOS

> :warning: **ADVERTENCIA** en este caso voy a utilizar [Homebrew](https://brew.sh/) para instalar los paquetes necesarios

~~~sh
brew install php
~~~

### Verificar instalación

~~~bash
php -v
~~~

## Instalación en servidor/pc para desarrollo con XAMPP/LAMP

> :warning: **ADVERTENCIA** esta parte solo será explicada en entornos Windows 10 y Linux Ubuntu 20.04

## Windows

### Instalar XAMPP

###  Iniciar y parar servicios

### Cambiar puertos (opcional)

## Linux

### Ubuntu

#### Instalar LAMPP

1. Descargar desde el [sitio oficial de XAMPP](https://www.apachefriends.org/index.html)
2. Ir a descargas

~~~sh
cd ~/Descargas
~~~

3. Cambiar permisos para poder ejecutar el fichero

~~~sh
chmod +x nombre_del_archivo_descargado.run
~~~

4. Ejecutar

~~~sh
sudo ./nombre_del_archivo_descargado.run
~~~

5. Seguir el instalador

#### Iniciar y parar LAMPP

~~~sh
sudo /opt/lampp/lampp start
~~~

~~~sh
sudo /opt/lampp/lampp stop
~~~

#### Cambiar puertos (opcional)

1. Acceder al fichero de configuracion httpd.conf

~~~sh
sudo nano /opt/lampp/etc/httpd.conf
~~~

2. Modificar estas líneas

~~~sh
Listen 80
ServerName localhost:80
~~~

3. Guardar cambios y cerrar el editor de texto

4. Reiniciar servicio

~~~sh
sudo /opt/lampp/lampp restart
~~~

## Instalación en servidor para producción

> :warning: **ADVERTENCIA** esta parte solo será explicada en entornos de servidor Linux, concretamente Debian o RHEL.

En entornos de servidor Linux, como Debian o RHEL (Red Hat Enterprise Linux), puedes seguir los siguientes pasos para instalar Apache, PHP y MySQL para producción:

### 1. Actualizar el sistema

Antes de comenzar con la instalación, asegúrate de que el sistema esté actualizado ejecutando los siguientes comandos:

**Debian/Ubuntu:**

~~~bash
sudo apt update
sudo apt upgrade
~~~

**RHEL/CentOS:**

~~~bash
sudo yum update
~~~

### 2. Instalar Apache

**Debian/Ubuntu:**

~~~bash
sudo apt install apache2
~~~

**RHEL/CentOS:**

~~~bash
sudo yum install httpd
~~~

### 3. Instalar PHP

**Debian/Ubuntu:**

~~~bash
sudo apt install php
~~~

**RHEL/CentOS:**

~~~bash
sudo yum install php
~~~

### 4. Instalar MySQL

**Debian/Ubuntu:**

~~~bash
sudo apt install mysql-server
~~~

**RHEL/CentOS:**

~~~bash
sudo yum install mysql-server
~~~

### 5. Iniciar y habilitar servicios

**Debian/Ubuntu:**

~~~bash
sudo systemctl start apache2
sudo systemctl start mysql
sudo systemctl enable apache2
sudo systemctl enable mysql
~~~

**RHEL/CentOS:**

~~~bash
sudo systemctl start httpd
sudo systemctl start mysqld
sudo systemctl enable httpd
sudo systemctl enable mysqld
~~~

### 6. Configurar MySQL

Después de instalar MySQL, es posible que debas configurar la contraseña del usuario root de MySQL y realizar otras configuraciones de seguridad.

~~~bash
sudo mysql_secure_installation
~~~

### 7. Verificar la instalación

Para verificar que todo esté funcionando correctamente, **abre un navegador web** y **visita la dirección IP o el nombre de dominio de tu servidor**. Deberías ver la página predeterminada de Apache.

Para probar que PHP también está funcionando correctamente, crea un **archivo phpinfo.php** en el directorio raíz de tu servidor web con el siguiente contenido:

~~~php
<?php
    phpinfo();
?>
~~~

Guarda el archivo y **visita http://tu_direccion_ip/phpinfo.php** en tu navegador. Deberías ver una página con información detallada sobre la configuración de PHP.

Con esto, deberías tener Apache, PHP y MySQL instalados y funcionando en tu servidor Linux para producción.
