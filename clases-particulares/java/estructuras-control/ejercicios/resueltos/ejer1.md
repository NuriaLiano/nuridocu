# Ejercicios de estructuras de control

## 1. [IF-SWITCH] Escribe un programa en Java que solicite al usuario un número del 1 al 7 para representar un día de la semana. Utiliza la estructura de control que consideres apropiada para determinar el nombre del día correspondiente y mostrarlo en pantalla

~~~java
import java.util.Scanner;

public class EjercicioSwitchIf {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingresa un número del 1 al 7 para representar un día de la semana:");
        int numeroDia = scanner.nextInt();

        if (numeroDia >= 1 && numeroDia <= 7) {
            String nombreDia;

            switch (numeroDia) {
                case 1:
                    nombreDia = "Lunes";
                    break;
                case 2:
                    nombreDia = "Martes";
                    break;
                case 3:
                    nombreDia = "Miércoles";
                    break;
                case 4:
                    nombreDia = "Jueves";
                    break;
                case 5:
                    nombreDia = "Viernes";
                    break;
                case 6:
                    nombreDia = "Sábado";
                    break;
                case 7:
                    nombreDia = "Domingo";
                    break;
                default:
                    nombreDia = "Número inválido";
                    break;
            }

            System.out.println("El número " + numeroDia + " representa el día " + nombreDia + ".");
        } else {
            System.out.println("El número ingresado no está en el rango válido.");
        }
    }
}
~~~

Se le pedirá al usuario que ingrese un número del 1 al 7 para representar un día de la semana en este ejercicio. Luego, se utiliza una estructura if para determinar si el número se encuentra dentro del rango apropiado. Si es así, se usa un interruptor para asignar el nombre del día adecuado según el número ingresado.
Finalmente, se muestra un mensaje con el número y el nombre del día específico. Se muestra un mensaje de error si el número está fuera del rango válido.

## 2. [IF-ARRAYS] Escribe un programa en Java que solicite al usuario ingresar un número del 1 al 12 para representar un mes. Utiliza las estructuras de control y/o arreglos que consideres necesarios para determinar el nombre del mes correspondiente y mostrarlo en pantalla

~~~java
import java.util.Scanner;

public class EjercicioIfElseArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] meses = {
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        };

        System.out.println("Ingresa un número del 1 al 12 para representar un mes:");
        int numeroMes = scanner.nextInt();

        if (numeroMes >= 1 && numeroMes <= 12) {
            String nombreMes = meses[numeroMes - 1];
            System.out.println("El número " + numeroMes + " representa el mes de " + nombreMes + ".");
        } else {
            System.out.println("El número ingresado no está en el rango válido.");
        }
    }
}
~~~

El usuario debe ingresar un número del 1 al 12 para representar un mes. Los nombres de los meses se almacenan en un array llamado "meses".
Luego se verifica si el resultado está dentro del rango apropiado. Si es así, se accede al array "meses" utilizando el número como índice (restando 1 para ajustar al índice base 0) y se obtiene el nombre del mes correspondiente. Finalmente, se muestra un mensaje con el mes y su nombre.
Se muestra un mensaje de error si el número está fuera del rango válido.

## 3. [IF-WHILE] Escribe un programa en Java que solicite al usuario ingresar un número entero positivo. Utiliza una estructura de control y contadores para determinar la cantidad de dígitos que tiene el número ingresado y mostrarlo en pantalla

~~~java
import java.util.Scanner;

public class EjercicioDoWhileContadores {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresa un número entero positivo:");
        int numero = scanner.nextInt();

        if (numero >= 1) {
            int contador = 0;

            do {
                numero /= 10;
                contador++;
            } while (numero != 0);

            System.out.println("El número ingresado tiene " + contador + " dígito(s).");
        } else {
            System.out.println("El número ingresado no es válido.");
        }
    }
}
~~~

En este ejercicio, el usuario debe ingresar un número entero positivo. A continuación, se determina si la cantidad ingresada es mayor o igual a cero. Si es así, se aumenta un contador en cada iteración y se divide el número por 10 hasta que sea igual a cero. Esto permite saber cuántos dígitos hay en el número ingresado.
Finalmente, el resultado del contador, que muestra la cantidad de dígitos del número ingresado, se muestra en pantalla.

## 4. [ARRAYS] Escribe un programa en Java que solicite al usuario ingresar una lista de palabras separadas por espacios. El programa debe identificar y mostrar en pantalla las palabras que comienzan con la letra 'a'

~~~java
import java.util.Scanner;

public class EjercicioForeach {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresa una frase:");
        String frase = scanner.nextLine();

        String[] palabras = frase.split(" ");

