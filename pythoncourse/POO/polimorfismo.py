'''
el polimorfismo, esto se refiere a que ambas personas tengan una misma caracteristica pero que cada uno ejecute su caracteristica de
forma distinta
ejemplo dos personajes de un juego, ambos atacan pero cada uno ataca de una forma distinta

la idea es tener clases relacionadas de alguna forma/organizadas en una jerarquia, y que los objetos de esa clase puedan respopnder de forma
distinta frente a esos mensajes

vamos a usar herencia como ya vimos y ademas vamos a "sobre cargar" algunas funciones o el metodo para el cual pueden responder de forma
distinta los objetos debera ser sobre cargado eso se logra con metodos virtuales o eso nos dice la teoria, pero en python es mas sencillo y
vamos a poder sobre cargar las funciones sin hacer algo extra simplemente todas las funciones ya son virtuales y todas las clases va a pooder 
implementarlas a su forma
'''

'''
polimorfismo.py 
script que simule un personaje y un grupo de enemigos que podran atacar al personaje principal de forma especial segun su naturalez.
Los enemigos seran modelados con clases y se hara uso de polimorfismo para permitirles atacar de manera personalizada.
'''
import enemigo
import os
import random


def main():
    enemigos =[]
    for i in range(5):
        tipoEnemigo = random.randint(0,len(enemigo.tipos)-1)
        if tipoEnemigo == enemigo.MOMIA:
            enemigos.append(enemigo.Momia())
        elif tipoEnemigo == enemigo.ZOMBIE:
            enemigos.append(enemigo.Zombie())
        else:
            enemigos.append(enemigo.Vampiro())
        
    personaje =  {'energia':100, 'fuerza':6}
    GANANCIA_DE_ENERGIA = 5
    INCREMENTO_DE_FUERZA = 4

    while personaje['energia'] > 0 and len(enemigos) > 0:
        while personaje['energia'] > 0 and enemigos[0].energia > 0:
            os.system('cls')
            print(f'Energia: {personaje["energia"]}     {enemigos[0].tipo}: {enemigos[0].energia}')
            enemigos[0].atacar()
            personaje['energia'] -= enemigos[0].fuerza 
            if personaje['energia'] > 0:
                print(f'Has atacado a {enemigos[0].tipo} y causaste {personaje["fuerza"]} de daño.')
                enemigos[0].energia -= personaje['fuerza']
                input('continuar batalla...')
        if personaje['energia'] > 0:
            os.system('cls')
            print(f'Energia: {personaje["energia"]}     {enemigos[0].tipo}: {enemigos[0].energia}')
            print(f'Has derrotado a {enemigos[0].tipo}')
            print(f'Has recuperado {GANANCIA_DE_ENERGIA} de energia')
            print(f'Tu fuerza a aumentado {INCREMENTO_DE_FUERZA}.')
            personaje['energia'] += GANANCIA_DE_ENERGIA
            personaje['fuerza'] += INCREMENTO_DE_FUERZA
            enemigos.pop(0)
            input('Continuar aventura...')
    if personaje['energia'] > 0:
        print('Has vencido a todos tus enemigos!')
    else:
        print('Has sido vencido! X.X')


if __name__ == '__main__':
    main()