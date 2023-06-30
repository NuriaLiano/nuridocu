# Ejercicio 17 - Repaso general

## Parques de Atracciones de Europa

Se desea crear un sistema para gestionar los parques de atracciones más famosos de Europa. Cada parque tiene un nombre, una ubicación y una lista de atracciones.

1. Crea una clase llamada `ParqueAtracciones` con los siguientes atributos y métodos:
   - Atributos:
     - `nombre` (String): el nombre del parque.
     - `ubicacion` (String): la ubicación del parque.
   - Métodos:
     - `getNombre()`: devuelve el nombre del parque.
     - `getUbicacion()`: devuelve la ubicación del parque.
     - `mostrarInformacion()`: muestra la información del parque (nombre y ubicación).

2. Crea una clase `ParqueTematico` que herede de `ParqueAtracciones`. Esta clase representa un parque temático y tiene un atributo adicional:
   - Atributo:
     - `tematica` (String): la temática del parque temático.
   - Métodos:
     - `getTematica()`: devuelve la temática del parque temático.

3. Crea una clase `ParqueAcuatico` que herede de `ParqueAtracciones`. Esta clase representa un parque acuático y tiene un atributo adicional:
   - Atributo:
     - `cantidadPiscinas` (int): la cantidad de piscinas en el parque acuático.
   - Métodos:
     - `getCantidadPiscinas()`: devuelve la cantidad de piscinas en el parque acuático.

4. Crea una clase llamada `Atraccion` con los siguientes atributos y métodos:
   - Atributos:
     - `nombre` (String): el nombre de la atracción.
     - `tipo` (String): el tipo de atracción (por ejemplo, montaña rusa, caída libre, etc.).
   - Métodos:
     - `getNombre()`: devuelve el nombre de la atracción.
     - `getTipo()`: devuelve el tipo de atracción.

5. Crea una clase llamada `ListaAtracciones` que implemente una lista enlazada utilizando nodos. La lista debe tener los siguientes métodos:
   - `agregar(Atraccion atraccion)`: agrega una atracción a la lista.
   - `eliminar(Atraccion atraccion)`: busca y elimina una atracción de la lista.
   - `mostrarAtracciones()`: muestra la información de todas las atracciones en la lista.
   - `contarAtracciones()`: cuenta el número de atracciones en la lista.

### Instrucciones

1. Crea instancias de varios parques temáticos y parques acuáticos con diferentes nombres, ubicaciones y características específicas.
2. Agrega atracciones a los parques utilizando el método `agregar()` de la lista de atracciones.
3. Llama al método `mostrarInformacion()` de cada parque para mostrar su información.
4. Llama al método `mostrarAtracciones()` de la lista de atracciones para mostrar las atracciones de cada parque.
5. Llama al método `contarAtracciones()` para obtener el número total de atracciones en cada parque.
6. Utiliza los métodos adicionales de la lista de atracciones (`eliminar()` y `contarAtracciones()`) para gestionar las atracciones de los parques.

~~~java
// Clase ParqueAtracciones
public class ParqueAtracciones {
    private String nombre;
    private String ubicacion;

    public ParqueAtracciones(String nombre, String ubicacion) {
        this.nombre = nombre;
        this.ubicacion = ubicacion;
    }

    public String getNombre() {
        return nombre;
    }

    public String getUbicacion() {
        return ubicacion;
    }

    public void mostrarInformacion() {
        System.out.println("Nombre del parque: " + nombre);
        System.out.println("Ubicación: " + ubicacion);
    }
}

// Clase ParqueTematico
public class ParqueTematico extends ParqueAtracciones {
    private String tematica;

    public ParqueTematico(String nombre, String ubicacion, String tematica) {
        super(nombre, ubicacion);
        this.tematica = tematica;
    }

    public String getTematica() {
        return tematica;
    }
}

// Clase ParqueAcuatico
public class ParqueAcuatico extends ParqueAtracciones {
    private int cantidadPiscinas;

    public ParqueAcuatico(String nombre, String ubicacion, int cantidadPiscinas) {
        super(nombre, ubicacion);
        this.cantidadPiscinas = cantidadPiscinas;
    }

    public int getCantidadPiscinas() {
        return cantidadPiscinas;
    }
}

// Clase Atraccion
public class Atraccion {
    private String nombre;
    private String tipo;

    public Atraccion(String nombre, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTipo() {
        return tipo;
    }
}

// Clase Nodo
public class Nodo {
    private Atraccion atraccion;
    private Nodo siguiente;

