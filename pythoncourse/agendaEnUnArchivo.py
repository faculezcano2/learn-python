'''
script en python que implemente una agenda de contactos haciendo uso de un diccionario. Para el diccionario las llaves sera los nombres y 
como valor estara una tupla que contenga el numero de telefono y el contacto electronico. La agenda se guardara en un archivo de texto del 
cual se podran recuperar los contactos y en el cual se podran agregar los nuevos contactos.Se mantendra un menu con las siguientes opciones:

1) Agregar contacto
2) Mostrar contactos
3) buscar un contacto
0) salir
'''

import pathlib
import os


SALIR = 0 
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3


def mostrarMenu():
    os.system('cls')
    print(f''' Mi agenda
        {AGREGAR}) Agregar contacto
        {MOSTRAR}) Mostar contacto
        {BUSCAR}) Buscar contacto
        {SALIR}) Salir
        ''')


def cargarAgenda(agenda, nombreArchivo):
    if(pathlib.Path(nombreArchivo).exists()):
        with open(nombreArchivo,'r') as archivo:
            for linea in archivo:
                contacto, telefono, email = linea.strip().split(',')
                agenda.setdefault(contacto, (telefono, email))
    else:
         with open(nombreArchivo,'w') as archivo:
             pass


def agregarContacto(agenda, nombreArchivo):
    os.system('cls')
    print('Agregar contacto')
    nombre = input('Nombre: ')
    if(agenda.get(nombre)):
        print('Contacto ya existente!')
    else:
        telefono = input('Telefono: ')
        email = input('Email: ')
        agenda.setdefault(nombre, (telefono, email))
        with open(nombreArchivo, 'a') as archivo:
            archivo.write(f'{nombre}, {telefono}, {email}\n')
        print('Contacto agregado!')


def mostrarContactos(agenda):
    os.system('cls')
    print('Mis contactos')
    if (len(agenda) > 0):
        for contacto, datos in agenda.items():
            print(f'Nombre: {contacto}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print('-'*50)
    else:
        print('No hay contactos agendados!')



def buscarContacto(agenda):
    os.system('cls')
    print('Buscar contacto')
    if(len(agenda) > 0):
        nombre = input('Nombre: ')
        coincidencias = 0
        for contacto, datos in agenda.items():
            if( nombre in contacto):
                print(f'Nombre: {contacto}')
                print(f'Telefono: {datos[0]}')
                print(f'Email: {datos[1]}')
                coincidencias += 1
                print('-'*50)
        if (coincidencias == 0):
            print('No se encontro el contacto')
        else:
            print(f'Se encontraron {coincidencias} contactos!')
    else:
        print('No hay contactos registrados!')

def main():
    continuar = True
    agenda = dict()
    nombreArchivo = 'agenda.txt'
    cargarAgenda(agenda, nombreArchivo)

    while continuar:
        mostrarMenu()
        opc = int(input('Seleccione la opcion: '))
        if opc == AGREGAR:
            agregarContacto(agenda, nombreArchivo)
        elif opc == MOSTRAR:
            mostrarContactos(agenda)
        elif opc == BUSCAR:
            buscarContacto(agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opcion no valida!')
        input('Presiona enter para continuar...')
    print('Adios!')


if __name__ == '__main__':
    main()
