---
author: @nurialiano
license: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# Ejercicio 1 (nivel básico)
1. Crear una tabla "Estudiantes" con las columnas "ID", "Nombre", "Edad" y "Correo electrónico".
Solución:
    ~~~~
    CREATE TABLE Estudiantes (
        ID INT,
        Nombre VARCHAR(50),
        Edad INT,
        Correo_electronico VARCHAR(50)
    );
    ~~~~
2. Insertar un nuevo estudiante en la tabla "Estudiantes" con ID=1, Nombre="Juan", Edad=20 y Correo electrónico="juan@example.com".
Solución:
``INSERT INTO Estudiantes (ID, Nombre, Edad, Correo_electronico) VALUES (1, 'Juan', 20, 'juan@example.com');``
3. Actualizar la edad del estudiante con ID=1 a 21 años.
Solución:
``UPDATE Estudiantes SET Edad=21 WHERE ID=1;``
4. Eliminar el estudiante con ID=1 de la tabla "Estudiantes".
Solución:
``DELETE FROM Estudiantes WHERE ID=1;``
5. Seleccionar todos los estudiantes de la tabla "Estudiantes" cuya edad sea mayor a 18 años.
Solución:
``SELECT * FROM Estudiantes WHERE Edad > 18;``

# Ejercicio 2 (nivel básico)
1. Crear una tabla "Productos" con las columnas "ID", "Nombre", "Precio" y "Cantidad".
Solución:
~~~sql
    CREATE TABLE Productos (
    ID INT,
    Nombre VARCHAR(50),
    Precio DECIMAL(10,2),
    Cantidad INT
    );
~~~
2. Insertar tres nuevos productos en la tabla "Productos".
Solución:
~~~sql
    INSERT INTO Productos (ID, Nombre, Precio, Cantidad) 
    VALUES 
    (1, 'Camiseta', 19.99, 50),
    (2, 'Pantalón', 29.99, 30),
    (3, 'Zapatos', 49.99, 20);
~~~
3. Actualizar el precio del producto con ID=2 a 39.99.
Solución:
``UPDATE Productos SET Precio=39.99 WHERE ID=2;``
4. Ejercicio: Eliminar el producto con ID=3 de la tabla "Productos".
Solución:
``DELETE FROM Productos WHERE ID=3;``
5. Ejercicio:  Seleccionar el nombre y el precio de los productos de la tabla "Productos" cuyo precio sea mayor a 20.
Solución:
``SELECT Nombre, Precio FROM Productos WHERE Precio > 20;``