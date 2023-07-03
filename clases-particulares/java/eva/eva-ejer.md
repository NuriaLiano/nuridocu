# Ejercicio EVA

## Juego de la vida

El Juego de la Vida es realmente un juego de cero jugadores lo que signica que su evolución está determinada por su estado inicial y no necesita actuación por parte de ningún jugador. La única forma de jugar es creando una conguración inicial y observando cómo evoluciona.

El universo del juego es una parrilla bidimensional de celdas cuadradas (también llamadas células).
Cada celda o célula puede estar en dos estados: viva o muerta. Cada celda interacciona con sus 8 celdas
vecinas adyacentes. En cada paso del juego se deben aplicar las siguientes transiciones simultáneamente
a todas las celdas:

- Una celda viva con menos de dos vecinas vivas morirá por subpoblación.
- Una celda viva con más de tres vecinas vivas morirá por superpoblación.
- Una celda viva con exactamente dos o tres vecinas vivas se mantendrá viva.
- Una celda muerta con exactamente tres vecinas vivas (re)vivirá.
- Una celda muerta con más o menos de tres vecinas vivas seguirá muerta.

Para más información puedes consultar: https://www.conwaylife.com/wiki/Main_Page donde puedes
encontrar las reglas anteriores y muchos más detalles sobre el juego.

No obstante, el objetivo académico de esta práctica es trabajar sobre los conceptos de herencia,
interfaces y polimorsmo y por ello, se van a introducir importantes modicaciones sobre el
juego clásico. Mientras se realiza la práctica, es importante ser consciente de qué lo importante es seguir
el diseño, el objetivo que se busca es implementar el diseño tal y como se va a especicar, no meramente
que el programa funcione.

## Clases e interfaces

- Célula
  - es la base del resto
  - Tiene 3 atributos de instacia
    - Posición
    - Centro
    - Color
  - Tiene un atributo de clase Dimension para indicar el tamaño de la mitad del lado del cuadrado que se va a dibujar. Podéis fijar este valor a 0,6, un poco más de lo que realmente miden, pero no importa
  - Para construir una célula se necesita la posición de su centro dado por sus dos coordenadas, dos números enteros entre 0 y 99 ambos incluidos. En principio todas la células se crean muertas, es decir, de color negro (StdDraw.BLACK).
  - Un método para hacer revivir a la célula, llama a ese método hacerViva, las células vivas tienen color blanco (StdDraw.WHITE).
  - Un método para saber si una célula está viva o no (verdadero/falso). En principio, una célula está viva si su color es blanco.
  - Un método para dibujar la célula, la célula se debe dibujar en el color que marque el valor del atributo correspondiente como un cuadrado relleno (método StdDraw.filledSquare), en la posición dada por sus coordenadas y con la dimensión dada por DIMENSION.

- CelulaClasica
  - Hereda de Celula
  - Implementa CambiarEstado
  - Como atributos necesita un array de células para guardar las celulas vecinas y otro atributo para guardar cúal va a ser su siguiente estado
  - Para calcular un nuevo estado se deben utilizar las reglas de evolución clásicas

- SiempreIgual
  - Hereda de Celula
  - Las células de esta clase son peculiares en el sentido de que siempre se van a mantener "vivas" o "muertas" independientemente del estado de sus vecinas
  - Al construir una célula de este tipo se debe pasar un dato boolean para indicar su va estar viva (true) o muerta(false)
  - Debido a esta particularidad estas células no siguen el patrón de colores general. Las que siempre están vivas serán de color rojo () y las muestras de color amarillo

- Interfaz Tick
  - Declara un único método "tick" sin parámetros de retorno
  - Este método se va a llamar, cuando este implementado, cada vez que se calcule y actualice un nuevo estado de las células

- CelulaIntermitente
  - Debe heredar de Celula
  - Debe implementar Tick
  - Las células de esta clase son peculiares porque no viven o mueren en función del estado de sus vecinas sino que lo hacen de forma intermitente. Cada 20 veces que se llame a tick alternan su estado entre viva y muerta.
  - Debido a esta particularidad no siguen el patrón de colores general, en este caso, se muestran en azul (StdDraw.BLUE) cuando están muertas y con el habitual blanco cuando están vivas.

