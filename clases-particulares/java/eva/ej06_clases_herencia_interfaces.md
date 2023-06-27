# Ejercicio 06 - Clases , herencia e interfaces

## Inventario de videojuegos

En este ejercicio, debes implementar un programa que simule un inventario de videojuegos. Debes utilizar herencia, interfaces, arrays y métodos de arrays para gestionar los items del inventario.

1. Crea una clase abstracta llamada `Item` con los siguientes atributos:
   - `nombre` (String): el nombre del item.
   - `precio` (int): el precio del item.

2. Implementa el método abstracto `usar()` en la clase `Item` que debe imprimir un mensaje genérico de uso del item.

3. Crea las siguientes clases que hereden de `Item`:
   - `Arma`: representa un arma y debe tener un atributo adicional `poder` (int) que indique la potencia del arma.
   - `Pocion`: representa una poción y debe tener un atributo adicional `curacion` (int) que indique la cantidad de curación que proporciona.

4. Implementa el método `usar()` en las clases hijas (`Arma` y `Pocion`) para mostrar un mensaje específico de uso para cada tipo de item.

5. Crea una interfaz llamada `ItemUsable` con un método `usar()` que represente los items que se pueden usar.

6. Implementa la interfaz `ItemUsable` en la clase `Pocion` para indicar que las pociones son items utilizables.

7. Crea una clase llamada `Inventario` con los siguientes atributos:
   - `items` (array de `Item`): representa los items del inventario.
   - `capacidad` (int): la capacidad máxima del inventario.
   - `numItems` (int): el número actual de items en el inventario.

8. Implementa el método `estaLleno()` en la clase `Inventario` que verifique si el inventario está lleno.

9. Implementa el método `agregarItem(Item item)` en la clase `Inventario` que agregue un item al inventario si hay espacio disponible.

10. Implementa el método `eliminarItem(int indice)` en la clase `Inventario` que elimine un item del inventario según su índice.

11. Implementa el método `mostrarItems()` en la clase `Inventario` que muestre los items presentes en el inventario.

12. En el método `main()`, crea instancias de diferentes items (al menos un arma y dos pociones) y agrégalos al inventario.

13. Muestra los items presentes en el inventario utilizando el método `mostrarItems()`.

14. Elimina uno de los items del inventario utilizando el método `eliminarItem()` y muestra los items actualizados.

~~~java
import java.util.Arrays;

interface ItemUsable {
    void usar();
}

abstract class Item {
    protected String nombre;
    protected int precio;

    public Item(String nombre, int precio) {
        this.nombre = nombre;
        this.precio = precio;
    }

    public abstract void usar();

    public String getNombre() {
        return nombre;
    }

    public int getPrecio() {
        return precio;
    }
}

class Arma extends Item {
    private int poder;

    public Arma(String nombre, int precio, int poder) {
        super(nombre, precio);
        this.poder = poder;
    }

    public int getPoder() {
        return poder;
    }

    @Override
    public void usar() {
        System.out.println("¡Has usado el arma " + nombre + "!");
    }
}

class Pocion extends Item implements ItemUsable {
    private int curacion;

    public Pocion(String nombre, int precio, int curacion) {
        super(nombre, precio);
        this.curacion = curacion;
    }

    public int getCuracion() {
        return curacion;
    }

    @Override
    public void usar() {
        System.out.println("¡Has usado la poción " + nombre + "!");
    }
}

class Inventario {
    private Item[] items;
    private int capacidad;
    private int numItems;

    public Inventario(int capacidad) {
        this.capacidad = capacidad;
        items = new Item[capacidad];
        numItems = 0;
    }

    public boolean estaLleno() {
        return numItems == capacidad;
    }

    public void agregarItem(Item item) {
        if (estaLleno()) {
            System.out.println("El inventario está lleno. No se puede agregar el item.");
        } else {
            items[numItems] = item;
            numItems++;
            System.out.println("Se ha agregado el item '" + item.getNombre() + "' al inventario.");
        }
    }

    public void eliminarItem(int indice) {
        if (indice >= 0 && indice < numItems) {
            Item itemEliminado = items[indice];
            items[indice] = null;
            System.arraycopy(items, indice + 1, items, indice, numItems - indice - 1);
            numItems--;
            System.out.println("Se ha eliminado el item '" + itemEliminado.getNombre() + "' del inventario.");
        } else {
            System.out.println("El índice especificado no es válido.");
        }
    }

    public void mostrarItems() {
        System.out.println("Inventario:");
        for (int i = 0; i < numItems; i++) {
            Item item = items[i];
            System.out.println((i + 1) + ". " + item.getNombre() + " (Precio: " + item.getPrecio() + ")");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Inventario inventario = new Inventario(5);

        Arma espada = new Arma("Espada", 100, 50);
        Pocion pocionCurativa = new Pocion("Poción curativa", 50, 50);
        Pocion pocionEnergia = new Pocion("Poción de energía", 30, 0);

        inventario.agregarItem(espada);
        inventario.agregarItem(pocionCurativa);
        inventario.agregarItem(pocionEnergia);

        inventario.mostrarItems();

        inventario.eliminarItem(1);

        inventario.mostrarItems();
    }
}
~~~
