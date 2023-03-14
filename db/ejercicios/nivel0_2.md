# Ejercicio 2 (nivel básico)
1. Crear una tabla "Productos" con las columnas "ID", "Nombre", "Precio" y "Cantidad".
Solución:
    ~~~~
    CREATE TABLE Productos (
    ID INT,
    Nombre VARCHAR(50),
    Precio DECIMAL(10,2),
    Cantidad INT
    );
    ~~~~
2. Insertar tres nuevos productos en la tabla "Productos".
Solución:
    ~~~~
    INSERT INTO Productos (ID, Nombre, Precio, Cantidad) 
    VALUES 
    (1, 'Camiseta', 19.99, 50),
    (2, 'Pantalón', 29.99, 30),
    (3, 'Zapatos', 49.99, 20);
    ~~~~
3. Actualizar el precio del producto con ID=2 a 39.99.
Solución:
``UPDATE Productos SET Precio=39.99 WHERE ID=2;``
4. Ejercicio: Eliminar el producto con ID=3 de la tabla "Productos".
Solución:
``DELETE FROM Productos WHERE ID=3;``
5. Ejercicio:  Seleccionar el nombre y el precio de los productos de la tabla "Productos" cuyo precio sea mayor a 20.
Solución:
``SELECT Nombre, Precio FROM Productos WHERE Precio > 20;``