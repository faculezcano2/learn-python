#vamos a ver como se hace una clase dentro de un modulo y ademas vamos a definir el metodo __str__
#hacer una classe en un modulo nos da mas independencia de la informacion 

'''
__str__ --> Para mostrar objetos, Python indica que hay que agregarle a la clase un método especial, llamado __str__ que debe devolver
una cadena de caracteres con lo que queremos mostrar. Ese método se invoca cada vez que se llama a la función str.

script que importe la clase Prenda para dspues crear dos objetos e imprimir su informacion en pantalla

'''

from moduloPrenda import Prenda

def main():
    playera = Prenda()


    playera.tipo = 'playera con estampado'
    playera.talle = 'M'

    print(playera)

'''
Vemos que con str(p) se obtiene la cadena construida dentro de __str__, y que internamente Python llama a __str__ cuando se le pide que imprima
una variable de la clase Punto.
'''
if __name__ == '__main__':
    main()