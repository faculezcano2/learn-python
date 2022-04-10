class Pelicula:
    def __init__(self, titulo='', director='', anio=None, duracion=None):
        self._titulo = titulo
        self._director = director
        self._anio = anio
        self._duracion = duracion

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self,valor):
        self._titulo = valor

    @titulo.deleter
    def titulo(self):
        del self._titulo

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self,valor):
        self._director = valor

    @director.deleter
    def director(self):
        del self._director

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self,valor):
        self._anio = valor

    @anio.deleter
    def anio(self):
        del self._anio


    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self,valor):
        self._duracion = valor

    @duracion.deleter
    def duracion(self):
        del self._duracion

    def __str__(self):
        ESPACIOS = 10
        return f'''{"Titulo:" : <{ESPACIOS}}{self.titulo}
{"Director:" : <{ESPACIOS}}{self.director}
{"Año:" : <{ESPACIOS}}{self.anio}
{"Duracion:" : <{ESPACIOS}}{self.duracion} min'''


    #lt: lower than. Sobrecargando los operadores
    def __lt__(self, otro):
        return self.titulo < otro.titulo 
    
    def __eq__(self, otro):
        return self.titulo == otro.titulo and self.anio == otro.anio
    
    def __le__(self, otro):
        return self < otro or self == otro