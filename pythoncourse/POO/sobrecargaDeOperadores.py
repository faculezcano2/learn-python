'''
a que nos referimos con sobrecarga de operadores?
los operadores ya estan definidos dentro de pyhton (+ - * /) sin embargo muchas veces nosotros vamos a necesitar utilizar estos operadores
para nuestros propios datos, ejemplo comparar dos libros como0 va a saber python cual es mayor o menor o iguales?
Esto es con funciones creadas popr nosotros que nos permita definir que es lo que queremos hacer  cuando intentamos comparar distintos
objetos por ejemplo podemos sobrecargar el operador < para un objeto libro para que python sepa cual es menor o para una clase

en sintesis poder hacer operaciones entre objetos definidos por nostros que no sean de tipo de dato simple


operadores relacionales
<    __it__
<=   __le__
>    __gt__
>=   __ge__
==   __eq__
!=   __ne__

operadores aritmeticos
+    __add__
-    __sub__
*    __mul__
**   __pow__
/    __truediv__
//   __floordiv__
%    __mood__


para poder entenderlo vamos hace lo siguiente:

script que tenga una lista de objetos tipo Pelicula. La lsita debera ser ordenada segun el nombre de las peliculas, una vez ordenada se
mostrara la lista ademas del menor y mayor objeto dentro de la coleccion
'''
from pelicula import Pelicula

def main():
    peliculas = []
    peliculas.append(Pelicula('El Padrino', 'Francis Ford Copolla', 1972, 175))
    peliculas.append(Pelicula('Sueño de fuga', 'Frank Darabont', 1994, 142))
    peliculas.append(Pelicula('La lista de Schindler', 'Steven spurs', 1993, 195))
    peliculas.append(Pelicula('Toro salvaje', 'Martin Scorsese', 1990, 129))
    peliculas.append(Pelicula('Casa Blanca', 'Michael Curtiz', 1942, 102))


    peliculas.sort() #esto sin sobrecargar los operadores no se puede ya que el < no estaria soportado.Entonces podemos sobrecargar esos operadores


    for pelicula in peliculas:
        print(pelicula)
        print('-'*40)

    print(f'Menor pelicula en la colecicon: \n {min(peliculas)}')
    print(f'Mayor pelicula en la colecicon: \n {max(peliculas)}')


if __name__ == '__main__':
    main()