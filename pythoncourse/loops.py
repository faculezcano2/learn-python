'''foods = ["aples", "cheese", "milk", "bacon", "graves"]

for i in foods:
    print("debes comprar ",i)
'''
#-------------------------------------
'''
#para decrementar en python seria de la siguiente manera
for i in range (10,-1,-1):
    print(i)

#contador que espera 1 segundo para imprimir el siguiente num
import os
import time

for i in range (10,-1,-1):
    os.system("cls")
    print(i)
    time.sleep(1)
print("bai")
'''
#TABLA DE MULTIPLICAR QUE DECIDA EL USUARIO
def tabla():
    numero = int(input("De que numero deseas ver la tabla de multiplicar?"))
    limite = int(input("hasta que multiplo deseas ver la tabla?"))
    print(f'tabla del {numero}')
    for multiplo in range(1,limite+1):
        print(f'{numero}x{multiplo} = {numero * multiplo}')


#tabla()

#tablas de multiplicar desde la 1 hasta la 10
def todasLasTablas():
    for i in range(1,11):
        print(f'TABLA DEL {i}')
        for multiplo in range(1,11):
            print(f'{i}x{multiplo} = {i * multiplo}')


#todasLasTablas()

def deletrar():
    palabra = input("ingrese la frase a deletrear")
    for letra in palabra:
        print(letra)

#deletrar()

def promedio():
    suma=0
    cant = int(input("cuantos numeros vas a registrar?"))
    for num in range(1,cant+1):
        numero = int(input(f'ingresa el numero {num}: '))
        suma = suma + numero
    
    print(suma / cant)

#promedio()

#cronometro de 24 hs con retraso de 1seg y limpieza de pantalla 
import os
import time
def cronometro():
    for hora in range(24):
        for minuto in range(60):
            for segundos in range(60):
                os.system("cls")
                print(f'{hora}:{minuto}:{segundos}')
                time.sleep(1)

#cronometro()
