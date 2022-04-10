#son el medio para hacer que la informacion permanezca en nuestra computadora

#modos dentro de python para utiliz<ar nustrsos archivos:
#open(nombreArchivo, modoApertura) forma de abrir el archivo
#'r' - lectura
#'w' - escritura
#'a' - agregar
#'r+' - lectura y escritura
#'b' - binario
''' 
archivo = open('miArchivo.txt','w')
#si el archivo no existe y utilizo 'w' lo crea automaticamente por mi

archivo.close() #siempre que se abre un archivo debe cerrarse por seguridad

archivo = open('miArchivo.txt','w') #se abre en modo escritura y para agregar contenido hacemos:
archivo.write('hola archivo') #esto va a devolver la cantidad de bytes o simbolos que se escribieron en el archivo
archivo.close()

archivo = open('miArchivo.txt','r') #leer lo que hay en el archivo
archivo.read() #asi lo lee y lo muestra
archivo.close()

archivo = open('miArchivo.txt','r+') #lo hace de lectura y escritura
archivo.write('Ootra cadena') #puedo escribir, pero reemplaza el contenido desde el inicio hasta la cantidad de caracterez que tenga lo que agrego
archivo.read() #puedo leer pero lee solo lo nuevo agregado
archivo.close()

archivo = open('miArchivo.txt','w') #como escritura
archivo.write('hola otra cosa') #ahora a diferencia de antes, borra todo
archivo.close()

archivo = open('miArchivo.txt','a') #modo solo agregar
archivo.write('hola catrasca') #ahora escribe nuevo contenido a partir de lo anterior ya existente
archivo.close()

#siempre tenemso que estar abriendo y cerrando el archivo y aveces se nos olvida cerrarlo y esto es peliogroso, para poder evitar abrirlo y cerrrarlo todo el tiempo existe un modo distinto que lo que hace es crear un contexto donde nuestro archivo esta abierto, una vez que salimos de ese contexto se cierra
#es asi
with open('miArchivo2.txt','w') as archivo:
    for i in range(11):
        archivo.write(f'{i}\n')


with open('miArchivo2.txt','a') as archivo:
    archivo.write('Hola catrasca')
'''

#prueba de escritura y lectura de un archivo

with open('miArchivo.txt','w') as archivo:
    for i in range(11):
        archivo.write(f'{i}\n')


with open('miArchivo.txt','a') as archivo:
    archivo.write('Hola catrasca\n')#agrego sin modificar lo anterior

with open('miArchivo.txt','a') as archivo:
    archivo.write('Hola catrascaaa\n')#agrego sin modificar lo anterior

with open('miArchivo.txt','r') as archivo:
    for linea in archivo:
        print(linea) #lee todas las lineas que hay 


