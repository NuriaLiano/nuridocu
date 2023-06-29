# Ejercicio 15 - Repaso general

## Generar una playlist

En este ejercicio, debes crear una aplicación que permita gestionar una playlist de reproducción. La playlist puede contener canciones y podcasts.

Debes implementar las siguientes clases:

### Interfaz Reproducible

- La interfaz `Reproducible` debe tener el método `reproducir()`, que será implementado por las clases `Cancion` y `Podcast`.

### Clase Cancion

- La clase `Cancion` representa una canción y debe tener los siguientes atributos:
  - `titulo` (String): el título de la canción.
  - `artista` (String): el nombre del artista.

- La clase `Cancion` debe implementar la interfaz `Reproducible` y sobrescribir el método `reproducir()` para mostrar el título y el artista de la canción.

### Clase Podcast

- La clase `Podcast` representa un podcast y debe tener los siguientes atributos:
  - `titulo` (String): el título del podcast.
  - `host` (String): el nombre del presentador del podcast.

- La clase `Podcast` debe implementar la interfaz `Reproducible` y sobrescribir el método `reproducir()` para mostrar el título y el host del podcast.

### Clase Playlist

- La clase `Playlist` representa una lista de reproducción y debe tener los siguientes atributos:
  - `elementos` (array de tipo `Reproducible`): el arreglo que contiene los elementos reproducibles de la playlist.

- La clase `Playlist` debe tener el método `reproducirTodo()`, que recorre el arreglo de elementos y llama al método `reproducir()` de cada elemento.

En el método principal (`main()`), debes crear instancias de canciones y podcasts, agregarlos a un arreglo de tipo `Reproducible` y luego crear una instancia de `Playlist` con ese arreglo. Finalmente, llama al método `reproducirTodo()` de la playlist para reproducir todos los elementos.

~~~java
// Interfaz reproducible
interface Reproducible {
    void reproducir();
}

// Clase padre para las canciones
class Cancion implements Reproducible {
    private String titulo;
    private String artista;

    public Cancion(String titulo, String artista) {
        this.titulo = titulo;
        this.artista = artista;
    }

    public void reproducir() {
        System.out.println("Reproduciendo la canción: " + titulo + " - " + artista);
    }
}

// Clase hija para los podcasts
class Podcast implements Reproducible {
    private String titulo;
    private String host;

    public Podcast(String titulo, String host) {
        this.titulo = titulo;
        this.host = host;
    }

    public void reproducir() {
        System.out.println("Reproduciendo el podcast: " + titulo + " - " + host);
    }
}

// Clase Playlist que contiene una lista de elementos reproducibles
class Playlist {
    private Reproducible[] elementos;

    public Playlist(Reproducible[] elementos) {
        this.elementos = elementos;
    }

    public void reproducirTodo() {
        System.out.println("Reproduciendo la playlist:");
        for (Reproducible elemento : elementos) {
            elemento.reproducir();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Cancion cancion1 = new Cancion("Shape of You", "Ed Sheeran");
        Cancion cancion2 = new Cancion("Bohemian Rhapsody", "Queen");
        Podcast podcast1 = new Podcast("The Joe Rogan Experience", "Joe Rogan");
        Podcast podcast2 = new Podcast("Serial", "Sarah Koenig");

        Reproducible[] elementos = {cancion1, cancion2, podcast1, podcast2};
        Playlist playlist = new Playlist(elementos);
        playlist.reproducirTodo();
    }
}
~~~
