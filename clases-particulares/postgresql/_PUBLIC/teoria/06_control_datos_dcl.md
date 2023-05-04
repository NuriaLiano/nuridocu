---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Definición de datos 'DCL'

DCL significa "Data Control Language" (Lenguaje de Control de Datos ) en SQL. Se utiliza para otorgar y revocar permisos a usuarios y roles en una base de datos

## Comandos comunes de DCL

- **GRANT**: se utiliza para otorgar permisos a un usuario o rol para realizar operaciones específicas en una base de datos o en objetos específicos de una base de datos.
- **REVOKE**: se utiliza para revocar los permisos concedidos previamente a un usuario o rol en una base de datos o en objetos específicos de una base de datos.

>:pencil: **NOTA** También puedes combinar varios permisos en una sola instrucción de GRANT o REVOKE.
> ej: Por ejemplo, para otorgar permisos SELECT, INSERT y UPDATE en la tabla "ventas" a un usuario llamado "usuario3"
> ``GRANT SELECT, INSERT, UPDATE ON ventas TO usuario3;``

### Ejemplo GRANT

Por ejemplo, si quieres otorgar permisos SELECT a un usuario llamado "usuario1"

~~~sql
GRANT SELECT ON nombre_tabla TO usuario1;
~~~

### Ejemplo REVOKE

Por ejemplo, si quieres revocar el permiso SELECT previamente concedido a un usuario llamado "usuario1"

~~~sql
REVOKE SELECT ON nombre_tabla FROM usuario1;
~~~
