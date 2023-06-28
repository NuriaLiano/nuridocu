# Ejercicio 12 - listas, nodos y clases

## La playlist

Se pide implementar una clase `Playlist` que represente una lista enlazada de canciones. Cada canción estará representada por la clase `Cancion`. La clase `Playlist` debe tener los siguientes métodos:

- `agregarCancion`: agrega una canción a la playlist.
- `mostrarPlaylist`: muestra por pantalla todas las canciones de la playlist.
- `eliminarCancion`: elimina una canción de la playlist según su título.
- `getLongitud`: devuelve la longitud actual de la playlist.

Implementa también una clase `Cancion` con los siguientes atributos:

- `titulo`: el título de la canción.
- `artista`: el artista de la canción.
- `duracion`: la duración de la canción en minutos.

En el método `main`, crea una instancia de `Playlist` y agrega algunas canciones. Luego, muestra la playlist, elimina una canción y muestra la playlist actualizada junto con la longitud de la misma.

~~~java
//cancion.java
public class Cancion {
    private String titulo;
    private String artista;
    private double duracion;

    public Cancion(String titulo, String artista, double duracion) {
        this.titulo = titulo;
        this.artista = artista;
        this.duracion = duracion;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getArtista() {
        return artista;
    }

    public double getDuracion() {
        return duracion;
    }

    @Override
    public String toString() {
        return "Cancion{" +
                "titulo='" + titulo + '\'' +
                ", artista='" + artista + '\'' +
                ", duracion=" + duracion +
                '}';
    }
}

//playlist.java
public class Playlist {
    private Nodo<Cancion> cabeza;
    private int longitud;

    public Playlist() {
        cabeza = null;
        longitud = 0;
    }

    public void agregarCancion(Cancion cancion) {
        Nodo<Cancion> nuevoNodo = new Nodo<>(cancion, null);

        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            Nodo<Cancion> puntero = cabeza;
            while (puntero.siguiente != null) {
                puntero = puntero.siguiente;
            }
            puntero.siguiente = nuevoNodo;
        }
        longitud++;
    }

    public void mostrarPlaylist() {
        Nodo<Cancion> puntero = cabeza;
        while (puntero != null) {
            System.out.println(puntero.elemento);
            puntero = puntero.siguiente;
        }
    }

    public void eliminarCancion(String titulo) {
        if (cabeza == null) {
            return;
        }

        if (cabeza.elemento.getTitulo().equals(titulo)) {
            cabeza = cabeza.siguiente;
            longitud--;
            return;
        }

        Nodo<Cancion> puntero = cabeza;
        while (puntero.siguiente != null) {
            if (puntero.siguiente.elemento.getTitulo().equals(titulo)) {
                puntero.siguiente = puntero.siguiente.siguiente;
                longitud--;
                return;
            }
            puntero = puntero.siguiente;
        }
    }

    public int getLongitud() {
        return longitud;
    }
}
//nodo.java
public class Nodo<E> {
    public E elemento;
    public Nodo<E> siguiente;

    public Nodo(E elemento, Nodo<E> siguiente) {
        this.elemento = elemento;
        this.siguiente = siguiente;
    }
}
//main.java
public class Main {
    public static void main(String[] args) {
        Playlist playlist = new Playlist();

        Cancion cancion1 = new Cancion("Canción 1", "Artista 1", 3.5);
        Cancion cancion2 = new Cancion("Canción 2", "Artista 2", 4.2);
        Cancion cancion3 = new Cancion("Canción 3", "Artista 3", 3.8);

        playlist.agregarCancion(cancion1);
        playlist.agregarCancion(cancion2);
        playlist.agregarCancion(cancion3);

        System.out.println("Playlist actual:");
        playlist.mostrarPlaylist();

        System.out.println("Longitud de la playlist: " + playlist.getLongitud());

        System.out.println("Eliminando la canción 'Canción 2'");
        playlist.eliminarCancion("Canción 2");

        System.out.println("Playlist actualizada:");
        playlist.mostrarPlaylist();

        System.out.println("Longitud de la playlist: " + playlist.getLongitud());
    }
}
~~~