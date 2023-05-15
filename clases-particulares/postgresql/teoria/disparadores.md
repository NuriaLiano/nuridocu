---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Disparadores (triggers)

En PostgreSQL, los "triggers" o "disparadores" son objetos que te permiten definir acciones automáticas que se ejecutan en respuesta a ciertos eventos en una tabla específica. Estos eventos pueden ser operaciones de inserción (INSERT), actualización (UPDATE) o eliminación (DELETE) en la tabla.

Un trigger consta de dos partes principales: un evento que desencadena la ejecución del trigger y una función que se ejecuta en respuesta al evento. Cuando ocurre el evento especificado, PostgreSQL ejecuta la función del trigger.

TODO:<!--IMAGEN DESCRIPTIVA DE LA PARTES DE UN TRIGGER-->

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

Estos triggers se ejecutan para cada fila afectada por la operación que desencadenó el evento. Pueden ser configurados para ejecutarse "antes" (BEFORE) o "después" (AFTER) de la operación que disparó el trigger. Los triggers a nivel de fila se definen para una tabla específica y pueden acceder y modificar los datos de la fila actual.

Por ejemplo:
Supongamos que tienes una tabla llamada "empleados" con las columnas "nombre", "salario" y "salario_anterior". Quieres mantener actualizado el valor de la columna "salario_anterior" cada vez que se actualice el salario de un empleado.

~~~sql
-- Crear la tabla de ejemplo
CREATE TABLE empleados (
  nombre VARCHAR(50),
  salario NUMERIC(10,2),
  salario_anterior NUMERIC(10,2)
);

-- Crear el trigger a nivel de fila
CREATE OR REPLACE FUNCTION actualizar_salario_anterior()
  RETURNS TRIGGER AS $$
BEGIN
  NEW.salario_anterior := OLD.salario; -- Actualizar el valor de salario_anterior
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Asociar el trigger al evento UPDATE en la tabla empleados
CREATE TRIGGER trigger_actualizar_salario_anterior
BEFORE UPDATE ON empleados
FOR EACH ROW
EXECUTE FUNCTION actualizar_salario_anterior();
~~~

### Disparadores de sentencia (statement-level triggers)

Estos triggers se ejecutan una vez por sentencia SQL, independientemente del número de filas afectadas por la sentencia. Los triggers a nivel de sentencia también se pueden configurar para ejecutarse "antes" o "después" de la operación que desencadenó el evento. A diferencia de los triggers a nivel de fila, los triggers a nivel de sentencia no tienen acceso directo a los datos de la tabla. Sin embargo, pueden ejecutar consultas adicionales basadas en la operación realizada.

Por ejemplo:
Supongamos que tienes una tabla llamada "pedidos" con las columnas "id_pedido", "fecha", "estado" y "total". Quieres realizar una auditoría que registre cada vez que se inserte, actualice o elimine un pedido en la tabla.

~~~sql
-- Crear la tabla de auditoría
CREATE TABLE auditoria_pedidos (
  id_audit SERIAL PRIMARY KEY,
  fecha_audit TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  accion VARCHAR(10),
  id_pedido INT,
  detalle TEXT
);

-- Crear el trigger a nivel de sentencia
CREATE OR REPLACE FUNCTION auditar_pedidos()
  RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    INSERT INTO auditoria_pedidos (accion, id_pedido, detalle)
    VALUES ('INSERT', NEW.id_pedido, 'Nuevo pedido insertado');
  ELSIF TG_OP = 'UPDATE' THEN
    INSERT INTO auditoria_pedidos (accion, id_pedido, detalle)
    VALUES ('UPDATE', OLD.id_pedido, 'Pedido actualizado');
  ELSIF TG_OP = 'DELETE' THEN
    INSERT INTO auditoria_pedidos (accion, id_pedido, detalle)
    VALUES ('DELETE', OLD.id_pedido, 'Pedido eliminado');
  END IF;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Asociar el trigger al evento INSERT, UPDATE y DELETE en la tabla pedidos
CREATE TRIGGER trigger_auditar_pedidos
AFTER INSERT OR UPDATE OR DELETE ON pedidos
EXECUTE FUNCTION auditar_pedidos();
~~~

## Crear disparadores

### Sintaxis básica

~~~sql
CREATE [CONSTRAINT] TRIGGER nombre_trigger
{BEFORE | AFTER | INSTEAD OF} {evento} ON nombre_tabla
[REFERENCING {OLD | NEW} {ROW | TABLE} [AS] alias]
[FOR EACH {ROW | STATEMENT}]
[WHEN (condición)]
EXECUTE FUNCTION nombre_función_trigger();
~~~

## Borrar disparadores

## Modificar disparadores

## Deshabilitar uno o varios disparadores asociados a una tabla

## Habilitar uno o varios disparadores asociados a una tabla