from Nodo import Nodo

class ListaSimpleEnlazada:
    def __init__(self):
        self.primero = None
        self.longitud = 0
    
    def insertar_dato(self,dato):
        nuevo_nodo = Nodo()
        #El primer nod esta vació, va entrar a esta conedición en la primera iteración
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo