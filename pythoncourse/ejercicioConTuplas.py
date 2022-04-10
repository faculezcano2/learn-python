'''
Script en python que permita almacenar registros de las mascotas del usuario. Para cada mascota se pedira el nombre, la edad, el peso y el 
tipo de mascota.Para permitir la posibilidad de tener varias mascotas se creara una lista en la cual se guarden los registros de cada mascota, 
es decir un a lista de tuplas. El programa debera contar con un menu ciclico que permita registrar y consultar las mascotas
'''

import os

REGISTRAR = 1
CONSULTAR = 2
SALIR = 0

def imprimirMenu():
    os.system('cls')
    print(f''' Mis Mascotas
    {REGISTRAR}) Registrar mascota
    {CONSULTAR}) Consultar mascotas
    {SALIR}) Salir
    ''')

def registrar(mascotas):
    os.system('cls')
    print(' Registrar mascota:')
    nombre = input('Nombre: ')
    edad = int(input('Edad: '))
    peso = float(input('Peso: '))
    tipo = input('Tipo mascota: ')
    mascotas.append((nombre, edad, peso, tipo))


def consultar(mascotas):
    os.system('cls')
    print('Mis mascotas:')
    if(len(mascotas) == 0):
        print('Aun no registraste mascotas!')
    else:
        for mascota in mascotas:
            nombre, edad, peso, tipo = mascota
            print(f'Nombre: {nombre}')
            print(f'Edad: {edad}')
            print(f'Peso: {peso}')
            print(f'Tipo: {tipo}')
            print('-----------------------')

def main():
    misMascotas = []
    continuar = True
    while continuar:
        imprimirMenu()
        opc =  int(input('Selecciona una opcion: '))
        if opc == REGISTRAR:
            registrar(misMascotas)
        elif opc == CONSULTAR:
            consultar(misMascotas)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opcion invalida...')
        input('Presiona enter para continuar...')
    input('Adios!')


if __name__ == '__main__':
    main()
