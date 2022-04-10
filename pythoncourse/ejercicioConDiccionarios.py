#AGENDA

'''
script en python que implemente una agenda de contactos haciendo uso de un diccionario. Para el diccionario las llaves sera los nombres y 
como valor estara una tupla que contenga el numero de telefono y el contacto electronico. Se mantendra un menu con las siguientes opciones:

1) Agregar contacto
2) Mostrar contactos
3) buscar un contacto
4) modificar un contacto
5) eliminar contacto
6) salir
'''

import email
import os

SALIR = 0 
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
MODIFICAR = 4
ELIMINAR = 5


def mostrarMenu():
    os.system('cls')
    print(f'''    ---MI AGENDA---
        {AGREGAR}) Agregar contacto
        {MOSTRAR}) Mostrar contactos
        {BUSCAR}) Buscar contactos
        {MODIFICAR}) Modificar contactos
        {ELIMINAR}) Eliminar contacto
        {SALIR}) Salir
    ''')

def agregarContacto(agenda):
    os.system('cls')
    print('Agregar contacto')
    nombre = input('Nombre:')
    if(agenda.get(nombre)):
        print('Ya existe el contacto!')
    else:
        telefono = input('Telefono: ')
        email = input('Email: ')
        agenda.setdefault(nombre, (telefono, email))
        print('Contacto agregado!')


def mostrarContactos(agenda):
    os.system('cls')
    print('Mostar mis contactos')
    if(len(agenda) > 0):
        for contacto, datos in agenda.items():
            print(f'Nombre: {contacto}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print('----------------------------------------------')
    else:
        print('No hay contactos registrados!')


def buscarContacto(agenda):
    os.system('cls')
    print('Buscar contacto')
    if(len(agenda) > 0):
        nombre =  input('Nombre a buscar: ')
        encontrados = 0
        for contacto, datos in agenda.items():
            if(nombre in contacto):
                print(f'Nombre: {contacto}')
                print(f'Telefono: {datos[0]}')
                print(f'Email: {datos[1]}')
                print('----------------------------------------------')
                encontrados += 1
        if (encontrados == 0):
            print('No se encontro el contacto!')
        else:
            print(f'Se encontraron {encontrados} contactos')
    else:
        print('No hay contactos registrados!')



def modificarContactos(agenda):
    os.system('cls')
    print('Modificar contactos')
    if(len(agenda) > 0):
        nombre = input('Nombre a modificar: ')
        if(agenda.get(nombre)):
            datos = agenda.get(nombre)
            print('Informacion: ')
            print(f'Nombre: {nombre}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print('----------------------------------------------')
            print('Ingresa los nuevos datos: ')
            telefono = input('Telefono: ')
            email = input('Email: ')
            agenda[nombre] = (telefono, email)
            print('Datos actualizados con exito!')
        else:
            print('No existe el contacto!')
    else:
        print('No hay contactos agendados!')


def eliminarContacto(agenda):
    os.system('cls')
    print('Eliminar contacto')
    if(len(agenda) > 0):
        nombre = input('Nombre: ')
        if (agenda.get(nombre)):
            agenda.pop(nombre)
            print('Contacto eliminado!')
        else:
            print('No existe el contacto!')
    else:
        print('No hay contactos registrados!')



def main():
    continuar = True
    agenda = {}
    while continuar:
        mostrarMenu()
        opc = int(input('Elija una opcion: '))
        if (opc == AGREGAR):
            agregarContacto(agenda)
        elif (opc == MOSTRAR):
            mostrarContactos(agenda)
        elif (opc == BUSCAR):
            buscarContacto(agenda)
        elif (opc == MODIFICAR):
            modificarContactos(agenda)
        elif (opc == ELIMINAR):
            eliminarContacto(agenda)
        elif (opc == SALIR):
            continuar = False
        else:
            print('Valor invalido!')
        input('Presiona enter para continuar...')
        print('Adios!')

if __name__ == '__main__':
    main()
