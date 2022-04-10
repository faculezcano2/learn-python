'''
herencia2.py
script que solicite la informacion de un objeto de tipo Estudiante y posteriormente imprima en pantalla sus datos.
La clase Estudiante heredara de la clase Persona, es decir que sera un tipo particular de persona. Un Estudiante ademas de la informacion y 
comportamientos de una persona tendra como atributos un promedio y un codigo de estudiante y como comportamiento podra estudiar una materia.
Finalmente hacer que el estudiante ejecute el comportamiento estudiar.
'''
from moduloEstudiante import Estudiante

def main():
    nombre = input('Nombre del estudiante: ')
    edad = input('Edad del estudiante: ')
    promedio = float(input('Promedio del estudiante: '))
    codigo = input('Codigo del estudiante: ')


    estudiante =  Estudiante(nombre,edad,promedio,codigo)
    print(f'''------Los datos del estudiante son:
{estudiante}''')
    print('-'*40)
    estudiante.estudiar('Python')
    estudiante.estudiar('Matematica')
    estudiante.hablar('Estoy aprendiendo python brodaaaaa')


if __name__ == '__main__':
    main()