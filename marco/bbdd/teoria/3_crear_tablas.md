---
autor: @nurialiano
licence: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# CREACIÓN DE TABLAS

## Aspectos importantes y recomendaciones

1. **Definir el nombre de la tabla**
   1. Nombre significativo y descriptivo
   2. Nombre en singular
   3. Evitar espacios o caracteres especiales
   4. No utilizar números
2. **Especificar las columnas y los tipos de datos**: Cada columna de la tabla debe tener un nombre y un tipo de dato asociado
3. **Definir las restricciones**: Las restricciones son reglas que limitan los valores que se pueden ingresar en una columna, por ejemplo, una restricción de clave primaria asegura que cada fila tenga un valor único en esa columna.
4. **Establecer las relaciones entre las tablas**: Si se tienen varias tablas en la base de datos, es importante establecer relaciones entre ellas para poder acceder a la información de manera eficiente. Las relaciones se definen mediante claves foráneas que apuntan a la clave primaria de otra tabla.
5. **Crear índices**: Los índices son estructuras de datos que permiten acceder a la información de manera más rápida. Se recomienda crear índices en las columnas que se utilizan con frecuencia en las consultas.

Es importante tener en cuenta algunos **aspectos adicionales**, como la **definición de valores predeterminados**, **las opciones de autoincremento para las claves primarias** y la **configuración de la codificación** de caracteres para admitir diferentes idiomas y conjuntos de caracteres.

## Ejemplo

~~~sql
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    fecha_nacimiento DATE
);
~~~

En este ejemplo, hemos definido el nombre de la tabla como "clientes". Además, hemos especificado las columnas "id" (que es la clave primaria de la tabla), "nombre", "apellido", "email" y "fecha_nacimiento", cada una con su respectivo tipo de dato.

También hemos establecido algunas restricciones: la columna "id" es la clave primaria de la tabla y, por lo tanto, no puede tener valores duplicados; la columna "email" tiene la restricción UNIQUE para asegurarnos de que cada email sea único en la tabla.