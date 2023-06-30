# Ejercicio 18 - Repaso general agregar y eliminar de listas enlazadas



~~~java
public class EjercicioListaEnlazada {
    public static void main(String[] args) {
        ListaEnlazada lista = new ListaEnlazada();

        // Agregar elementos al final de la lista
        lista.agregarAlFinal(10);
        lista.agregarAlFinal(20);
        lista.agregarAlFinal(30);
        lista.agregarAlFinal(40);
        lista.agregarAlFinal(50);

        // Mostrar la lista
        System.out.println("Lista original:");
        lista.mostrarLista();

        // Agregar elemento al principio de la lista
        lista.agregarAlPrincipio(5);

        // Mostrar la lista después de agregar al principio
        System.out.println("Lista después de agregar al principio:");
        lista.mostrarLista();

        // Agregar elemento en una posición específica
        lista.agregarEnPosicion(3, 15);

        // Mostrar la lista después de agregar en una posición específica
        System.out.println("Lista después de agregar en una posición específica:");
        lista.mostrarLista();

        // Eliminar elemento al final de la lista
        lista.eliminarAlFinal();

        // Mostrar la lista después de eliminar al final
        System.out.println("Lista después de eliminar al final:");
        lista.mostrarLista();

        // Eliminar elemento al principio de la lista
        lista.eliminarAlPrincipio();

        // Mostrar la lista después de eliminar al principio
        System.out.println("Lista después de eliminar al principio:");
        lista.mostrarLista();

        // Eliminar elemento en una posición específica
        lista.eliminarEnPosicion(2);

        // Mostrar la lista después de eliminar en una posición específica
        System.out.println("Lista después de eliminar en una posición específica:");
        lista.mostrarLista();
    }
}

class Nodo {
    private int valor;
    private Nodo siguiente;

    public Nodo(int valor) {
        this.valor = valor;
        this.siguiente = null;
    }

    public int getValor() {
        return valor;
    }

    public void setValor(int valor) {
        this.valor = valor;
    }

    public Nodo getSiguiente() {
        return siguiente;
    }

    public void setSiguiente(Nodo siguiente) {
        this.siguiente = siguiente;
    }
}

class ListaEnlazada {
    private Nodo cabeza;
    public ListEnlazada(){
        cabeza = null;
    }
    public void agregarAlFinal(int valor) {
        Nodo nuevoNodo = new Nodo(valor);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            Nodo nodoActual = cabeza;
            while (nodoActual.getSiguiente() != null) {
                nodoActual = nodoActual.getSiguiente();
            }
            nodoActual.setSiguiente(nuevoNodo);
        }
    }

    public void agregarAlPrincipio(int valor) {
        Nodo nuevoNodo = new Nodo(valor);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            nuevoNodo.setSiguiente(cabeza);
            cabeza = nuevoNodo;
        }
    }

    public void agregarEnPosicion(int posicion, int valor) {
        if (posicion < 0) {
            System.out.println("Posición inválida");
            return;
        }

        Nodo nuevoNodo = new Nodo(valor);

        if (posicion == 0) {
            nuevoNodo.setSiguiente(cabeza);
            cabeza = nuevoNodo;
            return;
        }

        Nodo nodoActual = cabeza;
        int contador = 0;
        while (nodoActual != null && contador < posicion - 1) {
            nodoActual = nodoActual.getSiguiente();
            contador++;
        }

        if (nodoActual == null) {
            System.out.println("Posición inválida");
            return;
        }

        nuevoNodo.setSiguiente(nodoActual.getSiguiente());
        nodoActual.setSiguiente(nuevoNodo);
    }

    public void eliminarAlFinal() {
        if (cabeza == null || cabeza.getSiguiente() == null) {
            cabeza = null;
            return;
        }

        Nodo nodoActual = cabeza;
        while (nodoActual.getSiguiente().getSiguiente() != null) {
            nodoActual = nodoActual.getSiguiente();
        }
        nodoActual.setSiguiente(null);
    }

    public void eliminarAlPrincipio() {
        if (cabeza != null) {
            cabeza = cabeza.getSiguiente();
        }
    }

    public void eliminarEnPosicion(int posicion) {
        if (posicion < 0 || cabeza == null) {
            System.out.println("Posición inválida");
            return;
        }

        if (posicion == 0) {
            cabeza = cabeza.getSiguiente();
            return;
        }

        Nodo nodoActual = cabeza;
        int contador = 0;
        while (nodoActual.getSiguiente() != null && contador < posicion - 1) {
            nodoActual = nodoActual.getSiguiente();
            contador++;
        }
        if (nodoActual.getSiguiente() != null) {
            nodoActual.setSiguiente(nodoActual.getSiguiente().getSiguiente());
        } else {
            System.out.println("Posición inválida");
        }
    }

    public void mostrarLista() {
        Nodo nodoActual = cabeza;
        while (nodoActual != null) {
            System.out.print(nodoActual.getValor() + " ");
            nodoActual = nodoActual.getSiguiente();
        }
        System.out.println();
    }
}
~~~
