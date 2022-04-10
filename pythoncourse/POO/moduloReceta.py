'''
moduloReceta.py
modulo de clase de una receta de cocina
atributos: 
    -ingredientes: lista de ingredientes
    -pasos: lista de pasos o instrucciones a seguir para la receta
    -nombre: nombre de la receta

comportamientos: 
    -menu: menu de operaciones
    -agregarIngrediente: agregar un ingrediente a la receta
    -consultarIngredientes: consultar ingredientes de la receta
    -agregarPasos: agregar pasos a la receta
    -consultarPasos: consultar los pasos de la receta
'''
from moduloIngrediente import Ingrediente
import os

class Receta:
    OPC_AGREGAR_INGREDIENTE = 1
    OPC_CONSULTAR_INGREDIENTE = 2
    OPC_AGREGAR_PASO = 3
    OPC_CONSULTAR_PASOS = 4
    OPC_SALIR = 0

    def __init__(self,nombre=''):
        self._nombre = nombre
        self._ingredientes = []
        self._pasos = []

    
    def __str__(self):
        s = f'    {self.nombre}\n'
        s += 'Ingredientes: \n'
        for ingrediente in self.ingredientes:
            s+= f'{ingrediente}\n'
        s += '\nPasos: \n'
        for i, paso in enumerate(self.pasos):
            s += f'{i+1}) {paso}\n'
        return s


    #propiedades de interefaz del nombre 
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor
    
    @nombre.deleter
    def nombre(self):
        del self._nombre

    #propiedades de interefaz de los ingredientes 
    @property
    def ingredientes(self):
        return self._ingredientes

    @ingredientes.setter
    def ingredientes(self,valor):
        self._ingredientes = valor
    
    @ingredientes.deleter
    def ingredientes(self):
        del self._ingredientes

    #propiedades de interefaz de los pasos
    @property
    def pasos(self):
        return self._pasos

    @pasos.setter
    def pasos(self,valor):
        self._pasos = valor
    
    @pasos.deleter
    def pasos(self):
        del self._pasos

    #metodos/comportamientos

    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print(f'''  {self.nombre}
            {self.OPC_AGREGAR_INGREDIENTE}) Agregar ingrediente
            {self.OPC_CONSULTAR_INGREDIENTE}) Consultar ingredientes
            {self.OPC_AGREGAR_PASO}) Agregar un paso
            {self.OPC_CONSULTAR_PASOS}) Cosultar pasos
            {self.OPC_SALIR}) Salir
            ''')

            opc =  int(input('Selecciona una opcion: '))
            
            if opc == self.OPC_AGREGAR_INGREDIENTE:
                self.agregarIngrediente()
            elif opc == self.OPC_CONSULTAR_INGREDIENTE:
                self.consultarIngredientes()
            elif opc == self.OPC_AGREGAR_PASO:
                self.agregarPaso()
            elif opc == self.OPC_CONSULTAR_PASOS:
                self.consultarPasos()
            elif opc == self.OPC_SALIR:
                continuar = False
            else:
                print('Opcion no valida!')
            input('Presiona enter para continuar...')
        print('Adios!')


    def agregarIngrediente(self):
        continuar = True
        while continuar:
            os.system('cls')
            print('Agregar Ingrediente')
            nombre = input('Nombre: ')
            cantidad = -1
            while cantidad <= 0:
                cantidad = input('Cantidad: ')
                try:
                    cantidad = float(cantidad)
                except:
                    cantidad = 0
            unidad = input('Unidad: ')

            ingrediente = Ingrediente(nombre, cantidad, unidad)
            self.ingredientes.append(ingrediente)
            respuesta = input('Desea agregar otro ingrediente? (s/n)')
            if respuesta != 's' and respuesta != 'S':
                continuar =  False 

    
    
    def consultarIngredientes(self):
        os.system('cls')
        print('Ingredientes: ')
        if(len(self.ingredientes) == 0):
            print('No hay ingredientes cargados!')
        else:
            for ingrediente in self.ingredientes:
                print(f'{ingrediente}')

    

    def agregarPaso(self):
        continuar = True
        while continuar:
            os.system('cls')
            print('Agregar paso: ')
            paso = input('Paso: ')
            self.pasos.append(paso)
            respuesta = input('Desea agregar otro paso? (s/n)')
            if respuesta != 's' and respuesta != 'S':
                continuar =  False 



    def consultarPasos(self):
        os.system('cls')
        print('Pasos: ')
        if (len(self.pasos) == 0):
            print('No hay pasos registrados')
        else:
            for i, paso in enumerate(self.pasos):      #enumerate() lo que hace es darle valor ( 1), 2), 3), 4), etc) a cada for que se ingrese
                print(f'{i+1}) {paso}')
