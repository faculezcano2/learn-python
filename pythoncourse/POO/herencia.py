'''
la herencia es tener 2 clases pero identificamos una como la clase padre o base y esa clase va a compartir/heredar sus atributos o 
comportamientos con otras nuevas clases, esas clases ademas de tener su info propia tienen la info de su clase padre/base
la herecia es un mecanismo que nos ayuda mucho a la hora de ampliar programas, nos evita reescribir codigo, ademas sirve para modelar de mejor
manera la realidad

patron a seguir
class Derivada(Base1, ..., Basen):
    instrucciones 


derivada:nombre de la clase que queremos desarllar, entre parentesis la calse base o las clases de la cual/es quiero heredar
'''
'''
ej:
script que cree e imprima la informacion de un objeto de tipo Persona y de otro de tipo Deportista.
las clases deportista heredara de la calse Persona, es decir que sera un tipo particular de persona
'''
from moduloDeportista import Deportista
from moduloPersona import Persona


def main():
    per1 = Persona('Hector tuga', 44)
    dep1 = Deportista('Pepe Nava', 33, 'Futbol')

    print(f'''Datos de la persona:
{per1}''')
    print('-'*50)
    print(f'''Datos del deportista:
{dep1}''')
    dep1.entrenar()
    dep1.hablar('Listo para ganar una medalla')


if __name__ == '__main__':
    main()