    public Nodo(Atraccion atraccion) {
        this.atraccion = atraccion;
        this.siguiente = null;
    }

    public Atraccion getAtraccion() {
        return atraccion;
    }

    public void setAtraccion(Atraccion atraccion) {
        this.atraccion = atraccion;
    }

    public Nodo getSiguiente() {
        return siguiente;
    }

    public void setSiguiente(Nodo siguiente) {
        this.siguiente = siguiente;
    }
}

// Clase ListaAtracciones
public class ListaAtracciones {
    private Nodo cabeza;
    private int contador;

    public ListaAtracciones() {
        cabeza = null;
        contador = 0;
    }

    public void agregar(Atraccion atraccion) {
        Nodo nuevoNodo = new Nodo(atraccion);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            Nodo nodoActual = cabeza;
            while (nodoActual.getSiguiente() != null) {
                nodoActual = nodoActual.getSiguiente();
            }
            nodoActual.setSiguiente(nuevoNodo);
        }
        contador++;
    }

    public void eliminar(Atraccion atraccion) {
        if (cabeza != null) {
            if (cabeza.getAtraccion().equals(atraccion)) {
                cabeza = cabeza.getSiguiente();
                contador--;
                return;
            }
            Nodo nodoActual = cabeza;
            while (nodoActual.getSiguiente() != null) {
                if (nodoActual.getSiguiente().getAtraccion().equals(atraccion)) {
                    nodoActual.setSiguiente(nodoActual.getSiguiente().getSiguiente());
                    contador--;
                    return;
                }
                nodoActual = nodoActual.getSiguiente();
            }
        }
    }

    public void mostrarAtracciones() {
        Nodo nodoActual = cabeza;
        while (nodoActual != null) {
            System.out.println("Nombre: " + nodoActual.getAtraccion().getNombre());
            System.out.println("Tipo: " + nodoActual.getAtraccion().getTipo());
            nodoActual = nodoActual.getSiguiente();
        }
    }

    public int contarAtracciones() {
        return contador;
    }
}

// Ejemplo de uso
public class Main {
    public static void main(String[] args) {
        // Crear parques temáticos y acuáticos
        ParqueTematico parqueTematico1 = new ParqueTematico("Parque Temático 1", "Ubicación 1", "Temática 1");
        ParqueTematico parqueTematico2 = new ParqueTematico("Parque Temático 2", "Ubicación 2", "Temática 2");

        ParqueAcuatico parqueAcuatico1 = new ParqueAcuatico("Parque Acuático 1", "Ubicación 3", 3);
        ParqueAcuatico parqueAcuatico2 = new ParqueAcuatico("Parque Acuático 2", "Ubicación 4", 5);

        // Crear atracciones y agregarlas a los parques
        Atraccion atraccion1 = new Atraccion("Atracción 1", "Tipo 1");
        Atraccion atraccion2 = new Atraccion("Atracción 2", "Tipo 2");
        Atraccion atraccion3 = new Atraccion("Atracción 3", "Tipo 3");
        Atraccion atraccion4 = new Atraccion("Atracción 4", "Tipo 4");

        ListaAtracciones listaAtracciones1 = new ListaAtracciones();
        listaAtracciones1.agregar(atraccion1);
        listaAtracciones1.agregar(atraccion2);

        ListaAtracciones listaAtracciones2 = new ListaAtracciones();
        listaAtracciones2.agregar(atraccion3);
        listaAtracciones2.agregar(atraccion4);

        // Mostrar información de los parques
        parqueTematico1.mostrarInformacion();
        System.out.println("Tema: " + parqueTematico1.getTematica());

        parqueTematico2.mostrarInformacion();
        System.out.println("Tema: " + parqueTematico2.getTematica());

        parqueAcuatico1.mostrarInformacion();
        System.out.println("Cantidad de piscinas: " + parqueAcuatico1.getCantidadPiscinas());

        parqueAcuatico2.mostrarInformacion();
        System.out.println("Cantidad de piscinas: " + parqueAcuatico2.getCantidadPiscinas());

        // Mostrar atracciones de los parques
        System.out.println("Atracciones en " + parqueTematico1.getNombre() + ":");
        listaAtracciones1.mostrarAtracciones();
        System.out.println("Número total de atracciones: " + listaAtracciones1.contarAtracciones());

        System.out.println("Atracciones en " + parqueTematico2.getNombre() + ":");
        listaAtracciones2.mostrarAtracciones();
        System.out.println("Número total de atracciones: " + listaAtracciones2.contarAtracciones());
    }
}
~~~