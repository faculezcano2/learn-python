#__init__ : lo mas comun es utilizarlo con una serie de argumetnos, que a su vez son los atributos de nuestra clase. DE manera tal que al 
# construir esa variable le damos valor inicial a sus atributos

'''
script que cree y asigne valor a los atributos de un abjeto tipo Ingrediente. Los ingredientes seran modelados dentro de una clase de 
un modulo separado y tendran los siguientes atributos:
-nombre
-cantidad
-unidad de medida
ademas la calse Ingrediente podra recibir como argumentos los valores iniciales pra sus atributos a travez del metodo constructor
'''
from moduloIngrediente import Ingrediente

def main():
    ingrediente = Ingrediente('Papa',3,'Kilos')
    ingrediente2 = Ingrediente('Banana', 7, 'kilos')
    ingrediente3 =  Ingrediente()

    ingrediente2.nombre = 'cebolla'

    print(ingrediente)
    print(ingrediente2)
    print(ingrediente3)


if __name__ == '__main__':
    main()