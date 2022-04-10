'''
modulo de conversiones de unidades de tiempo

-segundos a minutos: recibe segundos y devuelve minutos y segundos
-segundos a horas: recibe algunos segundos y regresa horass, minutos y segundos
-minutos a segundos: recibe minutos y segundos y regresa segundos
-minutos a horas: recibe minutos y segundos y regresa horas y segunndos
'''
SEGUNDOS_POR_MINUTO = 60
MINUTOS_POR_HORA = 60

def segundosAMinutos(segundos):
    '''
    Funcion que convierte segundos a minutos. 

    Argumentos: segundos -- la cantidad de segundos a convertir
    '''
    mins = segundos // SEGUNDOS_POR_MINUTO
    segs = segundos % SEGUNDOS_POR_MINUTO

    return mins, segs

def minutosASegundos(minutos,segundos):
    segs = minutos * SEGUNDOS_POR_MINUTO + segundos

    return segs

def minutosAHoras(minutos,segundos):
        '''
        Funcion que convierte minutos y segundos a horas minutos y segundos. 

        Argumentos:
        minutos -- cantidad de minutos a convertir 
        segundos -- la cantidad de segundos a convertir

        retorno:
        cantidad de horas minutos y segundos equivalentes
        '''
        hrs = minutos // MINUTOS_POR_HORA
        mins = minutos % MINUTOS_POR_HORA
        segs = segundos

        return hrs, mins, segs


def segundosAHoras(segundos):
    mins, segs = segundosAMinutos(segundos)
    hrs, mins, segs = minutosAHoras(mins, segs)

    return hrs, mins, segs