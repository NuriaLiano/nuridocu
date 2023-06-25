# Ejercicio 02 - Clases sencillas

## Gestión de un sistema de reservas de vuelos

Desarrolla un programa de gestión para un sistema de reservas de vuelos. El programa debe permitir a los usuarios realizar las siguientes operaciones:

- Consultar vuelos disponibles: El programa mostrará en pantalla la lista de vuelos disponibles, indicando el número de vuelo, origen, destino, hora de salida y plazas disponibles.
- Realizar una reserva: El usuario podrá seleccionar un vuelo y proporcionar su nombre y número de asientos deseados para realizar una reserva. El programa verificará si hay suficientes asientos disponibles y actualizará la disponibilidad del vuelo en caso de una reserva exitosa.
- Consultar reservas: El programa mostrará al usuario las reservas que ha realizado, indicando el número de vuelo, origen, destino, hora de salida y número de asientos reservados.
- Cancelar una reserva: El usuario podrá seleccionar una reserva para cancelarla. El programa actualizará la disponibilidad de asientos del vuelo correspondiente y eliminará la reserva de la lista.
- Salir: El programa finalizará su ejecución

~~~java
import java.util.ArrayList;
import java.util.Scanner;

class Vuelo {
    private String numeroVuelo;
    private String origen;
    private String destino;
    private String horaSalida;
    private int plazasDisponibles;

    public Vuelo(String numeroVuelo, String origen, String destino, String horaSalida, int plazasDisponibles) {
        this.numeroVuelo = numeroVuelo;
        this.origen = origen;
        this.destino = destino;
        this.horaSalida = horaSalida;
        this.plazasDisponibles = plazasDisponibles;
    }

    public String getNumeroVuelo() {
        return numeroVuelo;
    }

    public String getOrigen() {
        return origen;
    }

    public String getDestino() {
        return destino;
    }

    public String getHoraSalida() {
        return horaSalida;
    }

    public int getPlazasDisponibles() {
        return plazasDisponibles;
    }

    public void setPlazasDisponibles(int plazasDisponibles) {
        this.plazasDisponibles = plazasDisponibles;
    }
}

class Reserva {
    private String numeroVuelo;
    private String nombrePasajero;
    private int numAsientos;

    public Reserva(String numeroVuelo, String nombrePasajero, int numAsientos) {
        this.numeroVuelo = numeroVuelo;
        this.nombrePasajero = nombrePasajero;
        this.numAsientos = numAsientos;
    }

    public String getNumeroVuelo() {
        return numeroVuelo;
    }

    public String getNombrePasajero() {
        return nombrePasajero;
    }

    public int getNumAsientos() {
        return numAsientos;
    }
}

public class SistemaReservasVuelos {
    private ArrayList<Vuelo> vuelos;
    private ArrayList<Reserva> reservas;

    public SistemaReservasVuelos() {
        vuelos = new ArrayList<>();
        reservas = new ArrayList<>();
    }

    public void agregarVuelo(Vuelo vuelo) {
        vuelos.add(vuelo);
    }

    public void mostrarVuelosDisponibles() {
        System.out.println("Vuelos Disponibles:");
        for (Vuelo vuelo : vuelos) {
            System.out.println("Número de Vuelo: " + vuelo.getNumeroVuelo());
            System.out.println("Origen: " + vuelo.getOrigen());
            System.out.println("Destino: " + vuelo.getDestino());
            System.out.println("Hora de Salida: " + vuelo.getHoraSalida());
            System.out.println("Plazas Disponibles: " + vuelo.getPlazasDisponibles());
            System.out.println("--------------------");
        }
    }

    public void realizarReserva(String numeroVuelo, String nombrePasajero, int numAsientos) {
        for (Vuelo vuelo : vuelos) {
            if (vuelo.getNumeroVuelo().equalsIgnoreCase(numeroVuelo)) {
                if (vuelo.getPlazasDisponibles() >= numAsientos) {
                    Reserva reserva = new Reserva(numeroVuelo, nombrePasajero, numAsientos);
                    reservas.add(reserva);
                    vuelo.setPlazasDisponibles(vuelo.getPlazasDisponibles() - numAsientos);
                    System.out.println("Reserva realizada con éxito.");
                    return;
                } else {
                    System.out.println("No hay suficientes plazas disponibles en el vuelo.");
                    return;
                }
            }
        }
        System.out.println("El número de vuelo ingresado no existe.");
    }

