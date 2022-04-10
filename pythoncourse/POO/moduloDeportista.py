'''
moduloDeportista.py
modulo de un deportista. Hereda de la clase Persona
atributos:
    deporte: --deporte que prectica la persona
comportamientos:
    entrenar: --entrena deporte asignado
'''

from moduloPersona import Persona


class Deportista(Persona):
    def __init__(self, nombre='', edad=None, deporte=''):
        super().__init__(nombre, edad)#con super accedemos a la informacion de la clase base (Persona)
        self._deporte = deporte
    

    @property
    def deporte(self):
        return self._deporte

    @deporte.setter
    def deporte(self,valor):
        self._deporte = valor

    @deporte.deleter
    def deporte(self):
        del self._deporte

    def entrenar(self):
        print(f'{self.nombre} entrena {self.deporte}')


    def __str__(self):
        return f'''{super().__str__()}
Deporte: {self.deporte}'''