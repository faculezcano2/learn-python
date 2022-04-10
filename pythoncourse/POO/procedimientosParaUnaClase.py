'''
cript que implemente una clase Persona con las siguientes propiedades:
nombre
edad
Ademas se deberan agregar los comportamientos: 
    hablar(mensaje) - mensaje: el mensaje que dira la persona
    comer(alimento) - alimento: el alimento que consume la persona
'''

class Persona:
    def __init__(self):
        self._nombre = ''
        self._edad = None

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @nombre.deleter
    def nombre(self):
        del self._nombre


    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @edad.deleter
    def edad(self):
        del self._edad

    
    def hablar(self, mensaje):
        print(f'{self.nombre}: {mensaje}')

    def comer(self, alimento):
        print(f'{self.nombre} esta comiendo {alimento}.')

def main():
    persona1 = Persona()
    persona2 = Persona()

    persona1.nombre = 'Facundo Lezcano'
    persona1.edad = 22

    persona2.nombre = 'Nilo Lezcano'
    persona2.edad = 4

    print('Datos de la primer persona: ')
    print(f'nombre: {persona1.nombre}')
    print(f'edad: {persona1.edad}')
    print('Datos de la segunda persona: ')
    print(f'nombre: {persona2.nombre}')
    print(f'edad: {persona2.edad}')

    persona1.hablar(f'Hola {persona2.nombre} ¿como estas?')
    persona2.hablar(f'hola {persona1.nombre} bien ¿y vos?')
    persona1.comer('milanesa a la napolitana')
    persona2.comer('Comida de cordero')

if __name__ == '__main__':
    main()