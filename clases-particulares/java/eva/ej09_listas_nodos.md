# Ejercicio 09 - Listas y nodos

## Lista enlazada de números pares

1. Agregar número par al final de la lista.
2. Mostrar todos los números de la lista.
3. Obtener la cantidad de números almacenados en la lista.
4. Verificar si la lista está vacía.
5. Eliminar el primer número par de la lista.

~~~java
//nodo.java
public class Nodo {
    public int valor;
    public Nodo siguiente;

    public Nodo(int valor) {
        this.valor = valor;
        this.siguiente = null;
    }
}

//listaenlazada.java
public class ListaEnlazadaPares {
    private Nodo cabeza;
    private int longitud;

    public ListaEnlazadaPares() {
        this.cabeza = null;
        this.longitud = 0;
    }

    public void agregarAlFinal(int numero) {
        if (numero % 2 == 0) {
            Nodo nuevoNodo = new Nodo(numero);
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
    }

    public void mostrarLista() {
        Nodo puntero = cabeza;
        while (puntero != null) {
            System.out.print(puntero.valor + " ");
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

    public void eliminarPrimerPar() {
        if (cabeza != null && cabeza.valor % 2 == 0) {
            cabeza = cabeza.siguiente;
            longitud--;
        }
    }
}
public class Main {
    public static void main(String[] args) {
        ListaEnlazadaPares lista = new ListaEnlazadaPares();

        lista.agregarAlFinal(2);
        lista.agregarAlFinal(4);
        lista.agregarAlFinal(6);
        lista.agregarAlFinal(7);
        lista.agregarAlFinal(8);

        System.out.println("Lista de números pares:");
        lista.mostrarLista();

        System.out.println("Cantidad de números en la lista: " + lista.obtenerCantidad());
        System.out.println("La lista está vacía: " + lista.estaVacia());

        lista.eliminarPrimerPar();
        System.out.println("Lista después de eliminar el primer número par:");
        lista.mostrarLista();
    }
}
~~~