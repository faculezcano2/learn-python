'''
class indentificador:
    instrucciones

__init__ --> metodo especial nos permite crear a los objetos con ciertos valores iniciales, es como un constructor. se escribe siempre  que hagamos una clase
self --> argumento que se les pasa a los metodos de una clase, siempre. Hace referencia a si mismo, estamos recibiendo por argumento el 
propio objeto que le estamos dando el atributo
'''

'''
script que implemente una clase figura que como atributo tenga la cantidad de lados. Una vez creada la calse crear dos objetos y mostrar
su cantidad de lados
forma de hacer qu un atributo sea privado: poner un guion bajo dsp del punto a sus propiedades
self_lados = none
metodos de interfas --> obtener, dar y eliminar atributos a una clase 
'''

class Figura: 
    def __init__(self):
        self._lados = None

    @property #metodo de interfaz, regresa el valor asociado a al cantidad de lados
    def lados(self):
        return self._lados

    @lados.setter #nos permite asignarle valor al atributo lados
    def lados(self, valor):
        if valor < 3:
            print('El valor debe ser mayor que 3')
            self._lados = None 
        else:
            self._lados = valor

    @lados.deleter
    def lados(self):
        del self._lados



def main():
    triangulo = Figura()
    cuadrado = Figura()
    
    '''
    print(f'triangulo tiene {triangulo.lados} lados')
    print(f'cuadrado tiene {cuadrado.lados} lados')
    imprime none
    '''
    #darle valor a sus atributos:
    triangulo.lados = -3
    cuadrado.lados = 4

    print(f'triangulo tiene {triangulo.lados} lados')
    print(f'cuadrado tiene {cuadrado.lados} lados')

''' del cuadrado.lados
    print(f'cuadrado tiene {cuadrado.lados} lados')
    aca me tiraria error ya que quiere leer la propiedad lados de cuadrados que no la tiene ya que fue eliminada
'''
if __name__ == '__main__':
    main()