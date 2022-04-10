'''
moduloEstudiante.py
modelo sencillo de un estudiante. Hereda de la clase persona.
Atributos:
    promedio: --promedio de las calificaciones
    codigo: --codigo de alumno 
comportamientos:
    estudiar(materia): --indica que el estduiante esta estudiando esa materia
'''

from moduloPersona import Persona


class Estudiante(Persona):
    def __init__(self, nombre='', edad=None, promedio=None, codigo=''):
        super().__init__(nombre, edad)#con super accedemos a la informacion de la clase base (Persona)
        self._promedio = promedio
        self._codigo = codigo


    #interfaz del promedio
    @property
    def promedio(self):
        return self._promedio

    @promedio.setter
    def promedio(self,valor):
        if valor < 0.0:
            self._promedio = None
        else:
            self._promedio = valor

    @promedio.deleter
    def promedio(self):
        del self._promedio


    #interfaz del codigo de alumno
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self,valor):
        self._codigo = valor

    @codigo.deleter
    def codigo(self):
        del self._codigo

    def estudiar(self, materia):
        print(f'{self.nombre} se encuentra estudiando {materia} .')


    def __str__(self):
        return f'''{super().__str__()}
Promedio: {self.promedio}
codigo: {self.codigo}'''