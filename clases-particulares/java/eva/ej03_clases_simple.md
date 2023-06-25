# Ejercicio 03 - Clases sencillas

## Sistema de gestión para una biblioteca

- Agregar un libro: El usuario podrá ingresar el título, autor y año de publicación de un libro para agregarlo a la biblioteca.
- Mostrar todos los libros: El programa deberá mostrar en pantalla la lista de todos los libros disponibles en la biblioteca, indicando su título, autor y año de publicación.
- Buscar libros por autor: El usuario podrá ingresar el nombre de un autor y el programa mostrará en pantalla la lista de libros escritos por ese autor.
- Buscar libros por año de publicación: El usuario podrá ingresar un año y el programa mostrará en pantalla la lista de libros publicados en ese año.
- Salir: El programa finalizará su ejecución

~~~java
import java.util.Scanner;

class Libro {
    private String titulo;
    private String autor;
    private int anioPublicacion;

    public Libro(String titulo, String autor, int anioPublicacion) {
        this.titulo = titulo;
        this.autor = autor;
        this.anioPublicacion = anioPublicacion;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAnioPublicacion() {
        return anioPublicacion;
    }
}

public class SistemaGestionBiblioteca {
    private Libro[] libros;
    private int contadorLibros;

    public SistemaGestionBiblioteca(int capacidad) {
        libros = new Libro[capacidad];
        contadorLibros = 0;
    }

    public void agregarLibro(Libro libro) {
        if (contadorLibros < libros.length) {
            libros[contadorLibros] = libro;
            contadorLibros++;
            System.out.println("Libro agregado correctamente.");
        } else {
            System.out.println("La biblioteca está llena. No es posible agregar más libros.");
        }
    }

    public void mostrarTodosLosLibros() {
        if (contadorLibros == 0) {
            System.out.println("No hay libros en la biblioteca.");
        } else {
            System.out.println("Lista de libros:");
            for (int i = 0; i < contadorLibros; i++) {
                System.out.println("Título: " + libros[i].getTitulo());
                System.out.println("Autor: " + libros[i].getAutor());
                System.out.println("Año de publicación: " + libros[i].getAnioPublicacion());
                System.out.println("--------------------");
            }
        }
    }

    public void buscarLibrosPorAutor(String autor) {
        boolean librosEncontrados = false;
        System.out.println("Libros escritos por " + autor + ":");
        for (int i = 0; i < contadorLibros; i++) {
            if (libros[i].getAutor().equalsIgnoreCase(autor)) {
                System.out.println("Título: " + libros[i].getTitulo());
                System.out.println("Año de publicación: " + libros[i].getAnioPublicacion());
                System.out.println("--------------------");
                librosEncontrados = true;
            }
        }
        if (!librosEncontrados) {
            System.out.println("No se encontraron libros escritos por " + autor + ".");
        }
    }

    public void buscarLibrosPorAnioPublicacion(int anioPublicacion) {
        boolean librosEncontrados = false;
        System.out.println("Libros publicados en " + anioPublicacion + ":");
        for (int i = 0; i < contadorLibros; i++) {
            if (libros[i].getAnioPublicacion() == anioPublicacion) {
                System.out.println("Título: " + libros[i].getTitulo());
                System.out.println("Autor: " + libros[i].getAutor());
                System.out.println("--------------------");
                librosEncontrados = true;
            }
        }
        if (!librosEncontrados) {
            System.out.println("No se encontraron libros publicados en " + anioPublicacion + ".");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        SistemaGestionBiblioteca sistema = new SistemaGestionBiblioteca(50);

        while (true) {
            System.out.println("1. Agregar un libro");
            System.out.println("2. Mostrar todos los libros");
            System.out.println("3. Buscar libros por autor");
            System.out.println("4. Buscar libros por año de publicación");
            System.out.println("5. Salir");
            System.out.print("Ingrese una opción: ");
            int opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    scanner.nextLine(); // Limpiar el buffer
                    System.out.print("Ingrese el título del libro: ");
                    String titulo = scanner.nextLine();
                    System.out.print("Ingrese el autor del libro: ");
                    String autor = scanner.nextLine();
                    System.out.print("Ingrese el año de publicación del libro: ");
                    int anioPublicacion = scanner.nextInt();
                    sistema.agregarLibro(new Libro(titulo, autor, anioPublicacion));
                    break;
                case 2:
                    sistema.mostrarTodosLosLibros();
                    break;
                case 3:
                    scanner.nextLine(); // Limpiar el buffer
                    System.out.print("Ingrese el nombre del autor: ");
                    String nombreAutor = scanner.nextLine();
                    sistema.buscarLibrosPorAutor(nombreAutor);
                    break;
                case 4:
                    System.out.print("Ingrese el año de publicación: ");
                    int anio = scanner.nextInt();
                    sistema.buscarLibrosPorAnioPublicacion(anio);
                    break;
                case 5:
                    System.out.println("Gracias por utilizar el sistema de gestión de biblioteca. ¡Hasta luego!");
                    System.exit(0);
                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
            }
        }
    }
}
~~~