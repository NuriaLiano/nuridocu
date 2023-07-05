
# Ejercicio 19 - Repaso general

## Gestión de Envíos en una Empresa de Correos

Se desea crear un sistema para gestionar los envíos en una empresa de correos. Cada envío tiene un remitente, un destinatario y un peso en kilogramos. Los envíos pueden ser de dos tipos: envíos normales y envíos urgentes.

1. Crea una clase llamada `Envio` con los siguientes atributos y métodos:
   - Atributos:
     - `remitente` (String): el remitente del envío.
     - `destinatario` (String): el destinatario del envío.
     - `peso` (double): el peso en kilogramos del envío.
   - Métodos:
     - `getRemitente()`: devuelve el remitente del envío.
     - `getDestinatario()`: devuelve el destinatario del envío.
     - `getPeso()`: devuelve el peso del envío.
     - `calcularCosto()`: calcula y devuelve el costo del envío.

2. Crea una interfaz llamada `EmpresaCorreos` con los siguientes métodos:
   - `agregarEnvio(Envio envio)`: agrega un envío a la lista de envíos de la empresa.
   - `agregarEnvioAlPrincipio(Envio envio)`: agrega un envío al principio de la lista de envíos.
   - `agregarEnvioAlFinal(Envio envio)`: agrega un envío al final de la lista de envíos.
   - `agregarEnvioEnPosicion(Envio envio, int posicion)`: agrega un envío en una posición específica de la lista de envíos.
   - `eliminarEnvioAlPrincipio()`: elimina el primer envío de la lista de envíos.
   - `eliminarEnvioAlFinal()`: elimina el último envío de la lista de envíos.
   - `eliminarEnvio(Envio envio)`: busca y elimina un envío específico de la lista de envíos.
   - `mostrarEnvios()`: muestra la información de todos los envíos de la lista.
   - `calcularCostoEnvios()`: calcula y muestra el costo total de todos los envíos.

3. Crea una clase llamada `EnvioNormal` que herede de la clase `Envio` y represente un envío normal. Esta clase debe implementar el método `calcularCosto()` para calcular el costo del envío normal.

4. Crea una clase llamada `EnvioUrgente` que herede de la clase `Envio` y represente un envío urgente. Esta clase debe implementar el método `calcularCosto()` para calcular el costo del envío urgente, que incluye una tarifa adicional.

5. Implementa la clase `ListaEnvios` que utiliza una lista enlazada de nodos para gestionar los envíos en la empresa. La clase debe implementar todos los métodos de la interfaz `EmpresaCorreos`.

### Instrucciones

1. Crea instancias de la empresa de correos y varios envíos normales y urgentes con diferentes remitentes, destinatarios y pesos.
2. Utiliza los métodos de la empresa de correos para agregar envíos a la lista de envíos en diferentes posiciones, al principio, al final y en posiciones específicas.
3. Llama al método `mostrarEnvios()` para mostrar la información de todos los envíos en la lista.
4. Llama al método `calcularCostoEnvios()` para calcular y mostrar el costo total de todos los envíos en la lista.
5. Utiliza los métodos adicionales de la lista de envíos (`eliminarEnvio()`, `eliminarEnvioAlPrincipio()`, `eliminarEnvioAlFinal()`) para gestionar los envíos de la empresa de correos.

~~~java
import java.util.Scanner;

// Interfaz para los métodos comunes de una empresa de correos
interface EmpresaCorreos {
    void agregarEnvio(Envio envio);
    void agregarEnvioAlPrincipio(Envio envio);
    void agregarEnvioAlFinal(Envio envio);
    void agregarEnvioEnPosicion(Envio envio, int posicion);
    void eliminarEnvioAlPrincipio();
    void eliminarEnvioAlFinal();
    void eliminarEnvio(Envio envio);
    void mostrarEnvios();
    void calcularCostoEnvios();
}

// Clase base abstracta para representar un envío
class Envio {
    protected String remitente;
    protected String destinatario;
    protected double peso;

    public Envio(String remitente, String destinatario, double peso) {
        this.remitente = remitente;
        this.destinatario = destinatario;
        this.peso = peso;
    }
    public String getRemitente() {
        return remitente;
    }

    public String getDestinatario() {
        return destinatario;
    }

    public double getPeso() {
        return peso;
    }

    public double calcularCosto() {
        return peso * 2.5; // Costo base por kilogramo
    }

    @Override
    public String toString() {
        return "Remitente: " + remitente + ", Destinatario: " + destinatario + ", Peso: " + peso + " kg";
    }
}

// Clase para representar un envío normal
class EnvioNormal extends Envio {
    public EnvioNormal(String remitente, String destinatario, double peso) {
        super(remitente, destinatario, peso);
    }
    @Override
    public double calcularCosto() {
        // Implementa el cálculo del costo del envío normal aquí
        // Puedes usar una fórmula específica para el envío normal
        // Por ejemplo:
        double costo = getPeso() * 5.0; // Cálculo simple basado en el peso del envío normal
        return costo;
    }
}

