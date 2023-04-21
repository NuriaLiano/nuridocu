---
author: @nurialiano
license: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

    Crea una tabla llamada "Empleados" con los siguientes campos: "ID", "Nombre", "Apellido", "Departamento" y "Fecha de contratación".

sql

CREATE TABLE Empleados (
ID INT PRIMARY KEY,
Nombre VARCHAR(50),
Apellido VARCHAR(50),
Departamento VARCHAR(50),
FechaContratacion DATE
);

    Inserta 5 filas de datos en la tabla "Empleados".

sql

INSERT INTO Empleados (ID, Nombre, Apellido, Departamento, FechaContratacion) VALUES
(1, 'Juan', 'Pérez', 'Marketing', '2018-05-01'),
(2, 'María', 'Gómez', 'Ventas', '2017-03-15'),
(3, 'Pedro', 'Sánchez', 'Recursos Humanos', '2016-07-01'),
(4, 'Laura', 'García', 'Contabilidad', '2019-01-10'),
(5, 'Ana', 'Rodríguez', 'Tecnología', '2020-02-25');

    Crea una tabla llamada "Proyectos" con los siguientes campos: "ID", "Nombre" y "Fecha de inicio".

sql

CREATE TABLE Proyectos (
ID INT PRIMARY KEY,
Nombre VARCHAR(50),
FechaInicio DATE
);

    Inserta 3 filas de datos en la tabla "Proyectos".

sql

INSERT INTO Proyectos (ID, Nombre, FechaInicio) VALUES
(1, 'Proyecto A', '2019-01-01'),
(2, 'Proyecto B', '2020-02-01'),
(3, 'Proyecto C', '2021-03-01');

    Crea una tabla llamada "Asignaciones" con los siguientes campos: "ID_Empleado", "ID_Proyecto" y "Horas".

sql

CREATE TABLE Asignaciones (
ID_Empleado INT,
ID_Proyecto INT,
Horas INT,
PRIMARY KEY (ID_Empleado, ID_Proyecto),
FOREIGN KEY (ID_Empleado) REFERENCES Empleados(ID),
FOREIGN KEY (ID_Proyecto) REFERENCES Proyectos(ID)
);

    Inserta 4 filas de datos en la tabla "Asignaciones".

scss

INSERT INTO Asignaciones (ID_Empleado, ID_Proyecto, Horas) VALUES
(1, 1, 10),
(1, 2, 5),
(2, 1, 7),
(3, 3, 12);

    Actualiza el nombre del proyecto con ID 2 a "Proyecto D".

sql

UPDATE Proyectos SET Nombre = 'Proyecto D' WHERE ID = 2;

    Elimina la asignación del empleado con ID 2 al proyecto con ID 1.

sql

DELETE FROM Asignaciones WHERE ID_Empleado = 2 AND ID_Proyecto = 1;

    Selecciona los empleados que trabajan en más de un proyecto.

sql

SELECT Empleados.Nombre, COUNT(*) AS NumeroProyectos FROM Empleados
JOIN Asignaciones ON Empleados.ID = Asignaciones.ID_Empleado
GROUP BY Empleados.ID
HAVING COUNT(*) > 1;

    Selecciona los proyectos en los que trabajan más de 2 empleados y muestra el nombre del proyecto, el nombre del departamento y el número de empleados asignados a cada proyecto.

sql

SELECT Proyectos.Nombre AS Proyecto, Empleados.Departamento, COUNT(*) AS NumeroEmpleados FROM Proyectos
JOIN Asignaciones ON Proyectos.ID = Asignaciones.ID_Proyecto
JOIN Empleados ON Asignaciones.ID_Empleado = Empleados.ID
GROUP BY Proyectos.ID, Empleados.Departamento
HAVING COUNT(*) > 2;
