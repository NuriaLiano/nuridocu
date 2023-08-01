---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Set

1. [Set](#set)
   1. [Características](#características)
   2. [Añadir elementos](#añadir-elementos)
   3. [Eliminar elementos](#eliminar-elementos)
   4. [Recorrer set](#recorrer-set)
   5. [Unir sets](#unir-sets)
   6. [Métodos](#métodos)
      1. [Add](#add)
      2. [Remove](#remove)
      3. [Discard](#discard)
      4. [Pop](#pop)
      5. [Union](#union)
      6. [Intersection](#intersection)
      7. [Difference](#difference)
      8. [Symmetric\_difference](#symmetric_difference)

## Características

1. **Colección Desordenada**: Los conjuntos son colecciones desordenadas de elementos, lo que significa que no mantienen un orden específico.
2. **Elementos Únicos**: Los conjuntos no permiten elementos duplicados. Si intentas agregar un elemento que ya está presente, no se añadirá nuevamente.
3. **Mutable**: Los conjuntos son estructuras de datos mutables, lo que significa que puedes agregar y eliminar elementos después de su creación.
4. **No Soportan Indexación**: Debido a que los conjuntos son desordenados, no permiten el acceso a elementos mediante índices.
5. **Soporte para Iteración**: Puedes iterar sobre los elementos de un conjunto utilizando un bucle `for`.
6. **Soporte para Comprobación de Pertenencia**: Puedes verificar si un elemento está presente en un conjunto utilizando el operador `in`.
7. **No Permiten Elementos Mutables**: Los elementos de un conjunto deben ser objetos inmutables, ya que los conjuntos mismos son mutables.
8. **Uso de Llaves `{}`**: Para definir un conjunto, se utilizan llaves `{}` o la función `set()`.
9. **Conjuntos como Operaciones Matemáticas**: Los conjuntos en Python soportan operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.
10. **Métodos para Modificar Conjuntos**: Python proporciona varios métodos integrados para agregar, eliminar y actualizar elementos en un conjunto, como `add()`, `remove()`, `discard()`, `pop()`, `clear()`, `update()`, etc.
11. **Conjuntos Inmutables (Frozen Sets)**: Además de los conjuntos mutables, Python también ofrece conjuntos inmutables llamados "frozen sets" que no pueden ser modificados después de su creación.

## Añadir elementos

Puedes agregar elementos a un conjunto utilizando el método add().

~~~py
 # Ejemplo de un conjunto vacío
mi_set = set()

 # Agregar elementos al conjunto
mi_set.add(1)
mi_set.add(2)
mi_set.add(3)

print(mi_set)  # Salida: {1, 2, 3}
~~~

## Eliminar elementos

Puedes eliminar elementos de un conjunto utilizando varios métodos como remove(), discard(), o pop().

~~~py
 # Ejemplo de un conjunto
mi_set = {1, 2, 3, 4, 5}

 # Eliminar un elemento específico usando remove()
mi_set.remove(3)
print(mi_set)  # Salida: {1, 2, 4, 5}

 # Eliminar un elemento sin generar error usando discard()
mi_set.discard(6)  # No genera error si el elemento no está presente
print(mi_set)     # Salida: {1, 2, 4, 5}

 # Eliminar y obtener un elemento arbitrario usando pop()
elemento_eliminado = mi_set.pop()
print(elemento_eliminado)  # Salida: algún elemento del conjunto
print(mi_set)              # Salida: el conjunto sin el elemento eliminado
~~~

## Recorrer set

Puedes recorrer los elementos de un conjunto utilizando un bucle for.

~~~py
 # Ejemplo de un conjunto
mi_set = {1, 2, 3, 4, 5}

 # Recorrer los elementos del conjunto
for elemento in mi_set:
    print(elemento)
~~~

## Unir sets

Puedes unir dos o más conjuntos utilizando el método union() o el operador de barra vertical |

~~~py
 # Ejemplo de dos conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}

 # Unir los conjuntos usando el método union()
union_set = set1.union(set2)
print(union_set)  # Salida: {1, 2, 3, 4, 5}

 # Unir los conjuntos usando el operador |
union_set = set1 | set2
print(union_set)  # Salida: {1, 2, 3, 4, 5}
~~~

## Métodos

### Add

~~~py
 # Método add() para agregar un elemento
mi_set.add(6)
print(mi_set)  # Salida: {1, 2, 3, 4, 5, 6}
~~~

### Remove

~~~py
 # Método remove() para eliminar un elemento
mi_set.remove(3)
print(mi_set)  # Salida: {1, 2, 4, 5, 6}
~~~

### Discard

~~~py
 # Método discard() para eliminar un elemento sin generar error si no está presente
mi_set.discard(7)  # No genera error si el elemento no está presente
print(mi_set)     # Salida: {1, 2, 4, 5, 6}
~~~

### Pop

~~~py
 # Método pop() para eliminar y obtener un elemento arbitrario
elemento_eliminado = mi_set.pop()
print(elemento_eliminado)  # Salida: algún elemento del conjunto
print(mi_set)              # Salida: el conjunto sin el elemento eliminado
~~~

### Union

~~~py
 # Método union() para unir dos conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Salida: {1, 2, 3, 4, 5}
~~~

### Intersection

~~~py
 # Método intersection() para obtener la intersección de dos conjuntos
intersection_set = set1.intersection(set2)
print(intersection_set)  # Salida: {3}
~~~

### Difference

~~~py
 # Método difference() para obtener la diferencia entre dos conjuntos
difference_set = set1.difference(set2)
print(difference_set)  # Salida: {1, 2}
~~~

### Symmetric_difference

~~~py
 # Método symmetric_difference() para obtener la diferencia simétrica entre dos conjuntos
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Salida: {1, 2, 4, 5}
~~~