        System.out.println("Palabras que empiezan con la letra 'a':");
        for (int i = 0; i < palabras.length; i++) {
            String palabra = palabras[i];
            if (palabra.length() > 0 && palabra.toLowerCase().charAt(0) == 'a') {
                System.out.println(palabra);
            }
        }
    }
}
~~~

En este ejercicio, el usuario debe escribir una frase. Luego, el método split() se utiliza para dividir la frase en diferentes palabras y luego se almacenan en un array llamado palabras.
Después, cada palabra del array se itera utilizando el bucle foreach. El método startsWith() se utiliza para verificar si cada palabra comienza con la letra 'a', sin importar si es mayúscula o minúscula. La palabra se muestra en la consola si cumple con esta condición.
Las palabras de la frase que comienzan con la letra 'a' se muestran en el ejercicio.

## 5. [WHILE] Escribe un programa en Java que solicite al usuario ingresar una serie de números enteros positivos. El programa debe calcular y mostrar la suma de los números ingresados. El programa debe terminar cuando se ingrese el número 0

~~~java
import java.util.Scanner;

public class EjercicioWhile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int suma = 0;
        int numero;

        System.out.println("Ingrese números enteros positivos (ingrese 0 para terminar):");

        while (true) {
            numero = scanner.nextInt();

            if (numero == 0) {
                break;
            }

            if (numero < 0) {
                System.out.println("El número ingresado no es válido. Intente nuevamente.");
                continue;
            }

            suma += numero;
        }

        System.out.println("La suma de los números ingresados es: " + suma);
    }
}
~~~

El usuario de este ejercicio debe ingresar números enteros positivos. Se utiliza un ciclo while con una condición de salida que incluye un número 0.
Para terminar el bucle, se usa la palabra clave break si el número ingresado es igual a 0. Si el número es negativo, se muestra un mensaje de error y se usa la palabra clave continue para continuar con la siguiente iteración del bucle sin ejecutar el código restante en esa iteración.
Se suma al valor acumulado en la variable suma si el número es positivo. Al finalizar el ciclo, la suma de los números ingresados se muestra en la consola.

## 6. [DO-WHILE] Escribe un programa en Java que solicite al usuario ingresar una serie de números enteros positivos. El programa debe calcular y mostrar la suma de los números ingresados. El programa debe terminar cuando se ingrese el número 0

~~~java
import java.util.Scanner;

public class EjercicioDoWhile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numero;
        int suma = 0;

        System.out.println("Ingrese números enteros positivos (ingrese 0 para terminar):");

        do {
            numero = scanner.nextInt();

            if (numero < 0) {
                System.out.println("El número ingresado no es válido. Intente nuevamente.");
                continue;
            }

            suma += numero;
        } while (numero != 0);

        System.out.println("La suma de los números ingresados es: " + suma);
    }
}
~~~

Este ejercicio le pide al usuario que ingrese números positivos. Se utiliza un bucle do-while, que ejecuta el código una vez y luego prueba una condición para determinar si el bucle debe repetirse.
Dentro del bucle, comprueba si el número introducido es negativo. Si es así, aparecerá un mensaje de error y la instrucción continuar se usa para pasar a la siguiente iteración del ciclo sin ingresar el resto del código en ese punto.
Si el número es positivo, se suma al valor acumulado en la variable suma. El ciclo se repetirá hasta que el número ingresado sea 0.
Al final del bucle, la cantidad de números ingresados ​​​​se muestra en la consola.

## Diferencias entre el ejercicio 5 y el 6

1. **La condición de salida**: En el primer ejercicio con el bucle while, la condición se verifica al principio del bucle. Si la condición es falsa desde el inicio, el bucle no se ejecuta. En el segundo ejercicio con el bucle do-while, la condición se verifica al final del bucle. Esto garantiza que el código dentro del bucle se ejecuta al menos una vez, incluso si la condición es falsa desde el inicio.
2. **La ubicación de la condición**: En el primer ejercicio, la condición se verifica al inicio del bucle while. Si la condición es falsa, el bucle no se ejecuta y se sale inmediatamente. En el segundo ejercicio, la condición se verifica al final del bucle do-while. Esto significa que el código dentro del bucle se ejecuta primero y luego se verifica la condición para determinar si se debe repetir nuevamente.

### ¿Cuál utilizo?

La elección entre utilizar el bucle while o el bucle do-while depende de las necesidades y requisitos específicos de cada situación. Ambos bucles tienen sus casos de uso apropiados.

Estas consideraciones te van a ayudar a decidir que estructura utilizar:

