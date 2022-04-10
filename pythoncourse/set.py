#es una coleccion desordenada sin indice
from turtle import color


colors = {"red", "green", "blue"}

print(type(colors))

print("red" in colors)

#agregar un elemento, pero como no tenemos indice lo va a agregar al comienzo
colors.add("violet")

#eliminar elemento
colors.remove("red")

#elimina los elementos
colors.clear()
#o como si fuera una tuple
del colors 