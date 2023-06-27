# Ejercicio 04 - Clases con herencia

## Inventario para una tienda

1- Crea una clase Producto con los siguientes atributos:
    - id (entero): el identificador del producto.
    - nombre (cadena de caracteres): el nombre del producto.
    - precio (decimal): el precio del producto.
2. Crea dos clases adicionales que hereden de Producto:
    - Electronicos con un atributo adicional marca.
    - Libro con un atributo adicional autor.
3. Crea una clase Inventario que tenga una lista de productos y los siguientes métodos:
    - agregarProducto: recibe un objeto de tipo Producto y lo agrega al inventario.
    - eliminarProducto: recibe un identificador de producto y lo elimina del inventario.
    - verInventario: muestra por pantalla el inventario completo.
4. En el método main:
    - Crea una instancia de Inventario.
    - Crea algunos objetos de productos de diferentes tipos y agrega al inventario.
    - Muestra el inventario completo.
    - Elimina un producto del inventario por su identificador.
    - Muestra el inventario actualizado.

~~~java
import java.util.ArrayList;

class Producto {
    protected int id;
    protected String nombre;
    protected double precio;

    public Producto(int id, String nombre, double precio) {
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }

    @Override
    public String toString() {
        return "Producto [id=" + id + ", nombre=" + nombre + ", precio=" + precio + "]";
    }
}

class Electronico extends Producto {
    private String marca;

    public Electronico(int id, String nombre, double precio, String marca) {
        super(id, nombre, precio);
        this.marca = marca;
    }

    public String getMarca() {
        return marca;
    }

    @Override
    public String toString() {
        return "Electronico [id=" + id + ", nombre=" + nombre + ", precio=" + precio + ", marca=" + marca + "]";
    }
}

class Libro extends Producto {
    private String autor;

    public Libro(int id, String nombre, double precio, String autor) {
        super(id, nombre, precio);
        this.autor = autor;
    }

    public String getAutor() {
        return autor;
    }

    @Override
    public String toString() {
        return "Libro [id=" + id + ", nombre=" + nombre + ", precio=" + precio + ", autor=" + autor + "]";
    }
}

class Inventario {
    private ArrayList<Producto> productos;

    public Inventario() {
        productos = new ArrayList<>();
    }

    public void agregarProducto(Producto producto) {
        productos.add(producto);
    }

    public void eliminarProducto(int idProducto) {
        Producto productoEncontrado = null;
        for (Producto producto : productos) {
            if (producto.id == idProducto) {
                productoEncontrado = producto;
                break;
            }
        }
        if (productoEncontrado != null) {
            productos.remove(productoEncontrado);
            System.out.println("Producto eliminado: " + productoEncontrado.getNombre());
        } else {
            System.out.println("Producto no encontrado.");
        }
    }

    public void mostrarInventario() {
        if (productos.isEmpty()) {
            System.out.println("El inventario está vacío.");
        } else {
            for (Producto producto : productos) {
                System.out.println(producto);
            }
        }
    }
}

public class Principal {
    public static void main(String[] args) {
        Inventario inventario = new Inventario();

        Electronico telefono = new Electronico(1, "Teléfono inteligente", 599.99, "Samsung");
        Libro novela = new Libro(2, "Matar a un ruiseñor", 14.99, "Harper Lee");
        Electronico laptop = new Electronico(3, "Laptop", 1299.99, "Apple");

        inventario.agregarProducto(telefono);
        inventario.agregarProducto(novela);
        inventario.agregarProducto(laptop);

        inventario.mostrarInventario();

        inventario.eliminarProducto(2);
        inventario.eliminarProducto(4);

        inventario.mostrarInventario();
    }
}
~~~
