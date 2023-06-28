# Ejercicio 11 - Listas y nodos

## Lista de nombres

1. Agregar un nombre al final de la lista.
2. Mostrar todos los nombres de la lista.
3. Obtener la cantidad de nombres almacenados en la lista.
4. Verificar si la lista está vacía.
5. Insertar un nombre en el medio de la lista.
6. Eliminar un nombre específico de la lista.

~~~java
//nodo.java
public class Nodo {
    public String nombre;
    public Nodo siguiente;

    public Nodo(String nombre) {
        this.nombre = nombre;
        this.siguiente = null;
    }
}

//listaenlazada.java
public class ListaEnlazadaNombres {
    private Nodo cabeza;
    private int longitud;

    public ListaEnlazadaNombres() {
        this.cabeza = null;
        this.longitud = 0;
    }

    public void agregarAlFinal(String nombre) {
        Nodo nuevoNodo = new Nodo(nombre);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            Nodo puntero = cabeza;
            while (puntero.siguiente != null) {
                puntero = puntero.siguiente;
            }
            puntero.siguiente = nuevoNodo;
        }
        longitud++;
    }

    public void mostrarLista() {
        Nodo puntero = cabeza;
        while (puntero != null) {
            System.out.print(puntero.nombre + " ");
            puntero = puntero.siguiente;
        }
        System.out.println();
    }

    public int obtenerCantidad() {
        return longitud;
    }

    public boolean estaVacia() {
        return cabeza == null;
    }

    public void insertarEnMedio(String nombre, int posicion) {
        if (posicion >= 0 && posicion < longitud) {
            if (posicion == 0) {
                Nodo nuevoNodo = new Nodo(nombre);
                nuevoNodo.siguiente = cabeza;
                cabeza = nuevoNodo;
            } else {
                Nodo puntero = cabeza;
                int contador = 0;
                while (contador < posicion - 1) {
                    puntero = puntero.siguiente;
                    contador++;
                }
                Nodo nuevoNodo = new Nodo(nombre);
                nuevoNodo.siguiente = puntero.siguiente;
                puntero.siguiente = nuevoNodo;
            }
            longitud++;
        }
    }

    public void eliminarNombre(String nombre) {
        if (cabeza != null) {
            if (cabeza.nombre.equals(nombre)) {
                cabeza = cabeza.siguiente;
                longitud--;
            } else {
                Nodo puntero = cabeza;
                while (puntero.siguiente != null && !puntero.siguiente.nombre.equals(nombre)) {
                    puntero = puntero.siguiente;
                }
                if (puntero.siguiente != null) {
                    puntero.siguiente = puntero.siguiente.siguiente;
                    longitud--;
                }
            }
        }
    }
}

//main.java
public class Main {
    public static void main(String[] args) {
        ListaEnlazadaNombres lista = new ListaEnlazadaNombres();

        lista.agregarAlFinal("Juan");
        lista.agregarAlFinal("Pedro");
        lista.agregarAlFinal("María");

        System.out.println("Lista de nombres:");
        lista.mostrarLista();

        System.out.println("Cantidad de nombres en la lista: " + lista.obtenerCantidad());
        System.out.println("La lista está vacía: " + lista.estaVacia());

        lista.insertarEnMedio("Luisa", 1);
        System.out.println("Lista después de insertar en medio:");
        lista.mostrarLista();

        lista.eliminarNombre("Pedro");
        System.out.println("Lista después de eliminar un nombre:");
        lista.mostrarLista();
    }
}
~~~