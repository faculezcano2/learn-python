#Estructura de datos como las que venimos viendo y la dif es que en esta estructura o coleccio de datos, no pueden existir elementos repetidos, todos los elementos son unicos

#se crea con la palabra set
a = set()
type(a)#saber de que tipo es
#otra forma es con elementos ya 
a2 = {0,1,2,3}
#para agregar un elemento es con .add

a2.add(5) #al conjunto anterior se le agrega el 5

#si quiero agregar un elemento que ya existe no me tira ningun error pero no lo va a agregar devuelta

#eliminar el primer elemento
a2.pop()

#si quiero remover un elemento en especifico es con .remove
a2.remove(2)
#si quiero eliminar un elemento que no existe me tira un error

#si no quiero que me tire un error uso .discard si no se encuentra no hace nada
a2.discard(10)

5 in a2 #me tira true o flase si se encuentra en el conjunto o no

len(a2) #saber cuantos elementos hay en el conjunto

#operaciones entre dos conjuntos
A = {0,1,3,5}
B = {0,2,4,6}

A & B #nos devuelve un conjunto con los elementos que tienen en comun conjuntos A Y B 
A | B #nos devuelve la union de todos los elementos sin los repetidos
A - B #nos devuelve la diferencia entre conjuntos, osea todos los elementos del conjunto A que no estan en B
B - A #devuelve todos los elementos de B que no estan en A 
A ^ B #union de las diferencias de uno y de otro
A > B #evalua si A contiene los elemntos de B
A < B #evalua si todos los elementos de A estan contenidos en B
A.isdisjoint(B) #evalua si A no comparte elementos con B 

#¿para que se puede utilizar conjuntos? --> Es una manera rapida de evaluar cuantos simbolos unicos o elementos unicos hay una coleccion de datos
# EJEMPLO TENGO UNA LISTYA LA CONVIERTO A CONJUNTO Y DE AHI OBTENER LOS ELEMENTOS UNICOS y demas caracteristicas  