from functools import cmp_to_key
from operator import index
from re import M


myStr= "hello world"
name = "facundo"
#print(dir(myStr))#para saber que se puede hacer con este tipo de datos

print(myStr.upper()) #pone todo el texto en may
print(myStr.lower()) #pone todo el texto en min
print(myStr.swapcase())#una mayu y una mascu asi todo el texto
print(myStr.capitalize())#la primer letra en mayus
print(myStr.replace('hello', 'bye')) #cambiar
print(myStr.replace('hello', 'bye').upper())#cambiar y mayus
print(myStr.count('l')) #cuenta la cantidad de veces que haya la letra
print(myStr.startswith("hello")) #saber si empieza con tal palabra
print(myStr.endswith("hola"))#saber si termina con tal palabra
print(myStr.split()) #divide el texto, por defecto es en los espacios. Pero se puede decir que cambia por otras cosas
print(myStr.split('o'))#asi
print(myStr.find('o')) #busca la posicion donde se encuentra la letra
print(len(myStr))#longitud de la palabra
print(myStr.index('e'))#podemos buscar el indice de una palabra
print(myStr.isnumeric())#para saber si es numerico
print(myStr.isalpha())#para saber si es alfanumerico
print(myStr[4])#para saber que hay en esa posicion del texto
print(myStr.count("o"))#cuenta las ocurrencias de las o
print(myStr[3:7])#escribe la cadena desde la pos 3 hasta la 7 
print(f"My name is {name}")#agregar la f al principio para que lea {} como una var
print('o' in myStr)#devuelve true o false si se enceuntra la letra en la cadena
'.'.join(['nombre', 'apellido', 'ciudad'])#lo que hace es unir la cadena con un separador que n osotros demos
