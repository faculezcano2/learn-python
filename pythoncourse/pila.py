#coleccion de objetos, la forma en acceder a sus datos es de tipo LIFO last in first out
#se agrega un elemento con append() y se elimina con pop()


#script que solicite una expresion aritmetica y el programa le indique si dicha expresion esta balanceada, es decir, si tiene la misma cnatidad de parentesis de apertura y de cierre

def bienParentesis(expresion):
    pila = []
    for i in expresion:
        if i == '(':
            pila.append('(')
        elif i==')':
            if len(pila) > 0:
                pila.pop()
            else:
                return False
    return len(pila) == 0


def main():
    print('escribe una expresion aritmetica y te dire si esta bien con respecto a los parentesis.')
    e = input('Expresion: ')
    valida = bienParentesis(e)
    if valida:
        print('La expresion esta balanceada')
    else:
        print('La expresion no esta balanceada')

if __name__=='__main__':
    main()

