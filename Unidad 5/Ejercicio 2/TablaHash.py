import numpy as np

import random

# Política manejo de colisiones: Direccionamiento abierto

# Función de transformación de claves: Método de la división

# Procesamiento de claves sinónimas: Secuencia de prueba Pseudo Random

class TablaHash:
    __dimension: int
    __Tabla: np.array
    __numAleatorio: int
    
    def __init__(self,dimension,usarPrimo=False):
        self.__dimension = int(dimension/0.7)
        if usarPrimo:
            self.__dimension = self.__getPrimo(self.__dimension) #0.7 factor de carga

        self.__numAleatorio = random.randint(1,self.__dimension)
        self.__Tabla = np.full(self.__dimension,None)
    
    def insertar(self,clave):
        index = self.__PruebaPseudoRandom(clave)
        
        if index != -1:
            self.__Tabla[index] = clave
        else:
            #Peor caso: recorrer todo el arreglo y no encontrar posición disponible
            print("Tabla llena, no es posible almacenar la clave")
    
    def buscar(self,clave):
        index = self.__PruebaPseudoRandom(clave)
        if index != -1:
            return self.__Tabla[index]
        else:
            return None
    
    def longSecuencia_Busqueda(self,clave):
        index = self.__hash(clave)
        contador = 0
        
        while self.__Tabla[index] != None and self.__Tabla[index] != clave:
            index = (index + 1) % self.__dimension
            contador += 1
        
        return contador
    
    def calcularFactorCarga(self):
        print(self.__dimension)
        total = np.count_nonzero(self.__Tabla != None) #Cuenta el número de elementos no nulos
        return (total / self.__dimension)
    
    #Metodos Auxiliares---------------------------------------------------------
    # FUNCIÓN DE TRANSFORMACIÓN H(K)
    def __hash(self,clave): #Método de la división (módulo) h(k) = k % m
        return clave % self.__dimension
    
    
    # POLÍTICA DE MANEJO DE COLISIONES
    def __PruebaPseudoRandom(self,clave): #Secuencia de prueba pseudoRandom - Retorna la posición donde se debe almacenar la clave
        IndexOrigen = index = self.__hash(clave)
        
        while self.__Tabla[index] != None and self.__Tabla[index] != clave:
            index = (index + self.__numAleatorio) % self.__dimension
            
            if index == IndexOrigen:
                return -1 #Tabla llena
        
        return index
    
    def __getPrimo(self,numero):
        for i in range(2,numero):
            if numero % i == 0:
                return self.__getPrimo(numero+1)
        return numero
