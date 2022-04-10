import os

listaE=[]

AGREGAR = 1
INSERTAR = 2
MOSTRAR = 3
BUSCAR = 4
ELIMINAR = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 0

def imprimirMenu():
    os.system('cls')
    print(f'''
     Menu lista frutas
        {AGREGAR})Agregar
        {INSERTAR})Insertar
        {MOSTRAR})Mostrar
        {BUSCAR})Buscar
        {ELIMINAR})Eliminar
        {ORDENAR})Ordenar
        {LIMPIAR})Limpiar
        {SALIR})Salir''')


def agregarElemento():
    print("Agregar")
    elemento = input('Que desea agregar: ')
    listaE.append(elemento)
    print("Elemento agregado.")


def insertarElemento():
    print("Insertar")
    elemento = input("Que desea insertar:")
    posicion = int(input("En que posicion desea insertar:"))
    listaE.insert(posicion,elemento)
    print("Elemento insertado.")


def mostrarElementos():
    print("----mostrar----")
    if len(listaE) > 0:
        for i in listaE:
            print(i)
    else:
        print("No hay elementos en la lista")


def buscarElemento():
    print("buscar")
    if len(listaE) > 0:
        nombre = input('Nombre a buscar:')
        if nombre in listaE:
            cantidad = listaE.count(nombre)
            inicio = 0
            for i in range(cantidad):
                pos = listaE.index(nombre, inicio)
                print(f'{nombre} se encuentra en la posicion {pos+1}.')
                inicio = pos + 1 
        else: 
            print(f'{nombre} no esta en la lista')
    else:
        print("No hay elementos en la lista")


def eliminarElemento():
    print("Eliminar")
    if len(listaE) > 0:
        for i in range(len(listaE)):
            print(f'{i+1}. {listaE[i]}')
        print('0. Cancelar.')
        pos = int(input(f'posicion a eliminar (1 hasta {len(listaE)}:)'))
        if 0 < pos <=len(listaE):
            listaE.pop(pos-1)
            print('el elemento se elimino')
        else:
            print('no se eliminara ningun elemento')
    else:
        print("No hay elementos a eliminar")

def ordenarElementos():
    print('Eliminar')
    if len(listaE) > 0:
        listaE.sort()
        print('registros ordenados alfabeticamente')
    else:
        print('no hay elementos en la lista')


def limpiarElementos():
    print("Limpiar")
    listaE.clear()
    print("Lista eliminada")


def main():
    continuar = True
    while continuar:
        imprimirMenu()
        opcion=int(input('Selecciona una opcion:'))
        os.system('cls')
        if opcion == AGREGAR:
            agregarElemento()
        elif opcion == INSERTAR:
            insertarElemento()
        elif opcion == MOSTRAR:
            mostrarElementos()
        elif opcion == BUSCAR:
            buscarElemento()
        elif opcion == ELIMINAR:
            eliminarElemento()
        elif opcion == ORDENAR:
            ordenarElementos()
        elif opcion == LIMPIAR:
            limpiarElementos()
        elif opcion == SALIR:
            print('CHAU!')
            continuar = False
        else:
            print('Opcion no valida')
        input('presiona enter para continuar')

if __name__ == '__main__':
    main()
