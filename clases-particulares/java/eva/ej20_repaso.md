~~~java
import java.util.ArrayList;

// Interfaz para calcular promedio
interface Calculable {
    double calcularPromedio();
}

// Clase base Alumno
class Alumno {
    private String nombre;
    private int edad;

    public Alumno(String nombre, int edad) {
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

// Clase derivada AlumnoNotas
class AlumnoNotas extends Alumno implements Calculable {
    private ArrayList<Double> notas;

    public AlumnoNotas(String nombre, int edad, ArrayList<Double> notas) {
        super(nombre, edad);
        this.notas = notas;
    }

    public ArrayList<Double> getNotas() {
        return notas;
    }

    public double calcularPromedio() {
        double sum = 0;
        for (double nota : notas) {
            sum += nota;
        }
        return sum / notas.size();
    }
}

public class AdministradorNotas {
    public static void main(String[] args) {
        // Crear algunos alumnos con sus respectivas notas
        ArrayList<Double> notas1 = new ArrayList<>();
        notas1.add(8.5);
        notas1.add(7.2);
        notas1.add(9.1);
        AlumnoNotas alumno1 = new AlumnoNotas("Juan", 20, notas1);

        ArrayList<Double> notas2 = new ArrayList<>();
        notas2.add(6.9);
        notas2.add(7.8);
        notas2.add(8.6);
        AlumnoNotas alumno2 = new AlumnoNotas("María", 21, notas2);

        // Mostrar información de los alumnos y sus promedios
        System.out.println("Alumno 1:");
        System.out.println("Nombre: " + alumno1.getNombre());
        System.out.println("Edad: " + alumno1.getEdad());
        System.out.println("Notas: " + alumno1.getNotas());
        System.out.println("Promedio: " + alumno1.calcularPromedio());

        System.out.println();

        System.out.println("Alumno 2:");
        System.out.println("Nombre: " + alumno2.getNombre());
        System.out.println("Edad: " + alumno2.getEdad());
        System.out.println("Notas: " + alumno2.getNotas());
        System.out.println("Promedio: " + alumno2.calcularPromedio());
    }
}
~~~