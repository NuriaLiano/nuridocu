---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---
# Solución examen 'Creación de tablas'

Dado el esquema de las tablas de una base de datos que gestiona los pubs de una comarca, es necesario crear las tablas con las especificaciones que se indican a continuación. (3 puntos)

## PUB

| Tipus | Null | Primary Key |
| -     |  -   |   -         |
COD_PUB | Numèric | No | Si
NOMBRE | Alfabètic 60 | No
LICENCIA_FISCAL | Alfabètic  60 | No
DOMICILIO | Alfabètic 60 | Si
FECHA_APERTURA | Fecha | No
HORARIO | Alfabètic  60 | No
COD_LOCALIDAD | Numèric | No

COD_LOCALIDAD una llave foránea en la tabla LOCALIDAD en caso de Borrar --> R, Modificar --> P.

~~~sql
CREATE TABLE pub(
cod_pub INTEGER NOT NULL,
nombre VARCHAR(60) NOT NULL,
licencia_fiscal VARCHAR(60) NOT NULL,
domicilio VARCHAR(60)  NULL,
fecha_apertura DATE NOT NULL,
horario VARCHAR(60) NOT NULL,
cod_localidad INTEGER NOT NULL,
CONSTRAINT cp_pub PRIMARY KEY(cod_pub),
CONSTRAINT fk_pub FOREIGN KEY (cod_localidad) REFERENCES localidad
ON DELETE RESTRICT ON UPDATE CASCADE
);
~~~

## TITULAR

| Tipus | Null | Primary Key |
| -     |  -   |   -         |
DNI_TITULAR | Alfabètic 9 | No | Si
NOMBRE | Alfabètic  60 | No
DOMICILIO | Alfabètic  60 | Si
COD_PUB | Numèric | No | Si

COD_PUB una clave foránea en la tabla PUB en caso de Borrado --> P, Modificar --> P.

~~~sql
CREATE TABLE titular(
dni_titular VARCHAR(9) NOT NULL,
nombre VARCHAR(60) NOT NULL,
domicilio VARCHAR(60) NULL,
cod_pub INTEGER NOT NULL,
CONSTRAINT cp_titular PRIMARY KEY (dni_titular,cod_pub),
CONSTRAINT fk_titular FOREIGN KEY (cod_pub) REFERENCES pub
ON DELETE CASCADE ON UPDATE CASCADE
);
~~~

## EMPLEADO

| Tipus | Null | Primary Key |
| -     |  -   |   -         |
DNI_EMPLEADO | Alfabètic 9 | No | Si
NOMBRE | Alfabètic  60 | No
DOMICILIO | Alfabètic 60 | Si

~~~sql
CREATE TABLE empleado(
dni_empleado VARCHAR(9) NOT NULL,
nombre VARCHAR(60) NOT NULL,
domicilio VARCHAR(60) NULL,
CONSTRAINT cp_empleado PRIMARY KEY (dni_empleado)
);
~~~

## EXISTENCIAS

| Tipus | Null | Primary Key |
| -     |  -   |   -         |
COD_ARTICUL | ONumèric | No | i
NOMBRE | Alfabètic  60 | No
CANTIDAD | Numèric | No
PRECIO | Decimal | No
COD_PUB | Numèric | No | Si

COD_PUB una clave foránea en la tabla PUB en caso de Borrado --> P, Modificar --> P.
El campo Cantidad no puede ser negativo.

~~~sql
CREATE TABLE existencias(
cod_articulo INTEGER NOT NULL,
nombre VARCHAR(60) NOT NULL,
cantidad INTEGER NOT NULL,
precio DECIMAL NOT NULL,
cod_pub INTEGER NOT NULL,
CONSTRAINT cp_existencias PRIMARY KEY (cod_articulo,cod_pub),
CONSTRAINT fk_existencias FOREIGN KEY (cod_pub) REFERENCES pub
ON DELETE CASCADE ON UPDATE CASCADE
);
~~~

## LOCALIDAD

| Tipus | Null | Primary Key |
| -     |  -   |   -         |
|COD_LOCALIDAD | Numèric | No | Si
NOMBRE | Alfabètic  60 | No

~~~sql
CREATE TABLE localidad(
cod_localidad INTEGER NOT NULL,
nombre VARCHAR(60) NOT NULL,
CONSTRAINT cp_localidad PRIMARY KEY (cod_localidad)
);
~~~

## PUB_EMPLEADO

| Tipus | Null | Primary Key |
| -     |  -   |   -         |
COD_PUB | Numèric | No | Si
DNI_EMPLEADO | Alfabètic 9 | No | Si
FUNCION | Alfabètic 9 | No | Si

