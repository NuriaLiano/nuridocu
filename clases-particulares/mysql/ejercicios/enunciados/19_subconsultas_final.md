# Ejercicios de subconsultas y joins

## Base de datos, tablas y datos

~~~sql
-- Creación de la base de datos
CREATE DATABASE ejercicio_subconsultas;

-- Selección de la base de datos
USE ejercicio_subconsultas;

-- Creación de la tabla "clientes"
CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nombre VARCHAR(100),
  ciudad VARCHAR(100)
);

-- Inserción de datos en la tabla "clientes"
INSERT INTO clientes (id, nombre, ciudad) VALUES
  (1, 'John Smith', 'Nueva York'),
  (2, 'Maria Garcia', 'Madrid'),
  (3, 'Robert Johnson', 'Chicago'),
  (4, 'Ana Torres', 'Barcelona'),
  (5, 'David Kim', 'Los Ángeles');

-- Creación de la tabla "pedidos"
CREATE TABLE pedidos (
  id INT PRIMARY KEY,
  cliente_id INT,
  producto VARCHAR(100),
  cantidad INT,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Inserción de datos en la tabla "pedidos"
INSERT INTO pedidos (id, cliente_id, producto, cantidad) VALUES
  (1, 1, 'Camisa', 3),
  (2, 2, 'Pantalón', 2),
  (3, 3, 'Zapatos', 1),
  (4, 1, 'Chaqueta', 1),
  (5, 4, 'Vestido', 2);

~~~

## 1: Obtener los nombres de los clientes que han realizado pedidos

## 2: Obtener los productos y las cantidades de los pedidos realizados por clientes de Madrid

## 3: Obtener los nombres de los clientes que han realizado al menos 2 pedidos

## 4: Obtener el total de pedidos realizados por cada cliente

## 5: Obtener los nombres de los clientes que han realizado pedidos de productos diferentes al cliente con ID 1

## 5: Obtener los productos y las cantidades de los pedidos realizados por clientes de Madrid, excluyendo los pedidos de productos que contengan la palabra "Zapatos"

## Obtener los nombres de los clientes que han realizado al menos un pedido y su ciudad no coincide con la ciudad de ningún otro cliente

## Obtener el producto con la cantidad más alta entre todos los pedidos realizados

## Obtener los nombres de los clientes que han realizado pedidos de todos los productos disponibles

## Obtener el nombre del cliente que ha realizado el pedido con la cantidad más alta entre todos los pedidos realizados
