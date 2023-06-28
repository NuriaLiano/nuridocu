# Ejercicio 08 -  explicación listas y nodos

Escribe una clase **Libro** que tenga las siguientes **propiedades**: **titulo, autor e isbn**. La clase debe tener un **constructor** que acepte los valores para **todas las propiedades** y métodos de acceso (**getters**) y modificación (**setters**) para cada propiedad.

A continuación, crea una **clase Lista** que representa una **lista enlazada** de libros. La clase Lista debe tener una **clase interna Nodo** que tiene una **propiedad libro de tipo Libro y una propiedad siguiente de tipo Nodo.** La clase Lista debe tener las siguientes funcionalidades:

- insertarPrincipio: recibe un objeto Libro y lo inserta al principio de la lista.
- insertarFinal: recibe un objeto Libro y lo inserta al final de la lista.
- insertarDespues: recibe un índice n y un objeto Libro, e inserta el libro después del índice n en la lista.
- obtener: recibe un índice n y devuelve el libro en esa posición de la lista.
- contar: devuelve la cantidad de libros en la lista.
- estaVacia: devuelve un valor booleano que indica si la lista está vacía.
- eliminarPrincipio: elimina el primer libro de la lista.
- eliminarUltimo: elimina el último libro de la lista.
- eliminarLibro: recibe un índice n y elimina el libro en esa posición de la lista.

Implementa las clases Libro y Lista según la descripción dada y realiza pruebas para verificar que las funcionalidades de la lista enlazada se comporten correctamente.

~~~java
//libro.java
public class Libro{
    private String titulo;
    private String autor;
    private String isbn;

    public Libro (String titulo, String autor, String isbn){
        this.titulo = titulo;
        this.autor = autor;
        this.isbn = isbn;
    }

    public String getTitulo(){
        return titulo;
    }
    public void setTitulo(String titulo){
        this.titulo = titulo;
    }
    public String getAutor(){
        return autor;
    }
    public void setAutor(String autor){
        this.autor = autor;
    }
    public String getIsbn(){
        return isbn;
    }
    public void setIsbn(String isbn){
        this.isbn = isbn;
    }
}

//lista.java
public class Lista{
    private Nodo cabeza = null;
    private int longitud = 0;


    private class Nodo {
        public Libro libro;
        public Nodo siguiente = null;

        public Nodo(Libro libro){
            this.libro = libro;
        }
    }

    public void insertarPrincipio (Libro libro){
        Nodo nodo = new Nodo (libro);
        nodo.siguiente = cabeza;
        cabeza = nodo;
        longitud++;
    }

    public void insertarFinal(Libro libro){
        Nodo nodo = new Nodo (libro);
        
        if (cabeza == null){
            cabeza = nodo;
        }else{
            Nodo puntero = cabeza;
            while (puntero.siguiente != null){
                puntero = puntero.siguiente;
            }
            puntero.siguiente = nodo;
        }
        longitud++;
    }

    public void insertarDespues(int n, Libro libro){
        Nodo nodo = new Nodo (libro);
        if(cabeza == null){
            cabeza = nodo;
        }else{
            Nodo puntero = cabeza;
            int contador = 0;
            while (contador <n && puntero.siguiente !=null){
                puntero = puntero.siguiente;
                contador++;
            }
            nodo.siguiente = puntero.siguiente;
            puntero.siguiente = nodo;
        }
        longitud++;
    }

    public Libro obtener(int n){
        if(cabeza == null){
            return null;
        }else{
            while (contador <n && puntero.siguiente !=null){
                puntero = puntero.siguiente;
                contador++;
            }
            if(contador != n){
                return null;
            }else{
                return puntero.libro;
            }
        }
    }

    public int contar(){
        return longitud;
    }

    public estaVacia(){
        return cabeza == null;
    }

    public eliminarPrincipio(){
        if(cabeza != null){
            Nodo primer = cabeza;
            cabeza = cabeza.siguiente;
            //en java el recolector de basura se ocupa de liberar memoria
            //actualizar puntero
            primer.siguiente = null;
            longitud--;
        }
    }

    public void eliminarUltimo(){
        if (cabeza != null){
            if(cabeza.siguiente == null){
                cabeza = null;
            }else{
                Nodo puntero = cabeza;
                while(puntero.siguiente.siguiente != null){
                    puntero = puntero.siguiente;
                }
                puntero.siguiente = null;
                longitud--;
            }
            
        }
    }

    public void eliminarLibro(int n){
        if(cabeza != null){
            if(n == 0){
                Nodo primer = cabeza;
                cabeza = cabeza.siguiente;
                primer.siguiente = null;
                longitud--;
            }else if (n < longitud){
                Nodo puntero = cabeza;
                int contador = 0;
                while(contador >(n -1)){
                    puntero = puntero.siguiente;
                    contador++;
                }
                Nodo temporal = puntero.siguiente;
                puntero.siguiente = temporal.siguiente;
                temporal.siguiente = null;
                longitud--;
            }
            
        }
    }
}
~~~
