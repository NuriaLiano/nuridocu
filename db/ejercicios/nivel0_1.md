#Ejercicio 1 (nivel básico)
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