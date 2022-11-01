import numpy as np

class ColadePrioridad:
    __prioridades: np.array
    __cantidad: int
    
    def __init__(self,dimension):
        self.__prioridades = np.full(dimension,None)
        self.__cantidad = 0
        self.__prioridades[0] = -1
    
    def __iter__(self):
        return iter(self.__array)

    def vacio(self):
        return self.__cantidad == 0
    
    def lleno(self):
        return self.__cantidad == len(self.__prioridades)
    
    def padre(self,posicion):
        return posicion // 2
    
    def hijo_izquierdo(self,posicion):
        return posicion * 2
    
    def hijo_derecho(self,posicion):
        return (posicion*2) + 1
    
    def esHoja(self,posicion):
        return posicion > self.__cantidad
    
    def intercambiar(self,pos1,pos2):
        self.__prioridades[pos1],self.__prioridades[pos2] = self.__prioridades[pos2],self.__prioridades[pos1]
    
    def insertar(self, element):
        if self.lleno():
            return print("No hay espacio en la cola")
        else:
            #Propiedad de estructura
            self.__cantidad += 1
            actual = self.__cantidad
            Padre = self.padre(actual)
            self.__prioridades[actual] = element
            #Propiedad de orden
            while self.__prioridades[actual] < self.__prioridades[Padre]:
                self.intercambiar(actual, Padre)
                actual = Padre
                Padre = self.padre(actual)
    
    def minimo_a_eliminar(self,pos):
        Padre = pos
        Hizq = self.hijo_izquierdo(pos)
        Hder = self.hijo_derecho(pos) 
        #Mientras no sea hoja y el padre sea mayor que alguno de sus hijos
        while  not self.esHoja(Hder) and (self.__prioridades[Padre] > self.__prioridades[Hizq] or self.__prioridades[Hder]):
            if self.__prioridades[Hizq] <= self.__prioridades[Hder]: #Compara los hijos para ver cual es el menor
                self.intercambiar(Padre,Hizq)
                Padre = Hizq
            else:
                self.intercambiar(Padre,Hder)
                Padre = Hder
            #Actualiza los hijos
            Hizq = self.hijo_izquierdo(Padre) 
            Hder = self.hijo_derecho(Padre)
    
    def eliminar(self):
        #Propiedad de estructura
        eliminado = self.__prioridades[1]
        self.__prioridades[1] = self.__prioridades[self.__cantidad]
        self.__prioridades[self.__cantidad] = None
        self.__cantidad -= 1
        #Propiedad de orden
        self.minimo_a_eliminar(1)
        return eliminado
    
    def mostrar(self):
        for i in range(1,(self.__cantidad // 2+1)):
            print(" PADRE : "+ str(self.__prioridades[i])+" HIJO IZQUIERDO : "+ 
                                str(self.__prioridades[2 * i])+" HIJO DERECHO: "+
                                str(self.__prioridades[(2 * i) + 1]))
