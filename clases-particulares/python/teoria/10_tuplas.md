---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Tuplas

1. [Tuplas](#tuplas)
   1. [Características](#características)
   2. [Crear tupla](#crear-tupla)
   3. [Acceder a elementos](#acceder-a-elementos)
   4. [Longitud de tupla](#longitud-de-tupla)
   5. [Slicing](#slicing)
   6. [Comparar tuplas](#comparar-tuplas)
   7. [Extraer valores (Unpack)](#extraer-valores-unpack)
   8. [Recorrer la tupla](#recorrer-la-tupla)
   9. [Unir tuplas](#unir-tuplas)

## Características

1. **Colección Ordenad**a: Las tuplas son colecciones ordenadas de elementos, lo que significa que los elementos se mantienen en el mismo orden en el que se insertaron.
2. **Inmutabilidad**: Las tuplas son estructuras de datos inmutables, lo que significa que una vez creadas, no se pueden modificar, agregar ni eliminar elementos. Son estáticas y no cambian su contenido durante la ejecución del programa.
3. **Heterogeneidad**: Las tuplas pueden contener elementos de diferentes tipos de datos, al igual que las listas, como números, cadenas, otras tuplas, etc.
4. **Indexación**: Al igual que las listas, los elementos de una tupla se acceden mediante índices, que comienzan desde 0. Puedes acceder a elementos individuales utilizando su índice.
5. **Longitud Fija**: A diferencia de las listas, las tuplas tienen una longitud fija, lo que significa que no se pueden modificar para agregar o eliminar elementos después de su creación.
6. **Soporte de Slice**: Al igual que las listas, puedes acceder a una porción (slice) de una tupla utilizando la notación de rebanado (slicing) con dos puntos `:`.
7. **Iterabilidad**: Las tuplas son iterables, lo que significa que puedes recorrer sus elementos utilizando un bucle `for`.
8. **Uso de Paréntesis**: Para definir una tupla, se utilizan paréntesis `()` en lugar de corchetes `[]` que se usan para las listas.
9. **Rendimiento Mejorado**: Dado que las tuplas son inmutables, tienden a ser más rápidas en términos de acceso a elementos y uso de memoria en comparación con las listas.
10. **Embalaje y Desembalaje**: Las tuplas permiten el empaquetado y desempaquetado de valores, lo que permite asignar múltiples variables a la vez.
11. **Aplicaciones Específicas**: Debido a su inmutabilidad, las tuplas son útiles para datos que no deben cambiar, como coordenadas, configuraciones, claves para diccionarios, etc.

## Crear tupla

Puedes crear una tupla utilizando paréntesis () y separando los elementos con comas.

~~~py
mi_tupla = (1, 2, 3, "Hola", "Mundo")
~~~

## Acceder a elementos

~~~py
print(mi_tupla[0])  # Salida: 1
print(mi_tupla[3])  # Salida: "Hola"
~~~

## Longitud de tupla

~~~py
print(len(mi_tupla))  # Salida: 5
~~~

## Slicing

~~~py
print(mi_tupla[1:4])  # Salida: (2, 3, "Hola")
~~~

## Comparar tuplas

~~~py
tupla1 = (1, 2, 3)
tupla2 = (1, 2, 3)
if tupla1 == tupla2:
    print("Las tuplas son iguales.")
~~~

## Extraer valores (Unpack)

~~~py
a, b, c, d, e = mi_tupla
print(a, b, c, d, e)  # Salida: 1 2 3 "Hola" "Mundo"
~~~

## Recorrer la tupla

~~~py
for elemento in mi_tupla:
    print(elemento)
~~~

## Unir tuplas

~~~py
tupla_unida = tupla1 + tupla2
~~~