COD_PUB una clave foránea en la tabla PUB en caso de Borrado --> P, Modificar --> P.
DNI_EMPLEADO una llave foránea en la tabla EMPLEADO en caso de Borrado --> R, Modificar --> P.

~~~sql
CREATE TABLE pub_empleado(
cod_pub INTEGER NOT NULL,
dni_empleado VARCHAR(9) NOT NULL,
funcion VARCHAR (9) NOT NULL,
CONSTRAINT cp_pub_empleado PRIMARY KEY (cod_pub,dni_empleado,funcion),
CONSTRAINT fk_pub_empleado FOREIGN KEY (cod_pub) REFERENCES pub
ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT fk_pub_empleado2 FOREIGN KEY (dni_empleado) REFERENCES empleado
ON DELETE RESTRICT ON UPDATE CASCADE
);
~~~

Hay que tener en cuenta las siguientes consideraciones:

## 1.  El campo horario de la tabla PUB sólo puede tomar los valores HOR1,HOR2 y HOR3 (0,5 puntos)

~~~sql
alter table pub add constraint CK_pub_horario check (horario='HOR1' or horario='HOR2' or horario='HOR3');
~~~

## 2. No es posible tener en la tabla EXISTENCIAS algún artículo con precio 0 o negativo, ya que significaría que regalamos el artículo y esto no es posible en un negocio. (0,5 puntos)

~~~sql
alter table existencias add constraint CK_existencias_precio check (precio>0);
~~~

## 3. El campo "fecha_apertura" de la tabla PUB debe tener una fecha anterior al día actual. (0,5 puntos)

~~~sql
alter table pub add constraint CK_pub_fecha_apertura check (fecha_apertura<CURRENT_TIMESTAMP);
~~~

## 4. Las funciones que puede realizar un empleado son sólo: «LIMPIEZA, CAMARERO, SEGURIDAD». Debe reflejarlo en la tabla «PUB_EMPLEADO» (0,5 puntos)

~~~sql
alter table pub_empleado add constraint CK_pub_empleado_funcion check (funcion='LIMPIEZA' or funcion='CAMARERO' or funcion='SEGURIDAD');
~~~

## 5. Hoy el Servicio Joven del ayuntamiento de Badia con licencia fiscal cervecería ha abierto un nuevo Pub con nombre SJBadia en la carretera de Sabadell S/N de Matadepera y habrá que guardarlo en la base de datos. Trabajarán los alumnos de nuestro centro Daniel Bouacha Sánchez y Daniel Pinyol Sánchez, que se hacen llamar los DANIS, los dos serán camareros, en horario HOR2. El titular del Pub será otro Dani, concretamente Daniel Garcia Vila. (1 puntos)

~~~sql
insert into titular values ((select dni_titular from titular where nombre like 'Daniel Garcia Vila'), 'Daniel Garcia Vila', (select domicilio from titular where nombre like 'Daniel Garcia Vila'), (select cod_pub from pub where nombre like 'SJBadia'));
insert into pub_empleado values ((select cod_pub from pub where nombre like 'SJBadia'), '01321911D', 'CAMARERO');
insert into pub_empleado values ((select cod_pub from pub where nombre like 'SJBadia'), '49476674V', 'CAMARERO');
~~~

## 6. Añade a la tabla EMPLEADO la fecha en que los empleados han sido contratados. (1 puntos)

~~~sql
alter table empleado add fecha_contrato date;
update empleado set fecha_contrato='08/03/2021' where dni_empleado='01321911D';
update empleado set fecha_contrato='08/03/2021' where dni_empleado='49476674V';
~~~

## 7. El titular Aitor Nogueras Pinyol ha sido cesado por corrupción, así que habrá que cerrar todos los pubs en los que esté como titular que dejarán de estar en nuestra base de datos. (1 puntos)

~~~sql
delete from titular where nombre like 'Aitor Nogueras Pinyol';
~~~

## 8. Debido a la fiesta de los alumnos de primero de grado superior de informática se han terminado las cervezas de todos los pubs de Badia, hay que reflejar este hecho en la tabla correspondiente en el campo existencias. (1 puntos)

~~~sql
update existencias set cantidad=0 where cod_pub IN (select cod_pub from pub where cod_localidad=1 or cod_localidad=12);
~~~

## 9. Crear una vista, FUERZAS_ELITE, que muestre los DNI y nombre de todos los empleados de seguridad, indicando en qué localidad prestan sus servicios, ordenados por el nombre de empleados y después por localidad. (1 puntos)

~~~sql
create view FUERZAS_ELITE AS select empleado.dni_empleado, empleado.nombre, pub.cod_localidad from empleado, pub, pub_empleado where empleado.dni_empleado=pub_empleado.dni_empleado and pub_empleado.cod_pub=pub.cod_pub and funcion='SEGURIDAD';
~~~
