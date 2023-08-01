---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Diccionarios

1. [Diccionarios](#diccionarios)
   1. [Características](#características)
   2. [Crear diccionarios](#crear-diccionarios)
   3. [Añadir elementos](#añadir-elementos)
   4. [Eliminar elementos](#eliminar-elementos)
   5. [Acceder a elementos](#acceder-a-elementos)
   6. [Recorrer](#recorrer)
   7. [Copiar](#copiar)
   8. [Diccionarios anidados](#diccionarios-anidados)

## Características

Características de los Diccionarios en Python:

1. **Estructura de Datos**: Los diccionarios son una estructura de datos en Python que te permite almacenar elementos en pares clave-valor.
2. **Colección Desordenada**: Los diccionarios no mantienen un orden específico para sus elementos. No se indexan mediante índices numéricos como las listas o tuplas.
3. **Claves Únicas**: Las claves en un diccionario son únicas, lo que significa que no puede haber dos claves iguales en un mismo diccionario. Si agregas un valor con una clave existente, el valor anterior asociado con esa clave se sobrescribirá.
4. **Mutable**: Los diccionarios son estructuras de datos mutables, lo que significa que puedes agregar, modificar y eliminar elementos después de su creación.
5. **Acceso a Elementos**: Los elementos de un diccionario se acceden mediante sus claves, en lugar de índices numéricos.
6. **Tipos de Datos**: Las claves y los valores en un diccionario pueden ser de cualquier tipo de datos, incluso pueden contener estructuras de datos complejas como listas, tuplas o incluso otros diccionarios.
7. **Uso de Llaves {}**: Para definir un diccionario, se utilizan llaves {} y se separan los pares clave-valor mediante dos puntos (:), y los elementos se separan por comas.
8. **Comprobación de Pertenencia**: Puedes verificar si una clave está presente en el diccionario utilizando el operador `in`.
9. **Métodos Integrados**: Python proporciona varios métodos integrados para trabajar con diccionarios, como `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `clear()`, etc.
10. **Longitud del Diccionario**: Puedes obtener la cantidad de pares clave-valor en el diccionario utilizando la función `len()`.
11. **Utilidades**: Los diccionarios son útiles cuando necesitas asociar datos de manera eficiente y rápida. Se utilizan para representar mapeos, configuraciones, bases de datos pequeñas, y mucho más.

## Crear diccionarios

Puedes crear diccionarios utilizando llaves {} y separando los pares clave-valor mediante dos puntos :

~~~py
# Ejemplo de un diccionario vacío
mi_diccionario = {}

# Ejemplo de un diccionario con elementos
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
~~~

## Añadir elementos

Para agregar elementos a un diccionario, simplemente asigna un valor a una nueva clave o a una clave existente.

~~~py
# Ejemplo de un diccionario vacío
mi_diccionario = {}

# Agregar elementos al diccionario
mi_diccionario["nombre"] = "Ana"
mi_diccionario["edad"] = 25

print(mi_diccionario)  # Salida: {"nombre": "Ana", "edad": 25}
~~~

## Eliminar elementos

Puedes eliminar elementos de un diccionario utilizando el método pop() o la palabra clave del.

~~~py
# Ejemplo de un diccionario con elementos
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Eliminar un elemento específico usando pop()
mi_diccionario.pop("edad")
print(mi_diccionario)  # Salida: {"nombre": "Juan", "ciudad": "Madrid"}

# Eliminar un elemento usando del
del mi_diccionario["ciudad"]
print(mi_diccionario)  # Salida: {"nombre": "Juan"}
~~~

## Acceder a elementos

Puedes acceder a los elementos de un diccionario mediante sus claves.

~~~py
# Ejemplo de un diccionario con elementos
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Acceder a elementos mediante claves
print(mi_diccionario["nombre"])  # Salida: "Juan"
print(mi_diccionario["ciudad"])  # Salida: "Madrid"
~~~

## Recorrer

Puedes recorrer los elementos de un diccionario utilizando un bucle for. Por defecto, el bucle itera sobre las claves, pero puedes usar el método items() para iterar sobre los pares clave-valor.

~~~py
# Ejemplo de un diccionario con elementos
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Recorrer el diccionario para obtener claves
for clave in mi_diccionario:
    print(clave)

# Recorrer el diccionario para obtener pares clave-valor
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
~~~

## Copiar

Puedes copiar un diccionario utilizando el método copy() o la función dict().

~~~py
# Ejemplo de un diccionario con elementos
mi_diccionario = {"nombre": "Juan", "edad": 30}

# Copiar el diccionario usando copy()
copia_diccionario = mi_diccionario.copy()

# Copiar el diccionario usando dict()
copia_diccionario2 = dict(mi_diccionario)
~~~

## Diccionarios anidados

Puedes tener diccionarios anidados, es decir, un diccionario que contiene otro diccionario como valor.

~~~py
# Ejemplo de diccionarios anidados
datos_persona = {
    "nombre": "Juan",
    "edad": 30,
    "direccion": {
        "calle": "Calle Principal",
        "ciudad": "Madrid",
        "codigo_postal": 28001
    }
}

# Acceder a elementos de diccionarios anidados
print(datos_persona["direccion"]["ciudad"])  # Salida: "Madrid"
~~~
