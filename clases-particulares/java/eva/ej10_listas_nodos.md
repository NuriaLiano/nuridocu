# Ejercicio 08 - clases, listas y nodos

Crear una lista simple enlazada y realizar un menú donde se pueda hacer lo siguiente:

- Agregar
- Mostrar
- Ingresar al final
- Ingresar al inicio
- Encontrar el mayor número
- Encontrar el menor número
- Calcular el promedio
- Ordenar
- Eliminar por posición

~~~java
import java.util.Scanner;

//nodo.java
public class Nodo {

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

//listaenlazada.java
public class ListaEnlazada {

    private Nodo cabeza;

    public ListaEnlazada() {
        cabeza = null;
    }

    public boolean estaVacia() {
        return cabeza == null;
    }

    public void agregar(int valor) {
        Nodo nuevoNodo = new Nodo(valor);
        if (estaVacia()) {
            cabeza = nuevoNodo;
        } else {
            Nodo actual = cabeza;
            while (actual.getSiguiente() != null) {
                actual = actual.getSiguiente();
            }
            actual.setSiguiente(nuevoNodo);
        }
    }

    public void mostrar() {
        if (estaVacia()) {
            System.out.println("La lista está vacía");
        } else {
            Nodo actual = cabeza;
            while (actual != null) {
                System.out.print(actual.getValor() + " ");
                actual = actual.getSiguiente();
            }
            System.out.println();
        }
    }

    public void ingresarAlFinal(int valor) {
        Nodo nuevoNodo = new Nodo(valor);
        if (estaVacia()) {
            cabeza = nuevoNodo;
        } else {
            Nodo actual = cabeza;
            while (actual.getSiguiente() != null) {
                actual = actual.getSiguiente();
            }
            actual.setSiguiente(nuevoNodo);
        }
    }

    public void ingresarAlInicio(int valor) {
        Nodo nuevoNodo = new Nodo(valor);
        if (estaVacia()) {
            cabeza = nuevoNodo;
        } else {
            nuevoNodo.setSiguiente(cabeza);
            cabeza = nuevoNodo;
        }
    }

    public int encontrarMayor() {
        if (estaVacia()) {
            System.out.println("La lista está vacía");
            return Integer.MIN_VALUE;
        } else {
            int mayor = cabeza.getValor();
            Nodo actual = cabeza.getSiguiente();
            while (actual != null) {
                if (actual.getValor() > mayor) {
                    mayor = actual.getValor();
                }
                actual = actual.getSiguiente();
            }
            return mayor;
        }
    }

    public int encontrarMenor() {
        if (estaVacia()) {
            System.out.println("La lista está vacía");
            return Integer.MAX_VALUE;
        } else {
            int menor = cabeza.getValor();
            Nodo actual = cabeza.getSiguiente();
            while (actual != null) {
                if (actual.getValor() < menor) {
                    menor = actual.getValor();
                }
                actual = actual.getSiguiente();
            }
            return menor;
        }
    }

    public double calcularPromedio() {
        if (estaVacia()) {
            System.out.println("La lista está vacía");
            return 0.0;
        } else {
            int sumatoria = 0;
            int contador = 0;
            Nodo actual = cabeza;
            while (actual != null) {
                sumatoria += actual.getValor();
                contador++;
                actual = actual.getSiguiente();
            }
            return (double) sumatoria / contador;
        }
    }

    public void ordenar() {
        if (estaVacia()) {
            System.out.println("La lista está vacía");
        } else {
            Nodo actual = cabeza;
            while (actual != null) {
                Nodo siguiente = actual.getSiguiente();
                while (siguiente != null) {
                    if (actual.getValor() > siguiente.getValor()) {
                        int temp = actual.getValor();
                        actual.setValor(siguiente.getValor());
                        siguiente.setValor(temp);
                    }
                    siguiente = siguiente.getSiguiente();
                }
                actual = actual.getSiguiente();
            }
        }
    }

    public void eliminarPorPosicion(int posicion) {
        if (estaVacia()) {
            System.out.println("La lista está vacía");
        } else if (posicion < 0 || posicion >= size()) {
            System.out.println("Posición inválida");
        } else if (posicion == 0) {
            cabeza = cabeza.getSiguiente();
        } else {
            int contador = 0;
            Nodo actual = cabeza;
            while (contador < posicion - 1) {
                actual = actual.getSiguiente();
                contador++;
            }
            actual.setSiguiente(actual.getSiguiente().getSiguiente());
        }
    }

    private int size() {
        int contador = 0;
        Nodo actual = cabeza;
        while (actual != null) {
            contador++;
            actual = actual.getSiguiente();
        }
        return contador;
    }
}

//main.java
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ListaEnlazada lista = new ListaEnlazada();
        int opcion;

        do {
            System.out.println("----- MENÚ -----");
            System.out.println("1. Agregar");
            System.out.println("2. Mostrar");
            System.out.println("3. Ingresar al final");
            System.out.println("4. Ingresar al inicio");
            System.out.println("5. Encontrar el mayor número");
            System.out.println("6. Encontrar el menor número");
            System.out.println("7. Calcular el promedio");
            System.out.println("8. Ordenar");
            System.out.println("9. Eliminar por posición");
            System.out.println("0. Salir");
            System.out.print("Ingrese una opción: ");
            opcion = sc.nextInt();

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese el valor a agregar: ");
                    int valor = sc.nextInt();
                    lista.agregar(valor);
                    System.out.println("Elemento agregado correctamente");
                    break;
                case 2:
                    System.out.println("La lista es:");
                    lista.mostrar();
                    break;
                case 3:
                    System.out.print("Ingrese el valor a ingresar al final: ");
                    int valorFinal = sc.nextInt();
                    lista.ingresarAlFinal(valorFinal);
                    System.out.println("Elemento ingresado al final correctamente");
                    break;
                case 4:
                    System.out.print("Ingrese el valor a ingresar al inicio: ");
                    int valorInicio = sc.nextInt();
                    lista.ingresarAlInicio(valorInicio);
                    System.out.println("Elemento ingresado al inicio correctamente");
                    break;
                case 5:
                    int mayor = lista.encontrarMayor();
                    if (mayor != Integer.MIN_VALUE) {
                        System.out.println("El mayor número es: " + mayor);
                    }
                    break;
                case 6:
                    int menor = lista.encontrarMenor();
                    if (menor != Integer.MAX_VALUE) {
                        System.out.println("El menor número es: " + menor);
                    }
                    break;
                case 7:
                    double promedio = lista.calcularPromedio();
                    System.out.println("El promedio es: " + promedio);
                    break;
                case 8:
                    lista.ordenar();
                    System.out.println("Lista ordenada correctamente");
                    break;
                case 9:
                    System.out.print("Ingrese la posición a eliminar: ");
                    int posicion = sc.nextInt();
                    lista.eliminarPorPosicion(posicion);
                    break;
                case 0:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción inválida");
                    break;
            }

            System.out.println();
        } while (opcion != 0);

        sc.close();
    }
}
~~~
