---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Ejercicios de repaso manejando bases de datos, tablas, vistas, relaciones, restricciones y datos

## 1. Crea la base de datos

## 2. Conéctate a la base de datos

## 3. Crea la tabla 'PERSONAJES'

id_personaje (INTEGER PRIMARY KEY),
nombre (VARCHAR(50)),
apellido (VARCHAR(50)),
edad (INTEGER),
genero (VARCHAR(10)),
nacionalidad (VARCHAR(50)),
banda (VARCHAR(50))

## 4. Inserta los siguientes registros en la tabla 'PERSONAJES'

(1, 'Carl', 'Johnson', 29, 'Masculino', 'Estados Unidos', 'Grove Street Families'),
(2, 'Franklin', 'Clinton', 25, 'Masculino', 'Estados Unidos', 'Los Santos'),
(3, 'Michael', 'De Santa', 45, 'Masculino', 'Estados Unidos', 'FIB'),
(4, 'Trevor', 'Philips', 48, 'Masculino', 'Canadá', 'Trevor Philips Enterprises')

## 5. Crear la tabla 'JUEGOS'

id_juego (INTEGER PRIMARY KEY),
titulo (VARCHAR(50)),
fecha_lanzamiento (DATE),
plataforma (VARCHAR(20)),
desarrolladora (VARCHAR(50))

## 6. Inserta los siguientes registros en la tabla 'JUEGOS'

(1, 'Grand Theft Auto III', '2001-10-22', 'PlayStation 2', 'Rockstar North'),
(2, 'Grand Theft Auto: San Andreas', '2004-10-26', 'PlayStation 2', 'Rockstar North'),
(3, 'Grand Theft Auto IV', '2008-04-29', 'PlayStation 3', 'Rockstar North'),
(4, 'Grand Theft Auto V', '2013-09-17', 'PlayStation 4', 'Rockstar North');

## 7. Añade la clave primaria donde creas que falta

## 8. Añade la clave foránea en la tabla 'PERSONAJES'

## 9. Añade una restricción a la tabla 'JUEGOS' para que no se puedan insertar juegos con el mismo título

## 10. Añade una restricción a la tabla 'PERSONAJES' para que sólo se puedan insertar edades mayores de 18 años

## 11. Añade una restricción a la tabla 'PERSONAJES' para que no se puedan insertar valores nulos

## 12. Inserta estos valores en la tabla 'JUEGOS' y explica que ocurre

('Grand Theft Auto V', 'PC', '2013-09-17'),
('Grand Theft Auto IV', 'Xbox 360', '2008-04-29'),
('Grand Theft Auto V', 'PlayStation 3', '2013-09-17')

## 13. Muestra los registros de la tabla 'PERSONAJES' que sean de la banda 'Grove Street Families' y la nacionalidad sea 'Estados Unidos'

## 14. Muestra el número de personajes de cada banda

## 15. Muestra las bandas con más de 2 personajes

## 16. Muestra el número de personajes den cada juego que son de nacionalidad estadounidense

## 17. Muestra los nombres de los personajes y el título del juego correspondiente en el que aparecen en una vista llamada 'personajes_juegos'

## 18. Consulta la vista creada

## 19. Actualiza el título del juego a 'Grand Theft Auto: San Andreas' en la vista 'personajes_juegos' para el personaje 'CJ'

## 20. Elimina la vista 'personajes_juegos'

## 21. Elimina la vista 'personajes_juegos'

## 22. Devuelve los nombres de los personajes que pertenecen a las bandas "Ballers" o "Grove Street Families", y los nombres de los personajes que pertenecen a las bandas "Vagos" o "Aztecas". Los resultados de ambas consultas se combinan y se eliminan los duplicados

## 23. Devuelve los nombres de los personajes que pertenecen a la banda "Ballers" y que son de nacionalidad mexicana

## 24. Devuelve los nombres de los personajes que pertenecen a la banda "Grove Street Families" y que no son de nacionalidad estadounidense

## 25. Es lo mismo 'UNION', 'INTERSECT' y 'EXCEPT' que 'AND', 'OR' y 'NOT'?

## 26. Elimina la restricción para evitar que se puedan introducir títulos duplicados

>:warning: **ADVENTENCIA** Recuerda que al eliminar una restricción se permitirá insertar registros que antes no estaban permitidos. Por lo tanto, debes evaluar cuidadosamente si la restricción es necesaria antes de eliminarla.

## 27. Elimina la restricción de edad

>:warning: **ADVENTENCIA** Recuerda que al eliminar una restricción se permitirá insertar registros que antes no estaban permitidos. Por lo tanto, debes evaluar cuidadosamente si la restricción es necesaria antes de eliminarla.