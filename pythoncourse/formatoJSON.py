'''
es un formato que nos permite hacer transferencia de datos/ intercambio de informacion entre distintas apps y esta inspirado en la manera que javascript se definen los objetos de manera literal
'''

import json #para poder trabajaron con json
'''json.dumps  #convertir informacion en formato json
json.loads #convertir de json a python
json.dump #nos permite enviar info hacia un archivo
json.load #nos permite recuperar info de un archivo

entero = 33
jsonEntero = json.dumps(entero)  #convierte a formato json
print(type(jsonEntero))
pythonEntero = json.loads(jsonEntero)   #convierte a formato python
print(type(pythonEntero))


cadena = 'Hola mundo'
jsonCadena= json.dumps(cadena)
print(type(jsonCadena))
pythonCadena = json.loads(jsonCadena)
print(type(jsonCadena))


lista = [1,2,'tres']
jsonLista = json.dumps(lista) #representa en formato json la lista
pythonLista = json.loads(lista) #vuelve a la version de python


diccionario = {'entero':1, 'cadena':'hola', 'lista':[1,2,'tres', 4.4]}
jsonDiccionario = json.dumps(diccionario)
print(type(jsonDiccionario))
pythonDiccionario = json.loads(jsonDiccionario)
print(type(pythonDiccionario))
'''
diccionario = {'entero':1, 'cadena':'hola', 'lista':[1,2,'tres', 4.4]}

#vamos a escribir en un archivo el diccionario
with open('archivo_json.json', 'w') as archivo: #abrimos el archivo
    json.dump(diccionario, archivo) #envio la info con dump(que quiero enviar, donde lo quiero escribir)


#vamos a recuperar esa info
with open('archivo_json.json', 'r') as archivo: #abrimos el archivo
    datos = json.load(archivo) #envio la info con dump(que quiero enviar, donde lo quiero escribir)

print(datos)