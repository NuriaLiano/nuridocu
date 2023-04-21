---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---


## EJERCICIO 1

1. Crea una tabla llamada "Clientes" con los siguientes campos: "ID", "Nombre", "Apellido", "Dirección" y "Teléfono".

~~~sql

    CREATE TABLE Clientes (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Direccion VARCHAR(100),
    Telefono VARCHAR(20)
    );
~~~

2. Inserta 3 filas de datos en la tabla "Clientes".

~~~sql
    INSERT INTO Clientes (ID, Nombre, Apellido, Direccion, Telefono) VALUES
    (1, 'Juan', 'Pérez', 'Calle Falsa 123', '555-1234'),
    (2, 'María', 'Gómez', 'Avenida Siempreviva 742', '555-5678'),
    (3, 'Pedro', 'Sánchez', 'Calle Mayor 5', '555-4321');
~~~

## EJERCICIO 2

1. Crea una tabla llamada "Productos" con los siguientes campos: "ID", "Nombre", "Precio" y "Cantidad".

~~~
CREATE TABLE Productos (
ID INT PRIMARY KEY,
Nombre VARCHAR(50),
Precio DECIMAL(10,2),
Cantidad INT
);
~~~
2. Inserta 4 filas de datos en la tabla "Productos".

~~~
INSERT INTO Productos (ID, Nombre, Precio, Cantidad) VALUES
(1, 'Leche', 1.50, 10),
(2, 'Pan', 0.75, 20),
(3, 'Coca-Cola', 2.00, 5),
(4, 'Café', 3.00, 8);
~~~
6. Crea una tabla llamada "Pedidos" con los siguientes campos: "ID", "ID_Cliente", "ID_Producto" y "Cantidad".

~~~
CREATE TABLE Pedidos (
ID INT PRIMARY KEY,
ID_Cliente INT,
ID_Producto INT,
Cantidad INT,
FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID),
FOREIGN KEY (ID_Producto) REFERENCES Productos(ID)
);
~~~
7. Inserta 2 filas de datos en la tabla "Pedidos".

~~~
INSERT INTO Pedidos (ID, ID_Cliente, ID_Producto, Cantidad) VALUES
(1, 1, 1, 3),
(2, 2, 4, 2);
~~~
8. Actualiza el precio del producto "Coca-Cola" a 2.50.

~~~
UPDATE Productos SET Precio = 2.50 WHERE Nombre = 'Coca-Cola';
~~~
9. Elimina el producto "Pan" de la tabla "Productos".

~~~
DELETE FROM Productos WHERE Nombre = 'Pan';
~~~
10. Selecciona todos los pedidos realizados por el cliente con ID 1.

~~~
SELECT * FROM Pedidos WHERE ID_Cliente = 1;
~~~
11. Selecciona todos los productos que tengan una cantidad menor a 10.

~~~
SELECT * FROM Productos WHERE Cantidad < 10;
~~~
