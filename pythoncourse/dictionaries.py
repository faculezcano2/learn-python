#nos permite ordenar elementos a traves de claves y valores+ se conoce tambien como mapas o hash en otros idiomas
#se puede usar por ejemplo para mandar informacion entre el frontend y el backend
#taambien para guardar info de ususarios

from http.cookies import BaseCookie

#ej compra de un libro
{
    "name":"book",
    "quantity":3,
    "price": 4.49
}

#ejem,plo una persona
person={
    "name":"facundo",
    "lastName":"lezcano",
    "age":22
}

#otras formas de declararlo
#-
d = dict() #dict es un constructor de dictionaries
d = {1:'uno', 2:'dos', 3:'tres'} #d toma los valores que le damos
#-
d = {}
d= dict([(1,'uno'),(2,'dos'), (3,'tres')]) #diccionario con tuplas a la hora de consultarlo lo muestra como diccionario
#si quiero agregar uno hago 
d[4] = 'cuatro'
print(d)

#-
d.setdefault(5,'[1,2,3,4,5]') #otra forma de agregar o crear

d.setdefault(5,'cinco') #si hago esto  no lo reemplaza, para reemplazar hacemos asi:
d[5] = 'cinco'

#consultar diccionarios
d[5] #consultar la llave te da el valor de esta
#si no existe la llave te da un error

d.get(5) #no te tira error si no existe 

d.get(55,'No existe') #asi te devuelve un valor por defaultr si ese elemento no se encuentra

#eliminar de un diccionario
d.pop(5) #consulta el diciconario, si existe la llave me lo regresa y lo elimina

d.pop(55) #si eliminas algo que no existe te tira error

d.pop(55,'No existe') #devolucion por defoult si no existe

d.popitem() #elimina como si fuera una pila. Forma LIFO

len(d) #cantidad de llaves que hay en un diccionario

3 in d #si un valor existe en el diccionario

#print(dir(person))

#mostrar sus keys 
print(person.keys())

person.values()#devuelve los valores

#obtener sus keys y sus valores
print(person.items())

for k, v in d.items():   #por cada llave y cada valor de ese diccioinario hace algo
    print(f'{k}-{v}')

#eliminiar 
#del person

#eliminar sus elementos internos 
person.clear()

