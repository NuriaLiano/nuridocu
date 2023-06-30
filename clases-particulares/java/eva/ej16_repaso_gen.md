# Ejercicio 16 - Repaso general

## Crear un videojuego GTA

## Ejercicio: Gestión de Personajes en la saga de GTA

La misión es crear un sistema para gestionar los personajes jugables en la saga de GTA. Cada personaje tiene un nombre, una salud y una habilidad especial.

1. Crea una clase llamada `Personaje` con los siguientes atributos y métodos:
   - Atributos:
     - `nombre` (String): el nombre del personaje.
     - `salud` (int): la cantidad de salud del personaje.
   - Métodos:
     - `getNombre()`: devuelve el nombre del personaje.
     - `getSalud()`: devuelve la salud del personaje.
     - `setSalud(int salud)`: establece la salud del personaje.
     - `mostrarDatos()`: muestra los datos del personaje (nombre y salud).

2. Crea una interfaz llamada `Jugable` con el siguiente método:
   - `usarHabilidadEspecial()`: define el comportamiento de la habilidad especial del personaje.

3. Crea dos clases que hereden de `Personaje` e implementen la interfaz `Jugable`:
   - `Protagonista`: representa al protagonista del juego. Tiene una habilidad especial llamada "Modo Caos" que incrementa temporalmente su salud.
   - `Secundario`: representa a un personaje secundario. Tiene una habilidad especial llamada "Disfraz" que le permite pasar desapercibido durante un tiempo.

4. Crea una clase llamada `ListaPersonajes` que implemente una lista enlazada utilizando nodos. La lista debe tener los siguientes métodos:
   - `agregar(Personaje personaje)`: agrega un personaje a la lista.
   - `borrar(Personaje personaje)`: busca y elimina un personaje de la lista.
   - `mostrarPersonajes()`: muestra los datos de todos los personajes en la lista.
   - `contarPersonajes()`: cuenta el número de personajes en la lista.

### Instrucciones

1. Crea instancias de varios personajes (`Protagonista` y `Secundario`) con diferentes nombres y salud.
2. Agrega los personajes a la lista utilizando el método `agregar()`.
3. Llama al método `mostrarPersonajes()` para mostrar los datos de todos los personajes en la lista.
4. Llama al método `usarHabilidadEspecial()` para probar la habilidad especial de cada personaje.
5. Llama al método `borrar()` pasando un personaje para eliminarlo de la lista.
6. Llama al método `contarPersonajes()` para obtener el número de personajes restantes en la lista.

~~~java
// personaje.java
public class Personaje {
    private String nombre;
    private int salud;

    public Personaje(String nombre, int salud) {
        this.nombre = nombre;
        this.salud = salud;
    }

    public String getNombre() {
        return nombre;
    }

    public int getSalud() {
        return salud;
    }

    public void setSalud(int salud) {
        this.salud = salud;
    }

    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Salud: " + salud);
    }
}

//jugable.java
public interface Jugable {
    void usarHabilidadEspecial();
}

//protagonista.java
public class Protagonista extends Personaje implements Jugable {
    public Protagonista(String nombre, int salud) {
        super(nombre, salud);
    }

    @Override
    public void usarHabilidadEspecial() {
        System.out.println("Modo Caos activado. Salud incrementada.");
        setSalud(getSalud() + 10);
    }
}

//secundario.java
public class Secundario extends Personaje implements Jugable {
    public Secundario(String nombre, int salud) {
        super(nombre, salud);
    }

    @Override
    public void usarHabilidadEspecial() {
        System.out.println("Disfraz activado. Pasando desapercibido.");
        setSalud(getSalud() - 5);
    }
}

//nodo.java
public class Nodo {
    private Personaje personaje;
    private Nodo siguiente;

    public Nodo(Personaje personaje) {
        this.personaje = personaje;
        this.siguiente = null;
    }

    public Personaje getPersonaje() {
        return personaje;
    }

    public void setPersonaje(Personaje personaje) {
        this.personaje = personaje;
    }

    public Nodo getSiguiente() {
        return siguiente;
    }

    public void setSiguiente(Nodo siguiente) {
        this.siguiente = siguiente;
    }
}

//listaPersonajes.java
public class ListaPersonajes {
    private Nodo cabeza;
    private int contador;

    public ListaPersonajes() {
        cabeza = null;
        contador = 0;
    }

    public void agregar(Personaje personaje) {
        Nodo nuevoNodo = new Nodo(personaje);
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

    public void borrar(Personaje personaje) {
        if (cabeza != null) {
            if (cabeza.getPersonaje().equals(personaje)) {
                cabeza = cabeza.getSiguiente();
                contador--;
                return;
            }
            Nodo nodoActual = cabeza;
            while (nodoActual.getSiguiente() != null) {
                if (nodoActual.getSiguiente().getPersonaje().equals(personaje)) {
                    nodoActual.setSiguiente(nodoActual.getSiguiente().getSiguiente());
                    contador--;
                    return;
                }
                nodoActual = nodoActual.getSiguiente();
            }
        }
    }
    /*
    Comprueba si la lista no está vacía verificando si el nodo cabeza no es nulo.
    Si la lista no está vacía, se realiza una comprobación adicional para ver si el personaje a borrar se encuentra en el nodo cabeza. Esto se hace utilizando el método equals() para comparar el personaje del nodo cabeza con el personaje pasado como argumento.
        Si el personaje a borrar coincide con el personaje en el nodo cabeza, se actualiza el nodo cabeza para que apunte al siguiente nodo en la lista (es decir, se elimina el nodo cabeza). También se decrementa el contador de personajes en la lista y se finaliza la función.
    Si el personaje a borrar no coincide con el personaje en el nodo cabeza, se crea un nodo temporal llamado nodoActual que apunta al nodo cabeza.
    Se inicia un bucle mientras el siguiente nodo de nodoActual no sea nulo.
    En cada iteración del bucle, se verifica si el personaje a borrar coincide con el personaje en el siguiente nodo de nodoActual.
        Si hay una coincidencia, se actualiza el enlace del nodo actual para que salte el siguiente nodo (es decir, se elimina el siguiente nodo de la lista). También se decrementa el contador de personajes en la lista y se finaliza la función.
    Si no se encuentra una coincidencia en el nodo actual, se actualiza nodoActual para que apunte al siguiente nodo en la lista y se continúa con la siguiente iteración del bucle.
    Si se completa el bucle sin encontrar una coincidencia, significa que el personaje a borrar no está presente en la lista.
    */


    public void mostrarPersonajes() {
        Nodo nodoActual = cabeza;
        while (nodoActual != null) {
            nodoActual.getPersonaje().mostrarDatos();
            nodoActual = nodoActual.getSiguiente();
        }
    }

    public int contarPersonajes() {
        return contador;
    }
}
~~~
