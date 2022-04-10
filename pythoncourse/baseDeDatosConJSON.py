'''
baseDeDatosConJSON.py
script que permita el registro y consulta de libros dentro de una biblioteca.
Los libros seran modelados dentro de una clase y podran ser almacenados en un archivo con formato JSON y recuperados desde el mismo.
La biblioteca sera modelada dentro de una clase que podra administrar a los objetos de tipo libro.
'''
from biblioteca import Biblioteca


def main():
    bib = Biblioteca()
    bib.menu()

if __name__ == '__main__':
    main()