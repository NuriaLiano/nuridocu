# Ejercicio 01 - Clases sencillas

## Gestión de una tienda de productos electrónicos

Desarrolla un programa de gestión para una tienda de productos electrónicos. El programa debe permitir al usuario realizar las siguientes operaciones:

- Agregar productos al inventario: El usuario podrá ingresar el nombre, precio y cantidad de un producto para agregarlo al inventario de la tienda.
- Mostrar inventario: El programa deberá mostrar en pantalla la lista de productos disponibles en el inventario, indicando su nombre, precio y cantidad.
- Vender producto: El usuario podrá ingresar el nombre y la cantidad de un producto que desea vender. El programa verificará si hay suficiente stock disponible y actualizará la cantidad en el inventario en caso de una venta exitosa.
- Salir: El programa finalizará su ejecución.

~~~java
import java.util.ArrayList;
import java.util.Scanner;

class Producto {
    private String nombre;
    private double precio;
    private int cantidad;

    public Producto(String nombre, double precio, int cantidad) {
        this.nombre = nombre;
        this.precio = precio;
        this.cantidad = cantidad;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }
}

public class TiendaElectronica {
    private ArrayList<Producto> inventario;

    public TiendaElectronica() {
        inventario = new ArrayList<>();
    }

    public void agregarProducto(Producto producto) {
        inventario.add(producto);
    }

    public void mostrarInventario() {
        System.out.println("Inventario:");
        for (Producto producto : inventario) {
            System.out.println("Nombre: " + producto.getNombre());
            System.out.println("Precio: $" + producto.getPrecio());
            System.out.println("Cantidad: " + producto.getCantidad());
            System.out.println("--------------------");
        }
    }

    public void venderProducto(String nombre, int cantidad) {
        for (Producto producto : inventario) {
            if (producto.getNombre().equalsIgnoreCase(nombre)) {
                if (producto.getCantidad() >= cantidad) {
                    producto.setCantidad(producto.getCantidad() - cantidad);
                    System.out.println("Venta realizada con éxito.");
                    return;
                } else {
                    System.out.println("No hay suficiente stock disponible.");
                    return;
                }
            }
        }
        System.out.println("El producto no existe en el inventario.");
    }

    public static void main(String[] args) {
        TiendaElectronica tienda = new TiendaElectronica();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("1. Agregar producto");
            System.out.println("2. Mostrar inventario");
            System.out.println("3. Vender producto");
            System.out.println("4. Salir");
            System.out.print("Ingrese una opción: ");
            int opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese el nombre del producto: ");
                    String nombre = scanner.next();
                    System.out.print("Ingrese el precio del producto: ");
                    double precio = scanner.nextDouble();
                    System.out.print("Ingrese la cantidad disponible: ");
                    int cantidad = scanner.nextInt();
                    Producto producto = new Producto(nombre, precio, cantidad);
                    tienda.agregarProducto(producto);
                    System.out.println("Producto agregado correctamente.");
                    break;
                case 2:
                    tienda.mostrarInventario();
                    break;
                case 3:
                    System.out.print("Ingrese el nombre del producto a vender: ");
                    String nombreProducto = scanner.next();
                    System.out.print("Ingrese la cantidad a vender: ");
                    int cantidadVenta = scanner.nextInt();
                    tienda.venderProducto(nombreProducto, cantidadVenta);
                    break;
                case 4:
                    System.out.println("Gracias por usar el programa. ¡Hasta luego!");
                    System.exit(0);
                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
            }
        }
    }
}
~~~

