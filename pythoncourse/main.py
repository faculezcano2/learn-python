#procedimiento por el cual debe empezar el programa
#se lo define como main al ser el principal
#lo que viene a ser hacer modulos y llamar a los modulos desde un programa principal

def saludo(nombre):
    print(f'Hola {nombre}')

def main():
    usuario = input("Hola como te llamas?")
    saludo(usuario)

if __name__ == "__main__":
    main()