'''
#se crean con corchetes y pueden guiardar elementos de distintos tipos de datos

demoList = [1,"hola",3,4,56,True,"facundo",5,8,False,[1,2,3]]#se puede una lista adentro de otra lista
colors = ["blue","red", "green"]
#list() = es un constructor que nos ayuda a crear una lista
numberList= list((1,2,3,4,5))
print(numberList)

print(type(numberList))

#crear una lista en un rango
#range() toma valor incial al final y crea un rango, toma desde el primero hasta uno antes del segundo parametro
r = list(range(1,10))
print(r)

#obtener info de una lista
print(dir(colors))#todo lo que se puede hacer con una lista
print(len(colors))#cantidad de elementos dentro de la lista
print(colors[1])#segunda pos

print("green" in colors)#sabeer si un elemento existe dentro de una lista

#reasignarlos
print(colors)
colors[1]="yellow"
print(colors)

#metodos
colors.append("violet")#agregar un elemento
colors.append("yellow","violet")#no se puede pasar varios para pasar varios seria con una tuple
colors.append(("yellow","violet"))#asi seria con tuple pero seria un solo elemento, si quiero que sean separados
colors.extend(["yelow", "violet"])#asi con una lista o con tuple lo tomaria por separado cada uno

#insertar un elemento en una posicion dada
colors.insert(1,"black")#insertar en la posicion 1 el color tal

#remover elementos de una lista
colors.pop()#elimina el ultimo

#remover un elemento en especifico
colors.remove("violet")

#eliminar a partir de un indice
colors.pop(1) #elimina la pos 1

#eliminar todos
colors.clear()

#ordenar alfabeticamente
colors.sort()
#ordenar alrrevez alfabeticamente
colors.reverse()

#obetener indice
colors.index("red")

#obtener cuantas veces tenemos un elemento
colors.count("red")



#preguntar si un elemento esta en la lista
# elemento in lsita
#ej
listaNum = [1,2,3,4,2,2,5,6,2]
print(33 in listaNum)
print(2 in listaNum)

#obtener el minimo y el maximo de una lista
print(min(listaNum))
print(max(listaNum))

#crear una lista que tenga un menu con opciones :
agregar
insertar
mostrar lista
buscar un elemento
eliminar un registro
ordenar lista
limpiar lista
salir
'''
#hacer una copia de una lista
#si tenemos una lista l1  con ciertos datos y dsp tenemos 
#otra lista l2 y a l2 le asignamos los valores de l1 (l2=l1)
#lo que hacemos es que ambas apuntan a la misma direcc de 
#memoria, entonces si modificas una se ve reflejado en la otra
#para que no pase eso hacemos .copy()

l1 = [0,0,0,0,0,0,0,0]
l2 = l1.copy()
# asi copiaria los mismos valores y podes manejar las listas sin que se vea los cambios reflejados en la otra

#tambien para copiar podemos hacer asi
l2 = l1[:]

#para ver una lista desde una posicion hasta el final se hace asi
l2[3:]
#yhace la copia de esa lista desde esa posicion hasta el final
#si hacemos 
l2[:5]
#lo que hace es copiar desde el principio hasta la posicion

#tambien se puede combinar
l2[3:7]
#desde donde hasta donde

#tambien se puede hacer cada cuantos datos quiero copiar 
l2[1:6:2]
#lo que hace aca es ir desde la pos 1 hasta la pos 6 copíando
#los datos de dos en dos