// Clase para representar un envío urgente
class EnvioUrgente extends Envio {
    private int nivelUrgencia;

    public EnvioUrgente(String remitente, String destinatario, double peso, int nivelUrgencia) {
        super(remitente, destinatario, peso);
        this.nivelUrgencia = nivelUrgencia;
    }

    @Override
    public double calcularCosto() {
        // Incrementamos el costo base por kilogramo según el nivel de urgencia
        return super.calcularCosto() + (nivelUrgencia * 10);
    }

    @Override
    public String toString() {
        return super.toString() + ", Nivel de urgencia: " + nivelUrgencia;
    }
}

// Clase para representar un nodo de la lista enlazada
class Nodo {
    private Envio envio;
    private Nodo siguiente;

    public Nodo(Envio envio) {
        this.envio = envio;
        this.siguiente = null;
    }

    public Envio getEnvio() {
        return envio;
    }

    public void setSiguiente(Nodo siguiente) {
        this.siguiente = siguiente;
    }

    public Nodo getSiguiente() {
        return siguiente;
    }
}

// Clase para representar la empresa de correos
class EmpresaCorreosImpl implements EmpresaCorreos {
    private Nodo cabeza;

    public EmpresaCorreosImpl() {
        cabeza = null;
    }

    @Override
    public void agregarEnvio(Envio envio) {
        agregarEnvioAlFinal(envio);
    }

    @Override
    public void agregarEnvioAlPrincipio(Envio envio) {
       Nodo nuevoNodo = new Nodo(valor);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        }
        System.out.println("Envío agregado al principio: " + envio.toString());
    }

    @Override
    public void agregarEnvioAlFinal(Envio envio) {
        Nodo nuevoNodo = new Nodo(envio);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            Nodo nodoActual = cabeza;
            while (nodoActual.getSiguiente() != null) {
                nodoActual = nodoActual.getSiguiente();
            }
            nodoActual.setSiguiente(nuevoNodo);
        }
        System.out.println("Envío agregado al final: " + envio.toString());
    }

    @Override
    public void agregarEnvioEnPosicion(Envio envio, int posicion) {
        if (posicion == 0) {
            agregarEnvioAlPrincipio(envio);
        } else {
            Nodo nuevoNodo = new Nodo(envio);
            if (cabeza == null) {
                cabeza = nuevoNodo;
            } else {
                Nodo nodoActual = cabeza;
                int contador = 1;
                while (nodoActual.getSiguiente() != null && contador < posicion) {
                    nodoActual = nodoActual.getSiguiente();
                    contador++;
                }
                nuevoNodo.setSiguiente(nodoActual.getSiguiente());
                nodoActual.setSiguiente(nuevoNodo);
            }
            System.out.println("Envío agregado en la posición " + posicion + ": " + envio.toString());
        }
    }

    @Override
    public void eliminarEnvioAlPrincipio() {
        if (cabeza == null) {
            System.out.println("No hay envíos registrados.");
        } else {
            // Nodo nodoEliminado = cabeza;
            cabeza = cabeza.getSiguiente();
            // System.out.println("Envío eliminado al principio: " + nodoEliminado.getEnvio().toString());
        }
    }

    @Override
    public void eliminarEnvioAlFinal() {
        if (cabeza == null) {
            System.out.println("No hay envíos registrados.");
        } else {
            Nodo nodoActual = cabeza;
            Nodo nodoAnterior = null;
            while (nodoActual.getSiguiente() != null) {
                nodoAnterior = nodoActual;
                nodoActual = nodoActual.getSiguiente();
            }
            if (nodoAnterior == null) {
                cabeza = null;
            } else {
                nodoAnterior.setSiguiente(null);
            }
            System.out.println("Envío eliminado al final: " + nodoActual.getEnvio().toString());
        }
    }

    @Override
    public void eliminarEnvio(Envio envio) {
        if (cabeza == null) {
            System.out.println("No hay envíos registrados.");
        } else {
            Nodo nodoActual = cabeza;
            Nodo nodoAnterior = null;
            while (nodoActual != null && !nodoActual.getEnvio().equals(envio)) {
                nodoAnterior = nodoActual;
                nodoActual = nodoActual.getSiguiente();
            }
            if (nodoActual == null) {
                System.out.println("El envío no existe en la lista.");
            } else {
                if (nodoAnterior == null) {
                    cabeza = cabeza.getSiguiente();
                } else {
                    nodoAnterior.setSiguiente(nodoActual.getSiguiente());
                }
                System.out.println("Envío eliminado: " + envio.toString());
            }
        }
    }

    @Override
    public void mostrarEnvios() {
        if (cabeza == null) {
            System.out.println("No hay envíos registrados.");
        } else {
            Nodo nodoActual = cabeza;
            while (nodoActual != null) {
                System.out.println(nodoActual.getEnvio().toString());
                nodoActual = nodoActual.getSiguiente();
            }
        }
    }

    @Override
    public void calcularCostoEnvios() {
        if (cabeza == null) {
            System.out.println("No hay envíos registrados.");
        } else {
            Nodo nodoActual = cabeza;
            double costoTotal = 0;
            while (nodoActual != null) {
                Envio envio = nodoActual.getEnvio();
                double costoEnvio = envio.calcularCosto();
                costoTotal += costoEnvio;
                System.out.println("Costo del envío: " + envio.toString() + " - $" + costoEnvio);
                nodoActual = nodoActual.getSiguiente();
            }
            System.out.println("Costo total de envíos: $" + costoTotal);
        }
    }
}

