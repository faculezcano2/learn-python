'''
moduloPrenda.py

definicion para la clase prenda con los atributos:
tipo
talle
'''



class Prenda:
    def __init__(self):
        self._tipo = ''
        self._talle = ''

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self,valor):
        self._tipo = valor
    
    @tipo.deleter
    def tipo(self):
        del self._tipo

    @property
    def talle(self):
        return self._talle

    @talle.setter
    def talle(self,valor):
        self._talle = valor

    @talle.deleter
    def talle(self):
        del self._talle

    def __str__(self):
        return f'''
        Tipo:{self.tipo}
        talle:{self.talle}
        '''
    