# Ejercicio 08 - Clases, herencia y nodos

Se desea implementar una estructura de datos de una lista enlazada para almacenar información de libros. Cada libro tiene un título y un autor. Además, se requiere implementar una subclase de libros llamada "LibroDigital" que tenga un atributo adicional para almacenar la URL del libro digital.

### Clase `Libro`

- La clase `Libro` representa un libro y tiene los siguientes atributos privados:
  - `titulo` (String): el título del libro.
  - `autor` (String): el autor del libro.
- La clase `Libro` tiene un constructor que recibe el título y el autor del libro, y los correspondientes métodos de acceso (getters y setters) para cada atributo.

### Clase `LibroDigital`

- La clase `LibroDigital` hereda de la clase `Libro` e incluye un atributo adicional:
  - `url` (String): la URL del libro digital.
- La clase `LibroDigital` tiene un constructor que recibe el título, el autor y la URL del libro digital, y los correspondientes métodos de acceso (getters y setters) para el atributo `url`.

### Clase `Nodo`

- La clase `Nodo` es una clase interna a la clase `ListaEnlazada` y tiene los siguientes atributos privados:
  - `libro` (Libro): el libro almacenado en el nodo.
  - `siguiente` (Nodo): referencia al siguiente nodo en la lista enlazada.
- La clase `Nodo` tiene un constructor que recibe un libro y un método de acceso (getter) para el atributo `siguiente`.

### Clase `ListaEnlazada`

- La clase `ListaEnlazada` representa una lista enlazada de libros y tiene los siguientes atributos privados:
  - `cabeza` (Nodo): referencia al primer nodo de la lista enlazada.
- La clase `ListaEnlazada` tiene un constructor sin parámetros y los siguientes métodos públicos:
  - `agregarAlPrincipio(Libro libro)`: agrega un libro al principio de la lista enlazada.
  - `agregarAlFinal(Libro libro)`: agrega un libro al final de la lista enlazada.
  - `agregarEnPosicion(Libro libro, int posicion)`: agrega un libro en una posición específica de la lista enlazada.
  - `eliminarPorTitulo(String titulo)`: elimina un libro de la lista enlazada por su título.

~~~java

~~~