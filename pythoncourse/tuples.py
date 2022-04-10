'''
#conjunto de datos igual que las listas pero que no podemos cambiarlas
x = (1, 2, 3, 4)
print(x)

months = ("enero", "febrebro",)

#constructor que genera un tuple
y = tuple((1,2,3))
print(y)

2 in y #para saber si un elemento se encuentra en la tupla
y.index(2) #saber la posicion del elemento 2
y.count(2)#cuantas veces aparece el 2 en la tupla

#todo lo que se puede hacer con una tupla 
print(dir(x))

#x=(1) esta tupla toma el 1 como un enterto, no lo toma como una dupla
#si queres una tupla de un solo elemento seria asi = x=(1,)

#imprimir por indice
print(x[2])

#eliminar toda la tupla
del x
'''
#hay un ejercicio con tuplas