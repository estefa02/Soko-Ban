class Cola:
    '''Representa a una cola, con operaciones de encolar y 
       desencolar. El primero en ser encolado es también el primero
       en ser desencolado.'''

    def __init__(self):
        '''Crea una cola vacía'''
        self.frente = None
        self.ultimo = None

    def encolar(self, dato):
        '''Agrega el elemento x como último de la cola.'''
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self.frente = nodo
        else:
            self.ultimo.prox = nodo
        self.ultimo = nodo

    def desencolar(self):
        '''Desencola el primer elemento y devuelve su valor
           Pre: la cola NO está vacía.
           Pos: el nuevo frente es el que estaba siguiente al frente anterior'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        dato = self.frente.dato
        self.frente = self.frente.prox
        if self.frente is None:
            self.ultimo = None
        return dato

    def ver_frente(self):
        '''Devuelve el elemento que está en el frente de la cola.
           Pre: la cola NO está vacía.'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        return self.frente.dato

    def esta_vacia(self):
        '''Devuelve True o False según si la cola está vacía o no'''
        return self.frente is None
    
    def _str_(self):
        aux = Cola()
        cadena = ''
        while not self.esta_vacia():
            dato = self.desencolar()
            if len(cadena) == 0:
                cadena += str(dato)
            else:
                cadena += ' <-- ' + str(dato) 
            aux.encolar(dato)
        while not aux.esta_vacia():
            a = aux.desencolar()
            self.encolar(a)
        return cadena

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
        
def invertir_cola(cola):
    if cola.esta_vacia():
        return cola
    elemento = cola.desencolar()
    fun = invertir_cola(cola)
    cola.encolar(elemento)
    return fun
        
cola1 = Cola()
cola2 = Cola()
cola3 = Cola()
cola4 = Cola()
cola1.encolar(1)
cola1.encolar(2)
cola1.encolar(3)
cola2.encolar(4)
cola2.encolar(5)
cola2.encolar(6)
cola4.encolar(7)
cola4.encolar(8)
colas = [cola1, cola2, cola3, cola4]


    
            
        