- Clase Factoria.
  - Esta es una clase auxiliar para construir la matriz de células de 100x100 células a partir de los datos que se van a leer de un objeto sc de tipo Scanner. Se va a generar una célula para cada par de coordenadas x e y entre 0 y 99 y, además, se va a guardar cada célula en la matriz utilizando sus coordenadas como los índices en la matriz.
  - Tiene un único método de clase, crearCelulas, que toma como argumento un Scanner sc y devuelve una nueva matriz con las células correspondientes teniendo en cuenta que:
    - El primer dato en sc es un número entero, nEspeciales, el número de células especiales.
    - A continuación se podrá encontrar nEspeciales líneas, al principio de cada línea siempre habrá dos números, las coordenadas de la célula que se va a describir.
    - Después se encontrará una cadena que podrá tener los valores: Viva, CelulaIntermitente o SiempreIgual. Cuando se encuentre Viva se deberá construir una célula clásica, pero después de crearla se deberá cambiar su estado a viva, cuando sea CelulaIntermitente se deberá crear una célula de esa clase y cuando sea SiempreIgual se deberá leer un dato booleano (true/false) de sc y crear una célula de ese tipo cuyo estado es el booleano leído.
    - Una vez leídas y creadas las células especiales, todas las demás células en la matriz serán células clásicas cuyos estados iniciales son muertas.
    - Se adjunta al enunciado un archivo con datos cuyo formato es el esperado por este método. Se puede utilizar para pegar en la entrada estándar para hacer pruebas.

- Clase Mundo.
  - El mundo es la cuadrícula donde evolucionan las células.
  - En esta clase sólo se puede utilizar la clase Celula, la interfaz CambiarEstado y la interfaz Tick. Está prohibido usar las clases de células especiales.
  - Las células del mundo se deben construir mediante el método crearCelulas descrito anteriormente.
  Se debe implementar un método, pasarVecinas, para pasar a cada células las células que son vecinas. Se recuerda que para ello existe el método CambiarEstado.indicarVecina.
  - El mundo debe ser toroidal, esto signica que las células situadas en el borde superior son vecinas de las situadas en el borde inferior y viceversa, y exactamente igual con los bordes izquierdo y derecho. Existen muchas maneras de lograr esto, pero una manera muy elegante de conseguirlo es usando el resto de la división entera, de hecho, usando ese operador se pueden hacer dos bucles anidados para todas las células y sin ninguna sentencia condicional... Se debe implementar un método, dibujar, que dibuje todas las células.
  - Se debe implementar un método tick que debe marcar la evolución de las células. Este método debe: llamar al método calcularNuevoEstado de todas las células que lo tengan, y luego llamar al método actualizar. Adicionalmente se debe llamar al método tick de las células que lo tengan.
  
~~~java
import java.awt.Color;

interface CambiarEstado {
  void indicarVecina(Celula vecina);
}

interface Tick {
  void tick();
}

class Celula {
  private int x;
  private int y;
  private Color color;

  private static final double DIMENSION = 0.6;

  public Celula(int x, int y) {
    this.x = x;
    this.y = y;
    this.color = Color.BLACK;
  }

  public void hacerViva() {
    this.color = Color.WHITE;
  }

  public boolean estaViva() {
    return this.color == Color.WHITE;
  }

  public void dibujar() {
    double posX = x + 0.5;
    double posY = y + 0.5;
    StdDraw.setPenColor(this.color);
    StdDraw.filledSquare(posX, posY, DIMENSION);
  }
}

class CelulaClasica extends Celula implements CambiarEstado {
  private Celula[] vecinas;
  private boolean siguienteEstado;

  public CelulaClasica(int x, int y) {
    super(x, y);
    this.vecinas = new Celula[8];
    this.siguienteEstado = false;
  }

  public void indicarVecina(Celula vecina) {
    // Implementar la lógica para indicar las células vecinas
  }

  public void calcularNuevoEstado() {
    int contadorVivas = 0;
    for (Celula vecina : vecinas) {
      if (vecina != null && vecina.estaViva()) {
        contadorVivas++;
      }
    }

    if (this.estaViva()) {
      if (contadorVivas < 2 || contadorVivas > 3) {
        this.siguienteEstado = false;
      } else {
        this.siguienteEstado = true;
      }
    } else {
      if (contadorVivas == 3) {
        this.siguienteEstado = true;
      } else {
        this.siguienteEstado = false;
      }
    }
  }

