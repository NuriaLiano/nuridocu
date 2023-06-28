# Ejercicio 13 - listas, nodos y clases

## Colores

Implementa una clase **ListaColores** que represente una lista enlazada de colores. La lista debe tener las siguientes funcionalidades:

- Un método para obtener la longitud de la lista.
- Un método para verificar si la lista está vacía.
- Un método para agregar un color al final de la lista.
- Un método para agregar un color al principio de la lista.
- Un método para agregar un color en una posición específica de la lista.
- Un método para eliminar el primer color de la lista.
- Un método para eliminar el último color de la lista.
- Un método para eliminar un color en una posición específica de la lista.
- Un método para mostrar la lista completa.

Implementa el **programa principal (Main)** donde se instancie un objeto de la clase ListaColores y se realicen las siguientes operaciones:

- Agregar los colores "Rojo", "Verde" y "Azul" al final de la lista.
- Agregar el color "Amarillo" al principio de la lista.
- Agregar el color "Naranja" en la posición 2 de la lista.
- Mostrar la lista completa.
- Obtener la longitud de la lista y mostrarla.
- Verificar si la lista está vacía y mostrar el resultado.
- Eliminar el primer color de la lista.
- Eliminar el último color de la lista.
- Eliminar el color en la posición 2 de la lista.
- Mostrar la lista completa nuevamente.

~~~java
//nodo.java
public class Nodo<E> {
    public E elemento;
    public Nodo<E> siguiente;

    public Nodo(E elemento, Nodo<E> siguiente) {
        this.elemento = elemento;
        this.siguiente = siguiente;
    }
}

//listacolores.java
public class ListaColores {
    private Nodo<String> cabeza;
    private int longitud;

    public ListaColores() {
        cabeza = null;
        longitud = 0;
    }

    public int obtenerLongitud() {
        return longitud;
    }

    public boolean estaVacia() {
        return cabeza == null;
    }

    public void agregarAlFinal(String color) {
        Nodo<String> nuevoNodo = new Nodo<>(color, null);

        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            Nodo<String> puntero = cabeza;
            while (puntero.siguiente != null) {
                puntero = puntero.siguiente;
            }
            puntero.siguiente = nuevoNodo;
        }
        longitud++;
    }

    public void agregarAlPrincipio(String color) {
        Nodo<String> nuevoNodo = new Nodo<>(color, cabeza);
        cabeza = nuevoNodo;
        longitud++;
    }

    public void agregarEnPosicion(String color, int posicion) {
        if (posicion < 0 || posicion > longitud) {
            throw new IllegalArgumentException("Posición inválida");
        }

        if (posicion == 0) {
            agregarAlPrincipio(color);
        } else if (posicion == longitud) {
            agregarAlFinal(color);
        } else {
            Nodo<String> nuevoNodo = new Nodo<>(color, null);

            Nodo<String> puntero = cabeza;
            for (int i = 0; i < posicion - 1; i++) {
                puntero = puntero.siguiente;
            }

            nuevoNodo.siguiente = puntero.siguiente;
            puntero.siguiente = nuevoNodo;
            longitud++;
        }
    }

    public void eliminarAlPrincipio() {
        if (cabeza != null) {
            cabeza = cabeza.siguiente;
            longitud--;
        }
    }

    public void eliminarAlFinal() {
        if (cabeza == null) {
            return;
        }

        if (cabeza.siguiente == null) {
            cabeza = null;
        } else {
            Nodo<String> puntero = cabeza;
            while (puntero.siguiente.siguiente != null) {
                puntero = puntero.siguiente;
            }
            puntero.siguiente = null;
        }
        longitud--;
    }

    public void eliminarEnPosicion(int posicion) {
        if (posicion < 0 || posicion >= longitud) {
            throw new IllegalArgumentException("Posición inválida");
        }

        if (posicion == 0) {
            eliminarAlPrincipio();
        } else if (posicion == longitud - 1) {
            eliminarAlFinal();
        } else {
            Nodo<String> puntero = cabeza;
            for (int i = 0; i < posicion - 1; i++) {
                puntero = puntero.siguiente;
            }
            puntero.siguiente = puntero.siguiente.siguiente;
            longitud--;
        }
    }

    public void mostrarLista() {
        Nodo<String> puntero = cabeza;
        while (puntero != null) {
            System.out.println(puntero.elemento);
            puntero = puntero.siguiente;
        }
    }
}

//main.java
public class Main {
    public static void main(String[] args) {
        ListaColores lista = new ListaColores();

        lista.agregarAlFinal("Rojo");
        lista.agregarAlFinal("Verde");
        lista.agregarAlFinal("Azul");

        lista.agregarAlPrincipio("Amarillo");

        lista.agregarEnPosicion("Naranja", 2);

        System.out.println("Lista completa:");
        lista.mostrarLista();

        System.out.println("Longitud de la lista: " + lista.obtenerLongitud());

        System.out.println("La lista está vacía: " + lista.estaVacia());

        lista.eliminarAlPrincipio();
        lista.eliminarAlFinal();
        lista.eliminarEnPosicion(2);

        System.out.println("Lista actualizada:");
        lista.mostrarLista();
    }
}
~~~
