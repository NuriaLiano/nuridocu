---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Repaso Inicial de nivel

## 1. Crear la base de datos 'videojuegos'

**CONECTARSE A LA BASE DE DATOS**

## 2. Crear tabla 'juegos' con los siguientes campos

- id SERIAL PRIMARY KEY,
- titulo VARCHAR(100) NOT NULL,
- plataforma VARCHAR (50) NOT NULL,
- lanzamiento DATE NOT NULL,
- desarrollador VARCHAR (100),
- rating FLOAT

## 3. Insertar datos

- ('The Legend of Zelda: Breath of the Wild', 'Nintendo Switch', 'Acción-aventura', '2017-03-03', 'Nintendo EPD', 4.9),
- ('Super Mario Odyssey', 'Nintendo Switch', 'Plataformas', '2017-10-27', 'Nintendo EPD', 4.8),
- ('God of War', 'PlayStation 4', 'Acción-aventura', '2018-04-20', 'SIE Santa Monica Studio', 4.7),
- ('The Last of Us Part II', 'PlayStation 4', 'Acción-aventura', '2020-06-19', 'Naughty Dog', 4.6),
- ('Red Dead Redemption 2', 'PlayStation 4', 'Acción-aventura', '2018-10-26', 'Rockstar Studios', 4.5),
- ('Dark Souls III', 'PlayStation 4', 'Acción-RPG', '2016-04-12', 'FromSoftware', 4.4),
- ('Hades', 'PC', 'Roguelike', '2020-09-17', 'Supergiant Games', 4.9);

## 4. Añade una nueva columna llamada "precio" a la tabla "juegos" con el tipo de datos 'DECIMAL(10,2)'

## 5. Crea una nueva tabla llamada "plataformas" con los siguientes campos

- id
- nombre
- fabricante

## 6. Inserta algunos datos en la tabla 'plataformas'

- ('Nintendo Switch', 'Nintendo'),
- ('PlayStation 4', 'Sony Interactive Entertainment'),
- ('PC', NULL);

## 7. Añade una nueva columna llamada 'plataforma_id' a la tabla de 'juegos' con el tipo de datos 'int'

## 8. Actualiza la columna 'plataforma_id' con el id correspondiente de la tabla 'plataformas'

## 9. Cambia el campo 'rating' para que permita valores negativos

## 10. Añade la clave foráea para crear la relación entre las tablas

## 11. Seleccionar todos los juegos con un rating mayor o igual a 4.5

## 12. Seleccionar todos los titulos de juegos que se lanzaron antes de 2019

## 13. Seleccionar el promedio de rating de os juegos lanzados en Playstation 4

## 14. Seleccionar el número de juegos por plataforma, solo incluyendo plataformas con  más de un juego

## 15. Seleccionar el desarrollador y el promedio de rating de los juegos que tienen un rating mayor o igula a 4.5, ordenados por rating promedio de forma descendente

## 16. Selecciona los títulos de los juegos que se lanzaron en 2018 o después, limitado a 3 resultados

## 17. Exportar los datos de la tabla 'juegos' a un archivo CSV sen el directorio 'home' del usuario actual

## 18. Seleccionar todos los juegos junto con el nombre de la plataforma

## 19. Seleccionar los nombres de los desarrolladores y la cantidad de juegos que han creado solo incluyendo desarrolladores con más de un juego

## 20. Seleccionar los títulos de los juegos lanzados por Playstation 4 que tienen un ratin mayor o igual a la media de rating de todos los juegos

## 21. Seleccionar los nombres de las plataformas que tienen al menos un juego con un rating mayor o igual a 4.8 y lo snombres de los desarrolladores que han creado ese juego

## 23. Inserta los juegos lanzados después del 2018 en una tabla llamada 'juegos_mas_nuevos' siguiendo la misma estructura de la tabla 'juegos'

## 24. Cambia el desarrollador por 'Bandai Namco Entertainment' del juego 'Dark Souls III'

## 25. Actualizar el 'rating' de todos los juegos que hayan sido desarrollados por 'Nintendo EPD' y tengan un ratin menor a 4.8

## 26. Crea una vista que muestre información de los juegos desarrollados por 'Naughty Dog' y 'SIE Santa Monica Studio' junto con la información de la plataforma en la que estén disponibles

## 27. Elimina la tabla 'plataformas

## 28. Elimina el registro 'The Last of Us Part II'

## 29. Eliminar la base de datos 'videojuegos'

