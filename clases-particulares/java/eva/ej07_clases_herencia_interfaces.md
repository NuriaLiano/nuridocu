# Ejercicio 07 - Clases, herencias e interfaces

## Ejercicio de Herencia en Java - Campo de Batalla

### Clase `Ser`

- La clase `Ser` es la clase base para los seres espirituales y no se puede instanciar directamente.
- Tiene un atributo protegido `nombre` que representa el nombre del ser.
- Tiene un constructor que recibe el nombre del ser y un método `getNombre()` para obtener el nombre.

### Clase `Ángel`

- La clase `Ángel` hereda de `Ser` y representa a un ángel.
- Tiene un atributo protegido `bondad` que representa la bondad del ángel.
- Tiene un atributo protegido `maldad` que siempre es 0.
- Tiene un constructor que recibe el nombre del ángel y su bondad.
- Tiene un método `mostrar()` que muestra el nombre y la bondad del ángel.

### Clase `Demonio`

- La clase `Demonio` hereda de `Ser` y representa a un demonio.
- Tiene un atributo privado `bondad` que siempre es 0.
- Tiene un atributo privado `maldad` que representa la maldad del demonio.
- Tiene un constructor que recibe el nombre del demonio y su maldad.
- Tiene métodos `getMaldad()` y `setMaldad()` para obtener y establecer la maldad.
- Tiene un método `mostrar()` que muestra el nombre y la maldad del demonio.

### Clase `Humano`

- La clase `Humano` representa a un humano que interactúa con los seres espirituales.
- Tiene un atributo privado `fe` que representa la fe del humano.
- Tiene una lista de ángeles y una lista de demonios que le aconsejan.
- Tiene un constructor que recibe la fe inicial del humano.
- Tiene un método `añadirÁngel()` que genera aleatoriamente una bondad y añade un ángel a la lista de ángeles.
- Tiene un método `añadirDemonio()` que genera aleatoriamente una maldad y añade un demonio a la lista de demonios.
- Tiene un método `rezar()` que incrementa la fe del humano y añade un ángel a la lista.
- Tiene un método `pecar()` que disminuye la fe del humano y añade un demonio a la lista.
- Tiene un método `mostrar()` que muestra la fe del humano y el número de ángeles y demonios que le acompañan.

### Clase `CampoDeBatalla`

- La clase `CampoDeBatalla` es la clase principal que contiene el método `main()`.
- En el método `main()`, crea un humano con una fe de 50, muestra sus datos y realiza una lucha.
- Luego, llama al método `rezar()` dos veces, al método `pecar()` una vez y muestra nuevamente los datos del humano.

~~~java
class Ser {
    protected String nombre;

    public Ser(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}

class Ángel extends Ser {
    protected int bondad;
    protected int maldad;

    public Ángel(String nombre, int bondad) {
        super(nombre);
        this.bondad = bondad;
        this.maldad = 0;
    }

    public void mostrar() {
        System.out.println("Soy un Ángel llamado " + nombre + " con bondad " + bondad);
    }
}

class Demonio extends Ser {
    private int bondad;
    private int maldad;

    public Demonio(String nombre, int maldad) {
        super(nombre);
        this.bondad = 0;
        this.maldad = maldad;
    }

    public int getMaldad() {
        return maldad;
    }

    public void setMaldad(int maldad) {
        this.maldad = maldad;
    }

    public void mostrar() {
        System.out.println("Soy un Demonio llamado " + nombre + " con maldad " + maldad);
    }
}

class Humano {
    private int fe;
    private Ángel[] ángeles;
    private Demonio[] demonios;

    public Humano(int fe) {
        this.fe = fe;
        this.ángeles = new Ángel[1];
        this.demonios = new Demonio[1];
        añadirÁngel();
        añadirDemonio();
    }

    private void añadirÁngel() {
        int bondad = (int) (Math.random() * 101);
        Ángel ángel = new Ángel("Ángel", bondad);
        if (ángeles[0] == null) {
            ángeles[0] = ángel;
        }
    }

    private void añadirDemonio() {
        int maldad = (int) (Math.random() * 101);
        Demonio demonio = new Demonio("Demonio", maldad);
        if (demonios[0] == null) {
            demonios[0] = demonio;
        }
    }

    public void rezar() {
        fe++;
        añadirÁngel();
    }

    public void pecar() {
        fe--;
        añadirDemonio();
    }

    public void mostrar() {
        System.out.println("Fe del Humano: " + fe);
        System.out.println("Número de Ángeles: " + ángeles.length);
        System.out.println("Número de Demonios: " + demonios.length);
    }

    public void luchar(Humano h) {
        int sumaBondad = 0;
        int sumaMaldad = 0;

        for (Ángel ángel : ángeles) {
            sumaBondad += ángel.bondad;
        }

        for (Demonio demonio : demonios) {
            sumaMaldad += demonio.getMaldad();
        }

        if (sumaBondad > sumaMaldad) {
            rezar();
            System.out.println("El humano rezó.");
        } else if (sumaMaldad > sumaBondad) {
            pecar();
            System.out.println("El humano pecó.");
        } else {
            System.out.println("No ocurrió nada.");
        }

        mostrar();
    }
}

public class CampoDeBatalla {
    public static void main(String[] args) {
        Humano humano = new Humano(50);
        humano.mostrar();
        humano.luchar(null);
        humano.rezar();
        humano.rezar();
        humano.pecar();
        humano.mostrar();
    }
}
~~~
