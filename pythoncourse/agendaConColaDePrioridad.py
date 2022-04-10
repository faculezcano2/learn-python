import os
import queue


AGENDAR = 1
ATENDER = 2
SALIR = 0

def ImprimirMenu():
    os.system('cls')
    print(f''' MI AGENDA
        {AGENDAR}) Agendar Evento
        {ATENDER}) Atender Evento
        {SALIR}) Salir
    ''')


def agendar(ag):
    print('Agendar Evento')
    evento= input('Evento: ')
    ag.put(evento)


def atender(ag):
    print('Atender Evento')
    if(ag.empty()):
        print('No hay eventos para atender')
    else:
        evento = ag.get() 
        print(f'Evento: {evento}')
    

def main():
    agenda = queue.PriorityQueue()
    continuar = True
    while continuar:
        ImprimirMenu()
        opc = int(input('Selecciona una opcion: '))
        os.system('cls')
        if (opc == AGENDAR):
            agendar(agenda)
        elif(opc == ATENDER):
            atender(agenda)
        elif(opc == SALIR):
            continuar = False
        else:
            print('Opcion invalida...')
        input('Presiona enter para continuar...')
    print('Adios!')



if __name__ == '__main__':
    main()