    public void mostrarReservas() {
        System.out.println("Reservas realizadas:");
        for (Reserva reserva : reservas) {
            System.out.println("Número de Vuelo: " + reserva.getNumeroVuelo());
            System.out.println("Origen: " + obtenerOrigenVuelo(reserva.getNumeroVuelo()));
            System.out.println("Destino: " + obtenerDestinoVuelo(reserva.getNumeroVuelo()));
            System.out.println("Hora de Salida: " + obtenerHoraSalidaVuelo(reserva.getNumeroVuelo()));
            System.out.println("Nombre del Pasajero: " + reserva.getNombrePasajero());
            System.out.println("Número de Asientos: " + reserva.getNumAsientos());
            System.out.println("--------------------");
        }
    }

    public void cancelarReserva(String numeroVuelo, String nombrePasajero) {
        for (Reserva reserva : reservas) {
            if (reserva.getNumeroVuelo().equalsIgnoreCase(numeroVuelo) && reserva.getNombrePasajero().equalsIgnoreCase(nombrePasajero)) {
                reservas.remove(reserva);
                actualizarPlazasDisponibles(numeroVuelo, reserva.getNumAsientos());
                System.out.println("Reserva cancelada con éxito.");
                return;
            }
        }
        System.out.println("La reserva especificada no existe.");
    }

    private void actualizarPlazasDisponibles(String numeroVuelo, int numAsientos) {
        for (Vuelo vuelo : vuelos) {
            if (vuelo.getNumeroVuelo().equalsIgnoreCase(numeroVuelo)) {
                vuelo.setPlazasDisponibles(vuelo.getPlazasDisponibles() + numAsientos);
                return;
            }
        }
    }

    private String obtenerOrigenVuelo(String numeroVuelo) {
        for (Vuelo vuelo : vuelos) {
            if (vuelo.getNumeroVuelo().equalsIgnoreCase(numeroVuelo)) {
                return vuelo.getOrigen();
            }
        }
        return "";
    }

    private String obtenerDestinoVuelo(String numeroVuelo) {
        for (Vuelo vuelo : vuelos) {
            if (vuelo.getNumeroVuelo().equalsIgnoreCase(numeroVuelo)) {
                return vuelo.getDestino();
            }
        }
        return "";
    }

    private String obtenerHoraSalidaVuelo(String numeroVuelo) {
        for (Vuelo vuelo : vuelos) {
            if (vuelo.getNumeroVuelo().equalsIgnoreCase(numeroVuelo)) {
                return vuelo.getHoraSalida();
            }
        }
        return "";
    }

    public static void main(String[] args) {
        SistemaReservasVuelos sistema = new SistemaReservasVuelos();
        Scanner scanner = new Scanner(System.in);

        sistema.agregarVuelo(new Vuelo("FL123", "Londres", "Nueva York", "10:00", 100));
        sistema.agregarVuelo(new Vuelo("FL456", "Madrid", "París", "12:30", 80));
        sistema.agregarVuelo(new Vuelo("FL789", "Tokio", "Sídney", "14:45", 150));

        while (true) {
            System.out.println("1. Consultar vuelos disponibles");
            System.out.println("2. Realizar una reserva");
            System.out.println("3. Consultar reservas");
            System.out.println("4. Cancelar una reserva");
            System.out.println("5. Salir");
            System.out.print("Ingrese una opción: ");
            int opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    sistema.mostrarVuelosDisponibles();
                    break;
                case 2:
                    System.out.print("Ingrese el número de vuelo: ");
                    String numeroVuelo = scanner.next();
                    System.out.print("Ingrese su nombre: ");
                    String nombrePasajero = scanner.next();
                    System.out.print("Ingrese el número de asientos a reservar: ");
                    int numAsientos = scanner.nextInt();
                    sistema.realizarReserva(numeroVuelo, nombrePasajero, numAsientos);
                    break;
                case 3:
                    sistema.mostrarReservas();
                    break;
                case 4:
                    System.out.print("Ingrese el número de vuelo de la reserva a cancelar: ");
                    numeroVuelo = scanner.next();
                    System.out.print("Ingrese su nombre: ");
                    nombrePasajero = scanner.next();
                    sistema.cancelarReserva(numeroVuelo, nombrePasajero);
                    break;
                case 5:
                    System.out.println("Gracias por utilizar el sistema de reservas de vuelos. ¡Hasta luego!");
                    System.exit(0);
                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
            }
        }
    }
}
~~~
