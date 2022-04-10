import random
import os

MaxFallos = 5

paises = ['antigua y barbuda','argentina','bahamas','barbados','belice','bolivia','brasil','canada','chile','colombia','costa rica','cuba','dominicana','ecuador','el salvador','estados unidos','granada','guatemala','guyana','haiti','honduras','jamaica','mexico','nicaragua','panama','paraguay','peru','republica dominicana','san cristobal y nieves','san vicente y las granadinas','santa lucia','surinam','trinidad y tobago', 'uruguay', 'venezuela']

def crearCadenas():
    pais = random.choice(paises) #elije un pais random
    secreto = '_'*len(pais)
    return pais, secreto


def reemplazarLetra(original, secreto, letra):
    cantidad = original.count(letra)
    inicio = 0
    for i in range(cantidad):
        pos = original.find(letra, inicio)
        secreto = secreto[:pos] + letra + secreto[pos+1:]
        inicio = pos + 1
    return secreto


def ahorcado():
    print(f'Hola, vamos a jugar al ahorcado. La palabra secreta sera el nombre de uno de los {len(paises)} paises del continente americano. Tienes {MaxFallos} oportunidades de fallar, las palabras estaran en minuscula y sin acentos.')
    input('Presiona enter para empezar')
    original, secreto = crearCadenas()
    fallos = 0
    while (secreto != original and fallos < MaxFallos):
        os.system('cls')
        print(f'pablabra: {secreto}')
        s = input('Cual letra quieres descubrir?')
        if (s in original):
            secreto =  reemplazarLetra(original,secreto,s)
            print('Bien hecho! La letra es parte de la plabra.')
        else:
            print('Lo siento la letra no es parte de la palabra')
            fallos += 1
            print(f'LLevas un total de {fallos}')
        input('Presiona enter para continuar...')
    if (secreto == original):
        print(f'Felicidades, el pais es {secreto}')
    else:
        print(f'Fallaste, el pais era {original}')
    print('Adios!')


def main():
    ahorcado()

if __name__ == '__main__':
    main()

