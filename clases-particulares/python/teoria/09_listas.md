---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Listas

1. [Listas](#listas)
   1. [Características](#características)
   2. [Crear listas](#crear-listas)
   3. [Acceder a los elementos](#acceder-a-los-elementos)
   4. [Modificar elementos](#modificar-elementos)
   5. [Eliminar elementos](#eliminar-elementos)
   6. [Longitud de una lista](#longitud-de-una-lista)
   7. [Slicing list](#slicing-list)
   8. [Copiar listas](#copiar-listas)
   9. [Unir listas](#unir-listas)
   10. [Convertir otros objetos en listas](#convertir-otros-objetos-en-listas)
   11. [Otros métodos](#otros-métodos)
   12. [List Comprehesion (listas de compresión)](#list-comprehesion-listas-de-compresión)
   13. [Listas anidadas](#listas-anidadas)
       1. [Acceder a elementos](#acceder-a-elementos)
       2. [Modificar los elementos](#modificar-los-elementos)
       3. [Longitud de una lista anidada](#longitud-de-una-lista-anidada)
       4. [Slicing](#slicing)
       5. [Copiar](#copiar)
       6. [Unir](#unir)

## Características

1. **Colección Ordenada**: Las listas son colecciones ordenadas de elementos, lo que significa que los elementos se mantienen en el mismo orden en el que se insertaron.
2. **Heterogeneidad**: Las listas pueden contener elementos de diferentes tipos de datos, como números, cadenas, listas anidadas, tuplas, diccionarios, etc.
3. **Modificables** (Mutable): Las listas son estructuras de datos mutables, lo que significa que se pueden modificar después de su creación. Puedes cambiar, agregar o eliminar elementos.
4. **Indexación**: Los elementos de una lista se acceden mediante índices, que comienzan desde 0. Puedes acceder a elementos individuales utilizando su índice.
5. **Longitud Variable**: Las listas pueden cambiar de longitud dinámicamente, lo que significa que puedes agregar o eliminar elementos según sea necesario.
6. **Soporte de Slice**: Puedes acceder a una porción (slice) de una lista utilizando la notación de rebanado (slicing) con dos puntos `:`.
7. **Soporte para Iteración**: Las listas son iterables, lo que significa que puedes recorrer sus elementos utilizando un bucle `for`.
8. **Duplicados Permitidos**: Las listas pueden contener elementos duplicados, es decir, un mismo valor puede aparecer varias veces en la lista.
9. **Múltiples Métodos y Operaciones**: Python proporciona una amplia variedad de métodos y operaciones integrados para trabajar con listas, como `append()`, `insert()`, `remove()`, `pop()`, `extend()`, `sort()`, `reverse()`, etc.
10. **Listas Anidadas**: Las listas pueden contener otras listas como elementos, lo que permite crear estructuras de datos más complejas y jerárquicas.
11. **Versatilidad**: Las listas son ampliamente utilizadas debido a su versatilidad y su capacidad para adaptarse a diferentes necesidades y situaciones.

## Crear listas

Para crear una lista en Python, simplemente utiliza corchetes [] y separa los elementos con comas.

~~~py
mi_lista = [1, 2, 3, 15]
~~~

## Acceder a los elementos

Puedes acceder a los elementos individuales de una lista utilizando su índice. **Recuerda que la indexación en Python empieza desde 0.**

~~~py
print(mi_lista[0])  # Salida: 1
print(mi_lista[3])  # Salida: 15
~~~

## Modificar elementos

Puedes modificar elementos individuales de una lista asignándoles un nuevo valor a través de su índice.ç

~~~py
mi_lista[1] = 10
print(mi_lista)  # Salida: [1, 10, 3, 15]
~~~

## Eliminar elementos

Hay varios métodos para eliminar elementos de una lista:

- **remove(**): Elimina el primer elemento con el valor especificado.
- **pop()**: Elimina el elemento en el índice especificado y devuelve su valor.
- **del**: Elimina el elemento en el índice especificado.

~~~py
mi_lista.remove(3)
print(mi_lista)  # Salida: [1, 10, 3]

valor_eliminado = mi_lista.pop(1)
print(valor_eliminado)  # Salida: 10

del mi_lista[2]
print(mi_lista)  # Salida: [1, 10, 15]
~~~

## Longitud de una lista

Puedes obtener la longitud de una lista utilizando la función len().

~~~py
print(len(mi_lista))  # Salida: 3
~~~

## Slicing list

Puedes obtener una porción de una lista utilizando la notación de slicing con dos puntos :

~~~py
print(mi_lista[1:3])  # Salida: [10, 3, 15]
~~~

## Copiar listas

Puedes copiar una lista utilizando el método copy() o mediante el operador de slicing.

~~~py
copia_lista1 = mi_lista.copy()
copia_lista2 = mi_lista[:]
~~~

## Unir listas

Puedes unir dos listas utilizando el operador + o el método extend().

~~~py
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_unida = lista1 + lista2
print(lista_unida)  # Salida: [1, 2, 3, 4, 5, 6]

lista1.extend(lista2)
print(lista1)  # Salida: [1, 2, 3, 4, 5, 6]
~~~

## Convertir otros objetos en listas

La función list() en Python se utiliza para convertir otros objetos iterables en listas. Un objeto iterable es aquel que puede ser recorrido elemento por elemento, como una cadena, una tupla, un conjunto o incluso otro tipo de lista.

Es importante mencionar que si intentas convertir un objeto que no es iterable en una lista usando list(), generará un error. Sin embargo, la mayoría de los tipos de datos en Python son iterables, por lo que list() es una función muy útil para manipular datos en forma de listas.

~~~py
lista_nueva = list(iterable)

 # Convertir una cadena en una lista
cadena = "Hola"
lista_cadena = list(cadena)
print(lista_cadena)  # Salida: ['H', 'o', 'l', 'a']

 #Convertir un conjunto en lista
mi_set = {1, 2, 3}
lista_set = list(mi_set)
print(lista_set)  # Salida: [1, 2, 3]
~~~

## Otros métodos

Algunos métodos útiles para trabajar con listas en Python son:

- **append()**: Agrega un elemento al final de la lista.
- **insert()**: Inserta un elemento en una posición específica.
- **index()**: Devuelve el índice del primer elemento con el valor especificado.
- **count()**: Devuelve la cantidad de veces que aparece un elemento en la lista.
- **sort()**: Ordena la lista en orden ascendente.
- **reverse()**: Invierte el orden de los elementos en la lista.

~~~py
mi_lista.append("Mundo")
print(mi_lista)  # Salida: [1, 10, 3, 15, 'Mundo']

mi_lista.insert(1, "Python")
print(mi_lista)  # Salida: [1, 'Python', 10, 3, 15, 'Mundo']

print(mi_lista.index("Python"))  # Salida: 1

print(mi_lista.count(1))  # Salida: 1

mi_lista.sort()
print(mi_lista)  

mi_lista.reverse()
print(mi_lista) 
~~~

## List Comprehesion (listas de compresión)

La comprensión de listas (List Comprehension) es una forma concisa de crear listas utilizando una sintaxis especial.

~~~py
# Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]
~~~

## Listas anidadas

Las listas anidadas son listas que contienen otras listas como elementos. Esto permite crear estructuras de datos más complejas y flexibles.

~~~py
# Ejemplo de lista anidada
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_anidada)
~~~

### Acceder a elementos

~~~py
# Acceder a elementos en una lista anidada
print(lista_anidada[0])       # Salida: [1, 2, 3]
print(lista_anidada[1][2])    # Salida: 6
~~~

### Modificar los elementos

~~~py
# Modificar elementos en una lista anidada
lista_anidada[2][1] = 88
print(lista_anidada)         # Salida: [[1, 2, 3], [4, 5, 6], [7, 88, 9]]
~~~

### Longitud de una lista anidada

~~~py
# Longitud de una lista anidada
print(len(lista_anidada))    # Salida: 3
print(len(lista_anidada[0]))  # Salida: 3
~~~

### Slicing

~~~py
# Slicing en una lista anidada
print(lista_anidada[1][1:])  # Salida: [5, 6]
~~~

### Copiar

~~~py
# Copiar una lista anidada
copia_lista_anidada = [lista[:] for lista in lista_anidada]
~~~

### Unir

~~~py
# Unir listas anidadas
lista_anidada.extend([[10, 11, 12], [13, 14, 15]])
print(lista_anidada)  # Salida: [[1, 2, 3], [4, 5, 6], [7, 88, 9], [10, 11, 12], [13, 14, 15]]
~~~
