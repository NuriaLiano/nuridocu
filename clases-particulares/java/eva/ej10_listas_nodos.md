
# Ejercicio 10 - Listas y nodos

https://www.discoduroderoer.es/ejercicios-propuestos-y-resueltos-basicos-listas-enlazadas-en-java/

## Clase `MiListaEnlazadaAvanzada`

La clase `MiListaEnlazadaAvanzada` extiende a `MiListaEnlazadaBasica` y proporciona funcionalidades adicionales para la manipulación de una lista enlazada.

### Métodos

- `insertar(E info, int posicion)`: inserta un elemento en la posición especificada de la lista enlazada.
- `extraer(int posicion)`: extrae el elemento en la posición especificada de la lista enlazada.
- `insertarUltimo(E info)`: inserta un elemento al final de la lista enlazada.
- `extraerUltimo()`: extrae el último elemento de la lista enlazada.
- `imprimir(int posicion)`: imprime los elementos de la lista enlazada a partir de la posición especificada.

#### Clase Node`<E>`

~~~java

~~~

~~~java
public class MyBasicLinkedList<E> {
    
    protected Node<E> primero;

    public MyBasicLinkedList() {
        this.primero = null;
    }

    public Node<E> getPrimero() {
        return this.primero;
    }

    public void setPrimero(Node<E> primero) {
        this.primero = primero;
    }

    public boolean estaVacia() {
        return (this.primero == null);
    }

    public void insertar(E info) {
        Node<E> nuevoNodo = new Node<E>(info);
        nuevoNodo.setSiguiente(this.primero);
        primero = nuevoNodo;
    }

    public E extraer() {
        E dato = null;
        if (this.primero != null) {
            dato = this.primero.getInfo();
            this.primero = this.primero.getSiguiente();
        }
        return dato;
    }

    public void insertar(E info, Node<E> anterior) {
        if(anterior != null) {
            Node<E> nuevoNodo = new Node<E>(info);
            nuevoNodo.setSiguiente(anterior.getSiguiente());
            anterior.setSiguiente(nuevoNodo);
        }
    }

    public E extraer(Node<E> anterior) {
        E dato = null;
        if(anterior != null && anterior.getSiguiente() != null) {
            dato = anterior.getSiguiente().getInfo();
            anterior.setSiguiente(anterior.getSiguiente().getSiguiente());
        }
        return dato;
    }

    public int tamano() {
        int tamano = 0;
        Node<E> actual = this.primero;
        
        while(actual != null) {
            tamano++;
            actual = actual.getSiguiente();
        }
        return tamano;
    }

    public String toString() {
        String textoLista = "";
        Node<E> actual = this.primero;
        
        while(actual != null) {
            textoLista = textoLista + actual.getInfo().toString();
            if(actual.getSiguiente() != null) {
                textoLista = textoLista + " -> ";
            }
            actual = actual.getSiguiente();
        }
        return textoLista;
    }

    public void imprimir() {
        System.out.println(this);
    }

    public Node<E> buscarNodo(E info) {
        Node<E> nodoObjetivo = null;
        Node<E> nodoActual = this.primero;

        while(nodoActual != null && !nodoActual.getInfo().equals(info)) {
            nodoActual = nodoActual.getSiguiente();
        }
        if(nodoActual != null) {
            nodoObjetivo = nodoActual;
        }
        return nodoObjetivo;
    }

    public Node<E> buscarNodo(int n) {
        Node<E> nodoObjetivo = null;
        Node<E> nodoActual = this.primero;
        int contador = 0;

        while(nodoActual != null && contador < n) {
            nodoActual = nodoActual.getSiguiente();
        contador++;
        }
        if(nodoActual != null) {
            nodoObjetivo = nodoActual;
        }
        return nodoObjetivo;
    }

    public Node<E> buscarUltimoNodo() {
        Node<E> actual = this.primero;
        
        while(actual != null && actual.getSiguiente() != null) {
            actual = actual.getSiguiente();
        }
        return actual;
    }

    public int buscar(E info) {
        Node<E> actual = this.primero;
        int posicionInfo = -1;
        
        if(!estaVacia()) {
            posicionInfo = 0;
            while(actual != null && !actual.getInfo().equals(info)) {
                posicionInfo++;
                actual = actual.getSiguiente();
            }
        }
        return posicionInfo;
    }

    public int numeroDeOcurrencias(E info) {
        int contador = 0;
        Node<E> actual = this.primero;
        
        while(actual != null) {
            if(actual.getInfo().equals(info)){
                contador++;
            }
            actual = actual.getSiguiente();
        }
        return contador;
    }
}

public class MyAdvancedLinkedList<E> extends MyBasicLinkedList<E> {
    
    public MyAdvancedLinkedList() {
        super();
    }
    
    public void insertar(E info, int posicion) {
        Node<E> nodoAnterior = buscarNodo(posicion-1);

        if(nodoAnterior != null) {
            insertar(info, nodoAnterior);
        }
    }
    
    public E extraer(int posicion) {
        Node<E> nodoAnterior = buscarNodo(posicion-1);
        E info = null;
        
        if(nodoAnterior != null) {
            info = extraer(nodoAnterior);
        }
        return info;
    }

    public void insertarUltimo(E info) {
        Node<E> ultimoNodo = buscarUltimoNodo();
        
        if(ultimoNodo != null) {
            insertar(info, ultimoNodo);
        } else {
            this.primero = new Node<E>(info);;
        }
    }
    
    public E extraerUltimo() {
        E info = null;
        Node<E> actual = this.primero;
        int tamanoLista = tamano();

        if(!estaVacia()) {
            if(tamanoLista == 1) {
                info = actual.getInfo();
                this.primero = null;
            } else {
                Node<E> nodoAnteriorUltimo = buscarNodo(tamanoLista-2);
                info = extraer(nodoAnteriorUltimo);
            }
        }
        return info;
    }

    public void imprimir(int posicion) {
        Node<E> actual = this.primero;
        int contador = 0;
        String textoLista = "";

        if(!estaVacia()) {
            while(actual != null && contador < posicion ) {
                actual = actual.getSiguiente();
                contador++;
            }
            while(actual != null) {
                textoLista = textoLista + actual.getInfo().toString();
                if(actual.getSiguiente() != null) {
                    textoLista = textoLista + " -> ";
                }
                actual = actual.getSiguiente();
            }
        }
        System.out.println(textoLista);
    }    
}

~~~
