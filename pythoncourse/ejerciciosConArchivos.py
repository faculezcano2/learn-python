#FILTRAR Y BUSCAR ARCHIVOS
''' 
#Script que muestre los nombres de todos los archivos contenidos en una carpeta

import pathlib #modulo que es una biblioteca para el manejo de rutas

ruta = pathlib.Path('.') #toma la ruta de la carpeta en la que estamos

for archivo in ruta.iterdir(): #va a iterar o recorrer nuestro directorio/carpeta
    print(archivo)
'''


''' 
#script de python que muestre el nombre de todos los archivos de una carptea pero que tengan cierta extension
import pathlib #modulo que es una biblioteca para el manejo de rutas

ruta = pathlib.Path('.') #toma la ruta de la carpeta en la que estamos

for archivo in ruta.glob('*.py'): #cualquier archivo que tenga la extensio con .py
    print(archivo)

''' 

''' 
#script en python que busque un archivo en una carpeta e indique si existe o no. En caso de existir mostrar su tamaño
import pathlib #modulo que es una biblioteca para el manejo de rutas

ruta = pathlib.Path('.') #toma la ruta de la carpeta en la que estamos

print('Programa que busca un archivo dentro de la carpeta de trabajo')
archivo=input('Nombre del archivo buscado: ')
archivo = ruta / archivo #lo que hace esto es agregar el nombre del archivo que se buysca a la ruta de donde estoy, asi lo busca bien

if(archivo.exists()):
    print(f'El archivo existe y mide {archivo.stat().st_size} bytes')
else:
    print('No existe el archivo!')

'''

'''
#scrip en python que muestre todas las extensiones unicas de archivos existentes en una carpeta

import pathlib #modulo que es una biblioteca para el manejo de rutas

def main():
    ruta = pathlib.Path('.') #toma la ruta de la carpeta en la que estamos
    
    extensiones = {archivo.suffix for archivo in ruta.iterdir()}
    print(f'extensiones: {extensiones}')




if __name__ == '__main__':
    main()
'''
#.suffix --> accedo a la extension de un archivo

#script en python que genere un diccionario con las llaves siendo las extensiones unicoas de los archivos encontrados en una carptea y los valores una lista de los nombbres de cada uno de los archivos 
'''
import pathlib #modulo que es una biblioteca para el manejo de rutas

def main():
    ruta = pathlib.Path('.') #toma la ruta de la carpeta en la que estamos
    
    diccionario = {k : [v.name for v in ruta.glob(f'*{k}')]
                    for k in {archivo.suffix for archivo in ruta.iterdir()}}

    for extension, archivos in diccionario.items():
        print(f'Extension: {extension}')
        print(f'Archivos: {archivos}')

if __name__ == '__main__':
    main()

'''

#script que organice el contenido de la carptea actual de trabajo. Se debera generar una carperta para cada tipo de archivp y todos los
#  archivosdel tipo correspondiente deberan ser movidos a la carpeta segun su tipo
import pathlib #modulo que es una biblioteca para el manejo de rutas

def main():
    ruta = pathlib.Path('.') #toma la ruta de la carpeta en la que estamos
    diccionario = { k : [v for v in ruta.glob(f'*{k}')]
                    for k in {archivo.suffix for archivo in ruta.iterdir()}}

    for extension, archivos in diccionario.items():
        carpeta = ruta / extension[1:] #generar carpeta
        carpeta.mkdir()
        for archivo in archivos:
            archivo.replace(carpeta / archivo.name) #cambiar de nombre y hacia donde se va a mover
        print('Tu carpeta ha sido clasificada!')
if __name__ == '__main__':
    main()