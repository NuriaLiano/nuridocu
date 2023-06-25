# Ejercicio básico clases

> :pencil: **NOTA** Este ejercicio es básico para entender la estructura de las clases en JAVA

En este ejercicio, debes implementar una clase Persona que represente a una persona con su nombre y edad. Luego, debes crear un programa en Java que utilice objetos, funciones y colecciones para almacenar y manipular información de personas.

- Los atributos de la clase persona tienen que ser sólamente accesibles desde la propia clase.
- Es necesario un array de objetos de capacidad 3
- La función 'imprimirPersonas' recibe como parametro el array y devolverá por pantalla el nombre y la edad de todas las personas

~~~java
import java.util.ArrayList;

class Persona {
    private String nombre;
    private int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }
}

public class EjercicioJava {
    public static void main(String[] args) {
        // Crear un array de objetos Persona
        Persona[] personas = new Persona[3];
        personas[0] = new Persona("Juan", 25);
        personas[1] = new Persona("María", 30);
        personas[2] = new Persona("Pedro", 40);

        // Pasar el array como parámetro a una función
        imprimirPersonas(personas);

        // Crear un ArrayList de objetos Persona
        ArrayList<Persona> listaPersonas = new ArrayList<>();
        listaPersonas.add(new Persona("Ana", 35));
        listaPersonas.add(new Persona("Luis", 28));
        listaPersonas.add(new Persona("Laura", 42));

        // Pasar el ArrayList como parámetro a una función
        imprimirPersonas(listaPersonas);
    }

    // Función que recibe un array de objetos Persona como parámetro
    public static void imprimirPersonas(Persona[] personas) {
        for (Persona persona : personas) {
            System.out.println("Nombre: " + persona.getNombre() + ", Edad: " + persona.getEdad());
        }
    }
}
~~~