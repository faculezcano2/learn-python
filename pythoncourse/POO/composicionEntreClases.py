'''
ComposicionEntreClases.py
es una relacion entre clases, existen distintos tipos de relacion entre clases:
-COMPOSICION
-ASOCIACION
-AGREGACION
-HERENCIA

vamos a ver composicion
composicion: imagina una situacion que ya tenemos una clase definida y podemos modelar objetos, y tenemos otra clase que como parte de su
funcionamiento tiene elementos de la primer clase o administra lo que sucede con los objetos de la primer clase, ej:productos de un super 
que modelas clase de producto y dsp modelar clase tienda, dentro de tienda habra objetos de tipo producto

'''
#------------------------------------------------------------------------------------------------------------------------------------------
'''
script que utilice el menu de una clase Receta dentro de la cual habra una lista de ingredientes. Cada Ingrediente tendra como atributos 
los siguientes:
-nombre
-cantidad
-unidad de medida
La clase receta ademas de contener un menu y una lista de ingredientes debera tener un nombre y una lista de pasos o instrucciones asi 
como los siguientes comportamientos:
-agregar ingrediente
-consultar ingredientes
-agregar paso
-consultar pasos

moduloIngrediente.py y moduloReceta.py utilizados
'''
from moduloReceta import Receta

def main():
    receta = Receta('Pizza')


    receta.menu()
    print(receta)

if __name__ == '__main__':
    main()