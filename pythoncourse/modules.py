#modulos = codigo ya escrito y mejorado que esta en internet. No es necesario que vos crees todo ya que en internet podes encontrar m uchas cosas como los modulos
#hay tres tipos de modulos:
    #modulos que vos podes crear
    #modulos que podes descargar de internet
    #modulos de las bibliotecas de python

#--para traer un modulo que ya se encuentra en python escribimos la plabra "import" y luego el nombre del modulo
#ej import datetime
#o tambien: from datetime import timedelta, tengo acceso al metodo timedelta sin necesidad de esoecificar que viene de datetime

#import datetime
#print(datetime.date.today())
#print(datetime.timedelta(minutes = 100))

'''
#--para crear nuestro propio modulo hacemos
#supongamos que lo cree en un file que se llama "math"
def add(n1,n2):
    print(n1+n2)

def substract(n1,n2):
    print(n1-n2)

#si quiero llamar este modulo de otra parte de mi app lo que hago es "import + nombre del file donde lo creer" de la siguiente manera
#import math
#para usarlo seria
#math.add(3,6)
'''

#--la otra forma es descargar un modulo desde internet a travez de la consola, y asi se asignaria a python un nuevo modulo
#para usarlo igualmente tenemos que hacer from (nombre del modulo) import (las funcionalidades que necesites)
#o "import (nombre de modulo)"
 
