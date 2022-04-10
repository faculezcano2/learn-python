'''
libro.py
modelo sencillo de un libro
atributos:
    isbn:  --isbn del libro
    titulo:  --titulo del libro
    autor: --autor del libro
'''

import json

class Libro:
    def __init__(self,isbn='',titulo='',autor=''):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
    
    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, valor):
        self._isbn = valor
    
    @isbn.deleter
    def isbn(self):
        del self._isbn


    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor
    
    @titulo.deleter
    def titulo(self):
        del self._titulo


    
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, valor):
        self._autor = valor
    
    @autor.deleter
    def autor(self):
        del self._autor


    def __str__(self):
        ESPACIOS = 8
        return f'''{"isbn: " : <{ESPACIOS}}{self.isbn}
{"titulo: " : <{ESPACIOS}}{self.titulo}
{"autor: " : <{ESPACIOS}}{self.autor}'''


#serializacion de la informacion: convertir la info de formato python a formato JSON
class LibroEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Libro): #se fija si el objeto es de tipoo libro 
            return {'isbn':obj.isbn, 'Titulo':obj.titulo, 'Autor':obj.autor } #lo pone del formato que debe ser
        return json.JSONEncoder.default(self, obj) #sino devuelve lo que se escribio


#convertir a partir del formato JSON a un Libro
def desdeJSON(diccionario):
    return Libro(diccionario['isbn'], diccionario['Titulo'], diccionario['Autor'])