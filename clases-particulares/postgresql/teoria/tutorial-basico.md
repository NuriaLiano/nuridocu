---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Tutorial básico

>:warning: **ADVERTENCIA** es recomendable no usar Windows para instalar PostgreSQL, en cambio, puedes utilizar una distribución de Linux como Ubuntu

## Instalación

>:warning: **ADVERTENCIA** este tutorial está realizado sobre la distribución Ubuntu 22.04 de Linux. Si quieres realizar la instalación desde otra distribución o sistema operativo puedes seguir la [documentación oficial de instalación](https://www.postgresql.org/download/)

### Requisitos

El respositorio de PostgreSQL está soportado en estas versiones de Ubuntu:

- kinetic (22.10, non-LTS)
- jammy (22.04, LTS)
- focal (20.04, LTS)
- bionic (18.04, LTS)

>:pencil: **NOTA** si tu versión de Ubuntu no está incluida en esa lista, puedes añadir manualmente el [respositorio oficial de PostgreSQL](https://apt.postgresql.org/)

Y para las siguientes arquitecturas:

- amd64
- arm64 (18.04 and newer; LTS releases only)
- i386 (18.04 and older)
- ppc64el (LTS releases only

### Instalación desde paquetes de nuestra distribución

Es la forma más sencilla de instalación pero puede que nuestra distribución no tenga la última versión de PostgreSQL.

- Podemos buscar los paquetes disponibles en la distribución usando el comando 'search'

~~~sql
apt search postgresql
~~~

- Podemos obtener información sobre el paquete que queramos instalar con el comando 'info'.
  De esta forma podemos ver si el repositorio de nuestra distribución está actualiado.

~~~sql
apt info postgresql
~~~

1. Instalar PostgreSQL

>:pencil: **NOTA** Nos tenemos que fijar en los paquetes ('postgresql' y postgresql-server')

~~~sql
apt-get install postgresql-12
~~~

2. 

### Instalación desde el paquete oficial

### Instalación desde el código fuente

## Comandos básicos

### Programa de terminal interactivo 'PSQL'

Este comando es necesario para interactuar con las bases de datos SQL.

El programa 'psql' tiene varios comandos internos que no son comandos SQL. Todos comienzan con la barra invertida '\'.

#### Activar base de datos

>:warning: si no se proporciona un nombre para la base de datos, se establece por defecto el nombre del usuario como nombre de la base de datos.

~~~sql
psql nuriadb
~~~


~~~sql
nuriadb=> \h
~~~

~~~sql
nuriadb=> \q
~~~

~~~sql
nuriadb=> SELECT version();
~~~

### Programa de interfaz gráfica 'PgAdmin'

También existe la posibilidad, al igual que en MYSQL, de instalar la herramienta gráfica PgAdmin. Esta herramienta nos permite interactuar con las bases de datos sin tener que escribir los comandos. 
