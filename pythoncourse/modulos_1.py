'''
script que solicite al usuario una cantidad de peliculas a registrar y los almacene en un archivo .csv para posteriormente recuperarlos.
De cada pelicula se almacenara titulo, duracion y el año
'''
#este lo usamos para usar el modulo de conversiones creado por nosotros en la linea 33 la "duracion" transformaral con la funcion del mdoulo conversiones

import os
import csv           #modulo que tiene python dedicado a csv
import conversiones


def registrarPeliculas(nombreArchivo):
    cantidad = int(input('Cantidad de peliculas a registrar: '))
    with open(nombreArchivo, 'a', newline='') as archivoCSV:    #para los archivos csv python necesita un tercer argumento que se llama "newline" y va con comillas vacias
        writer = csv.writer(archivoCSV, delimiter=',') #se le pasa por parametro el archivo con el que va a trabajar y el delimitador que queremos que utilice
        for i in range(cantidad):
            os.system('cls')
            titulo = input('Titulo: ')
            duracion = input('Duracion: ')
            año = input('Año: ')
            writer.writerow([titulo, duracion, año])  #escribe un renglon


def recuperarPeliculas(nombreArchivo):
    os.system('cls')
    print('Peliculas registradas: ')
    with open(nombreArchivo, 'r', newline='') as archivoCSV:
        reader = csv.reader(archivoCSV)   #creamos una variable para lectura a travez de nuestro modulo csv
        for linea in reader: 
            print(f'Titulo: {linea[0]}')
            minutos = int(linea[1])
            h,m,s = conversiones.minutosAHoras(minutos, 0)
            print(f'Duracion: {h}:{m}:{s}')
            print(f'Año: {linea[2]}')
            print('-'*50)

def main():
    archivo = 'peliculas.csv'
    registrarPeliculas(archivo)
    recuperarPeliculas(archivo)


if __name__ == '__main__':
    main()