  public void actualizar() {
    if (this.siguienteEstado) {
      this.hacerViva();
    } else {
      this.color = Color.BLACK;
    }
  }
}

class SiempreIgual extends Celula {
  public SiempreIgual(int x, int y, boolean estado) {
    super(x, y);
    if (estado) {
      this.color = Color.RED;
    } else {
      this.color = Color.YELLOW;
    }
  }
}

class CelulaIntermitente extends Celula implements Tick {
  private static final int INTERVALO = 20;
  private boolean estadoActual;
  private int contador;

  public CelulaIntermitente(int x, int y) {
    super(x, y);
    this.estadoActual = true;
    this.contador = 0;
  }

  public void tick() {
    this.contador++;
    if (this.contador == INTERVALO) {
      this.estadoActual = !this.estadoActual;
      this.contador = 0;
    }

    if (this.estadoActual) {
      this.hacerViva();
    } else {
      this.color = Color.BLUE;
    }
  }
}

class Factoria {
  public static Celula[][] crearCelulas(Scanner sc) {
    int nEspeciales = sc.nextInt();
    Celula[][] matriz = new Celula[100][100];

    for (int i = 0; i < nEspeciales; i++) {
      int x = sc.nextInt();
      int y = sc.nextInt();
      String tipo = sc.next();

      if (tipo.equals("Viva")) {
        CelulaClasica celula = new CelulaClasica(x, y);
        celula.hacerViva();
        matriz[x][y] = celula;
      } else if (tipo.equals("CelulaIntermitente")) {
        CelulaIntermitente celula = new CelulaIntermitente(x, y);
        matriz[x][y] = celula;
      } else if (tipo.equals("SiempreIgual")) {
        boolean estado = sc.nextBoolean();
        SiempreIgual celula = new SiempreIgual(x, y, estado);
        matriz[x][y] = celula;
      }
    }

    for (int i = 0; i < 100; i++) {
      for (int j = 0; j < 100; j++) {
        if (matriz[i][j] == null) {
          matriz[i][j] = new CelulaClasica(i, j);
        }
      }
    }

    return matriz;
  }
}

class Mundo {
  private Celula[][] celulas;

  public Mundo(Scanner sc) {
    this.celulas = Factoria.crearCelulas(sc);
    pasarVecinas();
  }

  private void pasarVecinas() {
    for (int i = 0; i < 100; i++) {
      for (int j = 0; j < 100; j++) {
        Celula celula = celulas[i][j];

        if (i > 0 && j > 0) celula.indicarVecina(celulas[i - 1][j - 1]);
        if (i > 0) celula.indicarVecina(celulas[i - 1][j]);
        if (i > 0 && j < 99) celula.indicarVecina(celulas[i - 1][j + 1]);
        if (j > 0) celula.indicarVecina(celulas[i][j - 1]);
        if (j < 99) celula.indicarVecina(celulas[i][j + 1]);
        if (i < 99 && j > 0) celula.indicarVecina(celulas[i + 1][j - 1]);
        if (i < 99) celula.indicarVecina(celulas[i + 1][j]);
        if (i < 99 && j < 99) celula.indicarVecina(celulas[i + 1][j + 1]);
      }
    }
  }

  public void dibujar() {
    for (int i = 0; i < 100; i++) {
      for (int j = 0; j < 100; j++) {
        celulas[i][j].dibujar();
      }
    }
  }

  public void tick() {
    for (int i = 0; i < 100; i++) {
      for (int j = 0; j < 100; j++) {
        Celula celula = celulas[i][j];
        if (celula instanceof Tick) {
          celula.tick();
        }
        celula.calcularNuevoEstado();
      }
    }

    for (int i = 0; i < 100; i++) {
      for (int j = 0; j < 100; j++) {
        celulas[i][j].actualizar();
      }
    }
  }
}

public class JuegoDeLaVida {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Mundo mundo = new Mundo(sc);

    while (true) {
      StdDraw.clear();
      mundo.dibujar();
      StdDraw.show(100);
      mundo.tick();
    }
  }
}

~~~
