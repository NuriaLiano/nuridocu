---
author: @nurialiano
license: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# Variables de usuario

Variables que pueden ser definidas por el usuario y utilizadas en las consultas y sentencias de control. Estas variables comienzan con el prefijo "@@", que las diferencia de las variables de sistema que comienzan con el prefijo "@". Las variables de usuario se utilizan en MySQL para realizar tareas como el almacenamiento de valores que se utilizarán en múltiples sentencias, la simplificación de expresiones de consulta y el seguimiento de información de estado.

## Aspectos importantes

1. **Declaración**: se utiliza la sintaxis "@variable_nombre". Por ejemplo, si se desea definir una variable de usuario llamada "id_cliente", se puede hacer de la siguiente manera: "@id_cliente".
2. **Asignación**: se utiliza la sintaxis "SET @variable_nombre = valor". Por ejemplo, si se desea asignar el valor 1 a la variable de usuario "id_cliente", se puede hacer de la siguiente manera: "SET @id_cliente = 1".
3. **Uso**: puede ser utilizada en consultas y sentencias de control. Por ejemplo, se puede utilizar la variable de usuario "id_cliente" en una consulta para obtener información de un cliente específico: "SELECT * FROM clientes WHERE id = @id_cliente".
4. **Alcance**: las variables de usuario son válidas en la sesión actual de MySQL y se pierden al finalizar la sesión. Si se desea utilizar la variable de usuario en diferentes sesiones, se debe volver a definir y asignar la variable en cada sesión.

## Ejemplo

Supongamos que tienes una tabla "pedidos" con las siguientes columnas: "id_pedido", "id_cliente", "fecha" y "total". Además, quieres obtener la información de los pedidos de un cliente específico y guardar el id del cliente en una variable de usuario para usarla posteriormente en otra consulta.

~~~sql
-- Definir variable de usuario
SET @id_cliente = 1;

-- Obtener información de los pedidos del cliente con id = @id_cliente
SELECT id_pedido, fecha, total
FROM pedidos
WHERE id_cliente = @id_cliente;
~~~

En este ejemplo, se define la variable de usuario "@id_cliente" y se le asigna el valor 1. Luego, se utiliza esta variable en la consulta para obtener la información de los pedidos del cliente con el id almacenado en la variable. De esta manera, se puede cambiar el valor de la variable de usuario en cualquier momento para obtener la información de los pedidos de un cliente diferente sin tener que cambiar el código de la consulta.
