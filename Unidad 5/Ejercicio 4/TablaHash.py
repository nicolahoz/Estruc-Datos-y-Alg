# Política manejo de colisiones: Buckets

# Función de transformación de claves: Método de extracción
import numpy as np

class Buckets:
    __array: np.array
    __contador: int
    
    def __init__(self,tamBuckets):
        self.__array = np.full(tamBuckets,None)
        self.__contador = 0
    
    def insertar(self,valor):
        if self.__array[-1] is not None:
            print("No se puede insertar, el bucket está lleno")
        else:
            self.__array[self.__contador] = valor
            self.__contador += 1
    
    def getElem(self,pos):
        return self.__array[pos]
    
    def getTam(self):
        return self.__contador


class TablaHash:
    __dimension: int
    __Tabla: np.array
    __dimensionOverflow: int
    __longExtraccion: int
    
    
    def __init__(self,ct_claves,ct_buckets,usarPrimo = False):
        self.__dimension = int(ct_claves / 0.7 + 1)
        
        if usarPrimo:
            self.__dimension = self.__getPrimo(self.__dimension)
        
        self.__longExtraccion = len(str(self.__dimension)) #Cantidad de digitos a extraer = cant dígitos de M
        self.__dimensionOverflow = int(self.__dimension * 1.2)
        self.__Tabla = np.empty(self.__dimensionOverflow,dtype=Buckets)
        for i in range(self.__dimensionOverflow): #Inicializar buckets
            self.__Tabla[i] = Buckets(ct_buckets)
    
    def insertar(self,valor):
        #Método de extracción
        index = self.__metodoExtraccion(valor)
        #Insertar en el bucket
        self.__Tabla[index].insertar(valor)
    
    def buscar(self,valor):
        index = self.__metodoExtraccion(valor)
        i = 0
        valor_return = None
        #Zona no overflow
        while i < self.__Tabla[index].getTam() and valor_return == None:
            if self.__Tabla[index].getElem(i) == valor:
                valor_return = valor
            else:
                i += 1
        #Zona overflow
        if i == self.__Tabla[index].getTam():
            i = self.__dimension
            j = 0
            while i < self.__dimensionOverflow and valor_return == None:
                if self.__Tabla[i].getElem(j) == valor :
                    valor_return = valor
                else:
                    j += 1
                    if j == self.__Tabla[i].getTam():
                        j = 0
                        i += 1
        return valor_return

    #Metodos PRIVADOS---------------------------------------------------------
    # FUNCIÓN DE TRANSFORMACIÓN H(K)
    def __metododeDivison(self,valor): #Método de la división (módulo) h(k) = k % m
        return valor % self.__dimension
    
    def __metodoExtraccion(self,valor):
        clave = str(valor)
        #Indexación negativa (para extraer los últimos digitos)
        index = int(clave[-self.__longExtraccion:])
        #En caso de que la posición quede fuera del rango de 0 a M-1
        if index >= self.__dimension:
            index = self.__metododeDivison(index)
        return index
    
    def __getPrimo(self,numero):
        for i in range(2,numero):
            if numero % i == 0:
                return self.__getPrimo(numero+1)
        return numero

    def Mostrar(self):
        for i in range(self.__dimensionOverflow):
            print("Bucket ",i,": ",end="")
            for j in range(self.__Tabla[i].getTam()):
                print(self.__Tabla[i].getElem(j),end=" ")
            print()