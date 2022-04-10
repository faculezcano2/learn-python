'''
biblioteca.py
modelo sencillo de una biblioteca
atributos:
    libros: --coleccion de libros de la biblioteca
metodos:
    recuperarLibros(ruta) --recupera los libros desde el archivo indicado por ruta
    almacenarLibros(ruta) --almacena los libros en el archivo indicado por ruta
    agregarLibro          --agrega un libro en la coleccion de libros
    consultarLibros       --consulta los libros de la biblioteca
    menu                  --menu para la biblioteca
'''

import json
from libro import *
import os
import pathlib

class Biblioteca:
    AGREGAR_LIBRO = 1
    CONSULTAR_LIBROS = 2
    SALIR = 0


    def __init__(self):
        self._libros = []
        self.recuperarLibros('libros.json')


    #destructor de clase
    def __del__(self):
        self.almacenarLibros('libros.json')

    @property
    def libros(self):
        return self._libros
    
    @libros.setter
    def libros(self,valor):
        self._libros = valor

    @libros.deleter
    def libros(self):
        del self._libros

    def recuperarLibros(self, ruta):
        if pathlib.Path(ruta).exists(): #se fija si existe esa base de datos
            with open(ruta,'r') as archivo:
                datos = json.load(archivo)
            for lib in datos['libros']:
                self.libros.append(desdeJSON(lib))

    def almacenarLibros(self, ruta):
        with open(ruta,'w') as archivo:
            json.dump({'libros':self.libros}, archivo, cls=LibroEncoder, indent=4 )#tercer parametro indica como tiene que escribir el formato. Cuarto parametro sirve para mostrar de forma organizada la estructura json

    def agregarLibro(self):
        os.system('cls')
        print('Agregar libro')
        isbn = input('isbn: ')
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        self.libros.append(Libro(isbn,titulo,autor))

    def consultarLibro(self):
        os.system('cls')
        print('Consultar libros')
        if len(self.libros) == 0:
            print('No hay libros ingresados!')
        else:
            for lib in self.libros:
                print(f'{lib}')
                print('-'*50)


    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print(f'''  Biblioteca
{Biblioteca.AGREGAR_LIBRO}) Agregar libro
{Biblioteca.CONSULTAR_LIBROS}) Consultar libros
{Biblioteca.SALIR})Salir''')
            opc = input('Seleccione una opcion: ')
            try:
                opc = int(opc)
            except:
                opc = -1
            if opc == Biblioteca.AGREGAR_LIBRO:
                self.agregarLibro()
            elif opc == Biblioteca.CONSULTAR_LIBROS:
                self.consultarLibro()
            elif opc == Biblioteca.SALIR:
                continuar = False
            else:
                os.system('cls')
                print('Opcion no valida!')
            input('Presiona enter para continuar...')
        input('Presiona enter para salir...')