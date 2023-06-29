# Ejercicio 4 - uso de arrays, arraylists y listas enlazadas

En este ejemplo, se crea un array con 5 elementos y se muestra utilizando un bucle for. Luego, se utiliza un ArrayList para almacenar los mismos números y se muestra utilizando un bucle for y el método get(). Por último, se implementa una lista enlazada con nodos y cabeceras, donde se agregan los números y se muestra utilizando el método mostrar().

Observa cómo las estructuras de datos Array, ArrayList y la lista enlazada se utilizan de manera similar para almacenar y mostrar los números. Sin embargo, la implementación y la forma de acceso a los elementos pueden variar.

~~~java
import java.util.ArrayList;
import java.util.LinkedList;
public class ListaEjercicio {
    public static void main(String[] args) {
        // Usando Arrays
        int[] array = new int[5];
        array[0] = 10;
        array[1] = 20;
        array[2] = 30;
        array[3] = 40;
        array[4] = 50;

        System.out.println("Array:");
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }

        // Usando ArrayList
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList.add(10);
        arrayList.add(20);
        arrayList.add(30);
        arrayList.add(40);
        arrayList.add(50);

        System.out.println("ArrayList:");
        for (int i = 0; i < arrayList.size(); i++) {
            System.out.println(arrayList.get(i));
        }

        // Usando lista enlazada con nodos y cabeceras
        ListaEnlazada listaEnlazada = new ListaEnlazada();
        listaEnlazada.agregarAlFinal(10);
        listaEnlazada.agregarAlFinal(20);
        listaEnlazada.agregarAlFinal(30);
        listaEnlazada.agregarAlFinal(40);
        listaEnlazada.agregarAlFinal(50);

        System.out.println("Lista enlazada:");
        listaEnlazada.mostrar();
    }
}

class Nodo {
    int valor;
    Nodo siguiente;

    public Nodo(int valor) {
        this.valor = valor;
        this.siguiente = null;
    }
}

class ListaEnlazada {
    Nodo cabeza;

    public ListaEnlazada() {
        this.cabeza = null;
    }

    public void agregarAlFinal(int valor) {
        Nodo nuevoNodo = new Nodo(valor);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            Nodo actual = cabeza;
            while (actual.siguiente != null) {
                actual = actual.siguiente;
            }
            actual.siguiente = nuevoNodo;
        }
    }

    public void mostrar() {
        Nodo actual = cabeza;
        while (actual != null) {
            System.out.println(actual.valor);
            actual = actual.siguiente;
        }
    }
}
~~~
