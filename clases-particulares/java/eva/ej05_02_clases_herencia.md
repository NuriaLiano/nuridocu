# Ejercicio 05 (opcion 2 sin clases abstractas) - Clases con herencia

## Ejercicio de Figuras Geométricas

1. Crea una clase abstracta `Figura` con un método abstracto `calcularArea()`. Esta clase representará una figura geométrica genérica.

2. Crea las siguientes clases que hereden de `Figura`:
   - `Rectangulo`: representa un rectángulo y debe tener los atributos `ancho` y `altura`.
   - `Circulo`: representa un círculo y debe tener el atributo `radio`.

3. Implementa el método `calcularArea()` en las clases hijas para calcular el área de cada figura específica.

4. Crea una interfaz `Redimensionable` con un método `redimensionar(double proporcion)`. Esta interfaz permitirá redimensionar figuras geométricas.

5. Implementa la interfaz `Redimensionable` en una clase llamada `RectanguloRedimensionable` que extienda la clase `Rectangulo`. En esta clase, implementa el método `redimensionar()` para redimensionar el rectángulo según una proporción dada.

6. En el método `main()`, crea instancias de diferentes figuras geométricas (rectángulo, círculo y rectángulo redimensionable) y agrégalas a una lista.

7. Recorre la lista y muestra el área de cada figura utilizando el método `calcularArea()`. Si una figura es redimensionable, utiliza el método `redimensionar()` y muestra el área después de la redimensión.

~~~java
import java.util.ArrayList;
import java.util.List;

class Figura {
    public double calcularArea() {
        return 0;
    }
}

class Rectangulo extends Figura {
    private double ancho;
    private double altura;

    public Rectangulo(double ancho, double altura) {
        this.ancho = ancho;
        this.altura = altura;
    }

    public double getAncho() {
        return ancho;
    }

    public double getAltura() {
        return altura;
    }

    @Override
    public double calcularArea() {
        return ancho * altura;
    }
}

class Circulo extends Figura {
    private double radio;

    public Circulo(double radio) {
        this.radio = radio;
    }

    public double getRadio() {
        return radio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * radio * radio;
    }
}

interface Redimensionable {
    void redimensionar(double proporcion);
}

class RectanguloRedimensionable extends Rectangulo implements Redimensionable {
    public RectanguloRedimensionable(double ancho, double altura) {
        super(ancho, altura);
    }

    @Override
    public void redimensionar(double proporcion) {
        double nuevoAncho = getAncho() * proporcion;
        double nuevaAltura = getAltura() * proporcion;
        setAncho(nuevoAncho);
        setAltura(nuevaAltura);
    }

    private void setAncho(double ancho) {
        this.ancho = ancho;
    }

    private void setAltura(double altura) {
        this.altura = altura;
    }
}

public class Principal {
    public static void main(String[] args) {
        Rectangulo rectangulo = new Rectangulo(5, 3);
        Circulo circulo = new Circulo(2);
        RectanguloRedimensionable rectanguloRedimensionable = new RectanguloRedimensionable(7, 4);

        List<Figura> figuras = new ArrayList<>();
        figuras.add(rectangulo);
        figuras.add(circulo);
        figuras.add(rectanguloRedimensionable);

        for (Figura figura : figuras) {
            System.out.println("Área: " + figura.calcularArea());
            if (figura instanceof Redimensionable) {
                Redimensionable figuraRedimensionable = (Redimensionable) figura;
                figuraRedimensionable.redimensionar(0.5);
                System.out.println("Área después de redimensionar: " + figura.calcularArea());
            }
            System.out.println();
        }
    }
}
~~~
