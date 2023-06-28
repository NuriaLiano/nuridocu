# Listas enlazadas

## ¿Qué son las listas enlazadas?

### Conceptos básicos

Las listas enlazadas son estructuras de datos que permiten almacenar y manipular colecciones de elementos de manera dinámica. A diferencia de los arrays estáticos, las listas enlazadas no requieren un tamaño fijo y pueden crecer o reducirse durante la ejecución del programa.

Una lista enlazada está compuesta por nodos, donde cada nodo contiene un valor y una referencia al siguiente nodo en la lista. El primer nodo de la lista se conoce como "cabeza" o "nodo inicial", y el último nodo no tiene una referencia al siguiente nodo, lo que indica el final de la lista.

El enlace entre los nodos se establece mediante las referencias. Cada nodo tiene una referencia que apunta al siguiente nodo en la lista, lo que permite recorrer los elementos de la lista de manera secuencial.

### Tipos de listas enlazadas

Existen diferentes tipos de listas enlazadas, cada una con sus propias características y usos:

- **Lista enlazada simple**: Cada nodo contiene un valor y una referencia al siguiente nodo. La navegación en esta lista se realiza de forma unidireccional, es decir, solo se puede avanzar en una dirección (de principio a fin).
-**Lista enlazada doble**: Cada nodo contiene un valor, una referencia al nodo siguiente y una referencia al nodo anterior. Esto permite la navegación en ambas direcciones (de principio a fin y de fin a principio).
- **Lista enlazada circular**: El último nodo de la lista tiene una referencia que apunta al primer nodo, formando un ciclo. Esto significa que la lista no tiene un principio ni un final distintos, y se puede recorrer continuamente.

### Ventajas y desventajas

Ventajas

- Flexibilidad en la asignación de memoria
- Inserción y eliminación eficientes
- Uso eficiente del espacio

Desventajas

- Acceso secuencial
- Uso de memoria adicional
- Complejidad en la implementación

## Estructura de una lista enlazada

### Nodos y enlaces

### Nodo inicial (cabeza), cola y nodo final

### Enlace entre nodos

## ¿Cómo implementar una lista enlazada?

### Clase NODO

- Campos de la clase (`valor`, `siguiente`)
- Métodos (`getValor()`, `setValor()`, `getSiguiente()`, `setSiguiente()`)

### Clase ListaEnlazada

- Campos de la clase (`cabeza`)
- Métodos (`estaVacia()`, `agregar()`, `mostrar()`, `insertarAlFinal()`, `insertarAlInicio()`, etc.)

## Operaciones con listas enlazadas

### Agregar elementos a la lista

- Al principio
- Al final
- En una posición específica

### Mostrar los elementos de la lista

### Obtener un elemento de la lista por posición

### Contar la cantidad de elementos en la lista

### Verificar si la lista está vacía

### Eliminar elementos de la lista

- Al principio
- Al final
- Por posición

### Casos especiales

#### Lista vacía

### Primer y último elemento

#### Liberación de memoria y el recolector de basura en Java

## Diferencias entre arrays, arrayslist y listas enlazadas



En la clase Node<E>, el parámetro de tipo <E> se utiliza para indicar que la clase Node es una clase genérica y que puede trabajar con cualquier tipo de objeto. La E es una convención comúnmente utilizada para representar el tipo de elemento genérico en las estructuras de datos.

Al utilizar <E> como parámetro de tipo, la clase Node se vuelve reutilizable y flexible, ya que puede adaptarse a diferentes tipos de datos según sea necesario. Por ejemplo, si deseas crear una lista enlazada de enteros, puedes utilizar Node<Integer> y todos los nodos de la lista contendrán elementos de tipo Integer. Si deseas crear una lista enlazada de cadenas, puedes utilizar Node<String> y los nodos contendrán elementos de tipo String.

El uso de genéricos en Java permite crear estructuras de datos más genéricas y versátiles, ya que no están limitadas a un solo tipo de dato. Esto promueve la reutilización de código y la creación de estructuras de datos más flexibles y adaptables a diferentes escenarios de uso.

