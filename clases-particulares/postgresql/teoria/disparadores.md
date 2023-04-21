---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Disparadores (triggers)

Son una funcionalidad de PostgreSQL que permiten ejecutar automáticamente una acción en respuesta a ciertos eventos, como por ejemplo la inserción, actualización o eliminación de filas en una tabla.

Estos eventos pueden ser desencadenados por una operación realizada en una tabla específica, en cuyo caso se habla de disparadores de tabla, o bien por una operación realizada en cualquier tabla de una base de datos, en cuyo caso se habla de disparadores de base de datos.

Se pueden utilizar para:

- Enviar notificaciones o alertas en respuesta a cambios en una tabla.
- Validar la integridad de los datos en una tabla antes de permitir una inserción o actualización.
- Actualizar automáticamente los valores de una tabla en función de los cambios realizados en otras tablas.
- Realizar auditorías de cambios en una tabla, registrando información sobre quién realizó el cambio y cuándo.
- Mantener registros históricos de los cambios realizados en una tabla.
- Implementar restricciones de seguridad adicionales, como por ejemplo evitar la eliminación de filas en ciertas tablas.

>:pencil: **NOTA**  los disparadores son una herramienta muy útil y versátil para implementar la lógica de negocio de una aplicación de base de datos de forma automática y transparente.

## Tipos de disparadores

### Disparadores de fila (row-level triggers)

Se ejecutan una vez por cada fila afectada por una operación DML (insertar, actualizar o eliminar). Se pueden utilizar para realizar validaciones o acciones en función de los valores de las columnas de la fila afectada.

### Disparadores de sentencia (statement-level triggers)

Se ejecutan una sola vez por cada operación DML, independientemente del número de filas afectadas. Se utilizan para realizar acciones que afectan a varias filas, como actualizar una columna en todas las filas que cumplen una determinada condición.