public class EjercicioCorreos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        EmpresaCorreos empresaCorreos = new EmpresaCorreosImpl();

        while (true) {
            System.out.println("---- Menú ----");
            System.out.println("1. Agregar envío normal");
            System.out.println("2. Agregar envío urgente");
            System.out.println("3. Agregar envío al principio");
            System.out.println("4. Agregar envío al final");
            System.out.println("5. Agregar envío en posición");
            System.out.println("6. Eliminar envío al principio");
            System.out.println("7. Eliminar envío al final");
            System.out.println("8. Eliminar envío por búsqueda");
            System.out.println("9. Mostrar envíos");
            System.out.println("10. Calcular costo de envíos");
            System.out.println("11. Salir");
            System.out.print("Seleccione una opción: ");
            int opcion = scanner.nextInt();
            scanner.nextLine(); // Consumir el salto de línea

            switch (opcion) {
                case 1:
                    System.out.print("Remitente: ");
                    String remitenteNormal = scanner.nextLine();
                    System.out.print("Destinatario: ");
                    String destinatarioNormal = scanner.nextLine();
                    System.out.print("Peso (kg): ");
                    double pesoNormal = scanner.nextDouble();
                    empresaCorreos.agregarEnvio(new EnvioNormal(remitenteNormal, destinatarioNormal, pesoNormal));
                    break;

                case 2:
                    System.out.print("Remitente: ");
                    String remitenteUrgente = scanner.nextLine();
                    System.out.print("Destinatario: ");
                    String destinatarioUrgente = scanner.nextLine();
                    System.out.print("Peso (kg): ");
                    double pesoUrgente = scanner.nextDouble();
                    System.out.print("Nivel de urgencia: ");
                    int nivelUrgencia = scanner.nextInt();
                    empresaCorreos.agregarEnvio(new EnvioUrgente(remitenteUrgente, destinatarioUrgente, pesoUrgente, nivelUrgencia));
                    break;

                case 3:
                    System.out.print("Remitente: ");
                    String remitenteAlPrincipio = scanner.nextLine();
                    System.out.print("Destinatario: ");
                    String destinatarioAlPrincipio = scanner.nextLine();
                    System.out.print("Peso (kg): ");
                    double pesoAlPrincipio = scanner.nextDouble();
                    empresaCorreos.agregarEnvioAlPrincipio(new EnvioNormal(remitenteAlPrincipio, destinatarioAlPrincipio, pesoAlPrincipio));
                    break;

                case 4:
                    System.out.print("Remitente: ");
                    String remitenteAlFinal = scanner.nextLine();
                    System.out.print("Destinatario: ");
                    String destinatarioAlFinal = scanner.nextLine();
                    System.out.print("Peso (kg): ");
                    double pesoAlFinal = scanner.nextDouble();
                    empresaCorreos.agregarEnvioAlFinal(new EnvioNormal(remitenteAlFinal, destinatarioAlFinal, pesoAlFinal));
                    break;

                case 5:
                    System.out.print("Remitente: ");
                    String remitenteEnPosicion = scanner.nextLine();
                    System.out.print("Destinatario: ");
                    String destinatarioEnPosicion = scanner.nextLine();
                    System.out.print("Peso (kg): ");
                    double pesoEnPosicion = scanner.nextDouble();
                    System.out.print("Posición: ");
                    int posicion = scanner.nextInt();
                    empresaCorreos.agregarEnvioEnPosicion(new EnvioNormal(remitenteEnPosicion, destinatarioEnPosicion, pesoEnPosicion), posicion);
                    break;

                case 6:
                    empresaCorreos.eliminarEnvioAlPrincipio();
                    break;

                case 7:
                    empresaCorreos.eliminarEnvioAlFinal();
                    break;

                case 8:
                    System.out.print("Remitente: ");
                    String remitenteBusqueda = scanner.nextLine();
                    System.out.print("Destinatario: ");
                    String destinatarioBusqueda = scanner.nextLine();
                    System.out.print("Peso (kg): ");
                    double pesoBusqueda = scanner.nextDouble();
                    empresaCorreos.eliminarEnvio(new EnvioNormal(remitenteBusqueda, destinatarioBusqueda, pesoBusqueda));
                    break;

                case 9:
                    empresaCorreos.mostrarEnvios();
                    break;

                case 10:
                    empresaCorreos.calcularCostoEnvios();
                    break;

                case 11:
                    System.out.println("Saliendo del programa...");
                    System.exit(0);

                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
                    break;
            }
            System.out.println();
        }
    }
}
~~~
