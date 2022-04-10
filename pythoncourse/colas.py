#es una estructura de datos, coleccion de objetos, el criterio mediante el cual se organizan los datos es de tipo FIFO first in first out
#como ir a pagar un servicio y que haya cola, el primero en llegar paga primero y el ultiumo en llegar paga ultimo
#para trabajar con las colas se debe traer el modulo "queue"
import queue

cola = queue.Queue()

cola.put(5) #agregar elemento a la cola
cola.put([2,4,6])

cola.get() #regresa el primer elemento en ser igresado, osea el 5
cola.get()#regresa el otro elemento ingresado, osea la lista [2,4,6]

#existe otro tipo de cola, que se maneja a traves de la prioridad de los elementos, sigue siendo igual, el elemneto primero en entrar es el primero en salir pero al momento de trabajar esa estructura se vanm a ordenar con prioridad, en el caso de python los organiza el de menor valor alfrente

cp = queue.PriorityQueue()
cp.put(5)
cp.put(3)
cp.put(4)
cp.get()#devuelve el 3
cp.get()#devuelve el 4
cp.get()#devuelve el 5
#hicimos una agenda con cola de prioridad
