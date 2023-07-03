# a

- Asignatura
  valor y nombre, valor representa dos cosas diferentes segun el punto de vista. Para un progfesor, sera el numero de horas de imparticion a la semana. Para un estudiante sera la calificacion en esa asignatura
- Persona
  nombre (string)
  dni(int)
- Pas
  extiende de persona 
  antiguedad (int)
  especialidad laboral (string)
- Estudiante
  extiende de persona
  nummatricula(int)
  expediente(lista enlazada de personas)
- Profesor
  extiende de persona
  antiguedad(int)
  categoria(catedratico, titular, colaborador o asociado)
  docencia (lista enlazada de asignaturas)
  funcion impartidas()
- Centro
  plan de estudios(array de asignaturas)
  personal (lista enlazada de persona)
  nombre(string)
  cursosPlan(int)

interfaz de lista enlazada
public interface IList<E>{
    void add(int index, E elem)
    void add(E elem)
    E get(int index)
    int size()
    void set (int index, E elem)
    int indexOf(E elem)
    void remove (int index)
    void remove (E elem)
    IList<E> sublist (int inicio, int fin)
    String toString()
}

Ejercicios:

Ejercicio 1: haz el constructor de la clase Centro.
Ejercicio 2: programa el método listadoProfes de la clase Centro
Ejercicio 3: programa el método encargarAsig de la clase Profesor
Ejercicio 4: programa el método calificar de la clase Alumno