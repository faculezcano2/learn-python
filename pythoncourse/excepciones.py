#se usa cuando hay un error que se ejecutte eso ante el error

'''
script que muestre un menu de seleccion de personajes y solicite al usuario seleccione uno de ellos para ver sus detalles. el script debera
poder tolerar fallos en la entrada por parte del usuario.
'''
import os

MAGO = 1 
GUERRERO = 2
SACERDOTISA = 3
SALIR = 0

def mostrarMenu():
    os.system('cls')
    print(f'''   Personajes
        {MAGO}) Mago
        {GUERRERO}) Geguerro
        {SACERDOTISA}) Sacerdotisa
        {SALIR}) Salir
    ''')


def main():
    continuar = True
    while continuar:
        mostrarMenu()
        opc = input('Seleccine un personaje: ')

        try:
            opc = int(opc)
        except:
            opc = -1

        os.system('cls')
        if opc == MAGO:
            print('MAGO')
            print('Fuerza: 30')
            print('Energia: 50')
            print('Habilidad: 30')
        elif opc == GUERRERO:
            print('GUERRERO')
            print('Fuerza: 40')
            print('Energia: 60')
            print('Habilidad: 20')
        elif opc == SACERDOTISA:
            print('SACERDOTISA')
            print('Fuerza: 15')
            print('Energia: 35')
            print('Habilidad: 20')
        elif opc == SALIR:
            continuar = False
        else:
            print('Opcion no valida!')
        input('Presiona enter para continuar...')
    print('Adios!')


if __name__ == '__main__':
    main()