- **Ejecución mínima**: Si necesitas que el código dentro del bucle se ejecute al menos una vez, independientemente de la condición, el bucle do-while es más adecuado, ya que garantiza una ejecución inicial antes de verificar la condición
- **Condición inicial**: Si la condición para entrar en el bucle se cumple inicialmente, es decir, el código dentro del bucle puede no ejecutarse nunca, entonces el bucle while puede ser más apropiado. Esto evita una ejecución innecesaria si la condición inicialmente no se cumple.
- **Condición de salida**: Si la condición de salida es sencilla y se puede verificar de manera confiable antes de ingresar al bucle, el bucle while puede ser más adecuado, ya que evita la ejecución del código dentro del bucle si la condición no se cumple inicialmente.

## 7. [FOR ANIDADOS] Imprime esta pirámide

RESULTADO:

~~~java
    *
   ***
  *****
 *******
*********
~~~

~~~java
import java.util.Scanner;

public class EjercicioPiramide {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese la altura de la pirámide:");
        int altura = scanner.nextInt();

        for (int i = 0; i < altura; i++) {
            for (int j = 0; j < altura - i - 1; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 2 * i + 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
~~~

Esta acción permite al usuario ingresar la altura deseada de la pirámide. Luego, el ciclo for se usa para imprimir cada fila de la pirámide.
En el bucle, se utilizan dos for integrados. El primer ciclo for imprime el espacio antes de la estrella en cada línea. El número de espacios disminuye a medida que avanza en las filas. El segundo bucle for imprime las estrellas en cada fila. El número de estrellas aumenta en 2 por cada fila.
Al final de cada iteración del bucle exterior, se imprime una nueva fila en la siguiente fila de la pirámide.
El resultado es una pirámide estelar impresa a la altura especificada por el usuario.

## 8. [FOR ANIDADOS] Imprime la misma pirámide pero invertida

RESULTADO:

~~~java
*********
 *******
  *****
   ***
    *
~~~

~~~java
public class EjercicioPiramideInvertida {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese la altura de la pirámide invertida:");
        int altura = scanner.nextInt();

        for (int i = altura - 1; i >= 0; i--) {
            for (int j = 0; j < altura - i - 1; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 2 * i + 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
~~~

En este caso, hemos invertido el orden de los bucles y ajustado la condición del bucle exterior. Ahora, el bucle exterior comienza desde el valor altura - 1 y va decreciendo hasta 0.
El proceso de impresión de los espacios en blanco y los asteriscos es similar al ejemplo anterior, pero en este caso, los espacios en blanco aumentan a medida que avanzamos hacia la parte inferior de la pirámide invertida.

## 9. [FOR-IF-ELSEIF] Escribe un programa en Java que solicite al usuario ingresar una frase. El programa debe contar y mostrar la cantidad de vocales, consonantes y espacios presentes en la frase

~~~java
import java.util.Scanner;

public class EjercicioControl {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int contadorVocales = 0;
        int contadorConsonantes = 0;
        int contadorEspacios = 0;

        System.out.println("Ingrese una frase:");
        String frase = scanner.nextLine();

        for (int i = 0; i < frase.length(); i++) {
            char caracter = frase.charAt(i);

            if (caracter == ' ') {
                contadorEspacios++;
            } else if (caracter == 'a' || caracter == 'e' || caracter == 'i' || caracter == 'o' || caracter == 'u') {
                contadorVocales++;
            } else {
                contadorConsonantes++;
            }
        }

        System.out.println("Cantidad de vocales: " + contadorVocales);
        System.out.println("Cantidad de consonantes: " + contadorConsonantes);
        System.out.println("Cantidad de espacios: " + contadorEspacios);
    }
}
~~~

En este ejercicio, se solicita al usuario que ingrese una frase. Luego, se utiliza un bucle for para iterar sobre cada caracter de la frase.
Dentro del bucle, se realizan las siguientes comprobaciones:

- Si el caracter es un espacio, se incrementa el contador de espacios.
- Si el caracter es una vocal (a, e, i, o, u), se incrementa el contador de vocales.

En cualquier otro caso, se incrementa el contador de consonantes.
Al final del bucle, se imprime la cantidad de vocales, consonantes y espacios encontrados en la frase.

## 10. [ARRAYS BIDIMENSIONALES] Escribe un programa en Java que contenga una matriz bidimensional predefinida de números enteros. El programa debe imprimir el contenido de la matriz en la consola

~~~java
public class EjercicioArraysBidimensionales {
    public static void main(String[] args) {
        int[][] matriz = { 
            { 1, 2, 3 },
            { 4, 5, 6 },
            { 7, 8, 9 }
        };

        System.out.println("Contenido de la matriz:");

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
~~~

En este ejercicio, se crea un array bidimensional llamado matriz que contiene una matriz de números enteros.
Luego, se utiliza un bucle for anidado para recorrer los elementos de la matriz. El bucle exterior itera sobre las filas de la matriz y el bucle interior itera sobre las columnas de cada fila. Se imprime el valor de cada elemento en la consola.
El resultado es la impresión del contenido de la matriz en formato de matriz.
