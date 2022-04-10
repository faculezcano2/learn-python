#igual que el registros de peliculas de "archivosCSV" pero esta vez el primer renglon va a ser la key de cada cosa 
'''
script que solicite al usuario una cantidad de peliculas a registrar y los almacene en un archivo .csv con encabezado para posteriormente 
recuperarlos. De cada pelicula se almacenara titulo, duracion y el año
'''


import os
import csv
import pathlib


def registrarPeliculas(nombreArchivo):
    cantidad = int(input('Cantidad de peliculas a registrar: '))
    campos = ['Titulo', 'Duracion', 'Año']

    if not pathlib.Path(nombreArchivo).exists():
        with open(nombreArchivo, 'w', newline='') as archivoCSV:
            writer = csv.DictWriter(archivoCSV, fieldnames=campos) #ahora tenemos un diccionario de escritura, "fieldnames" es el encabezado que queremos
            writer.writeheader() #escribir el encabezado


    with open(nombreArchivo, 'a', newline='') as archivoCSV:
        writer = csv.DictWriter(archivoCSV, fieldnames=campos ) #objeto para poder escribir
        for i in range(cantidad):
            os.system('cls')
            titulo = input('Titulo: ')
            duracion =  input('Duracion: ')
            anio = input('Año: ')
            writer.writerow({'Titulo':titulo, 'Duracion':duracion, 'Año':anio})


def recuperarPeliculas(nombreArchivo):
    os.system('cls')
    print('Peliculas registradas:')
    with open(nombreArchivo, 'r', newline='') as archivoCSV:
        reader = csv.DictReader(archivoCSV)
        for linea in reader:
            for campo, valor in linea.items():
                print(f'{campo}:{valor}')
            print('-'*50)


def main():
    archivo = 'peliculasEncabezado.csv'
    registrarPeliculas(archivo)
    recuperarPeliculas(archivo)


if __name__ == '__main__':
    main()