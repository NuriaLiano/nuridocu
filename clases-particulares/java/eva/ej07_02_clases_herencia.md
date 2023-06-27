# Ejercicio 07 - Clases, herencias e interfaces

## Campo de Batalla

### Clase Ser

- Clase base para la herencia, no se puede instanciar.

### Clase Ángel

- Atributos (visibles desde cualquier clase del paquete): bondad y maldad.
- La maldad siempre es 0, por lo que su método `mostrar()` solo muestra la bondad.

### Clase Demonio

- Atributos (visibles solo desde la misma clase): bondad y maldad.
- La bondad siempre es 0, por lo que su método `mostrar()` solo muestra la maldad.
- Métodos para ver y cambiar sus atributos.

### Clase Humano

- Atributos: fe (visible solo desde la misma clase) y listas de ángeles y demonios que le aconsejan.
- Cada vez que se crea un humano, se le asigna una fe y se le añade un ángel y un demonio.
- Método `añadirÁngel()`: genera aleatoriamente una bondad (entre 0 y 100), crea un ángel y lo añade a la lista de ángeles.
- Método `añadirDemonio()`: genera aleatoriamente una maldad (entre 0 y 100), crea un demonio y lo añade a la lista de demonios.
- Método `rezar()`: cada vez que el humano reza, su fe se incrementa y se añade un ángel a su lista.
- Método `pecar()`: cada vez que el humano peca, su fe disminuye y se añade un demonio a su lista.
- Método `mostrar()`: muestra la fe del humano, el número de ángeles y el número de demonios que le acompañan.

### Clase CampoDeBatalla

- Es la clase principal.
- Método `main()`: crea un humano con una fe de 50, muestra sus datos y hace que luche una vez.
  - A continuación, hace que el humano rece dos veces, luego peque una vez y finalmente muestra los datos del humano.

- Método `luchar(Humano h)`: se le pasa un humano por parámetro.
  - Calcula la suma de la bondad de todos sus ángeles y la suma de la maldad de todos sus demonios, y las compara.
  - Si hay más bondad que maldad, el humano reza.
  - Si hay más maldad que bondad, el humano peca.
  - Cada vez que un humano lucha, se muestra lo que sucede.
  - Antes de terminar, se muestran los datos del humano tras el combate.

~~~java
interface Espiritual {
    void mostrar();
}

abstract class Ser {
    // No se puede instanciar
}

abstract class Incorpóreo extends Ser implements Espiritual {
    // Implementación de la interfaz Espiritual
}

class Ángel extends Incorpóreo {
    protected int bondad;
    protected int maldad;

    public Ángel(int bondad) {
        this.bondad = bondad;
        this.maldad = 0;
    }

    @Override
    public void mostrar() {
        System.out.println("Soy un Ángel con bondad " + bondad);
    }
}

class Demonio extends Incorpóreo {
    private int bondad;
    private int maldad;

    public Demonio(int maldad) {
        this.bondad = 0;
        this.maldad = maldad;
    }

    public int getMaldad() {
        return maldad;
    }

    public void setMaldad(int maldad) {
        this.maldad = maldad;
    }

    @Override
    public void mostrar() {
        System.out.println("Soy un Demonio con maldad " + maldad);
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
        Ángel ángel = new Ángel(bondad);
        if (ángeles[0] == null) {
            ángeles[0] = ángel;
        }
    }

    private void añadirDemonio() {
        int maldad = (int) (Math.random() * 101);
        Demonio demonio = new Demonio(maldad);
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
        humano.luchar(humano);

        humano.rezar();
        humano.rezar();
        humano.pecar();
        humano.mostrar();
    }
}
~~~
