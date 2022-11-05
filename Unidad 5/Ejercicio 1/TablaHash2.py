import numpy as np
import random

# Política manejo de colisiones: Direccionamiento abierto

# Función de transformación de claves: Método de la división

# Procesamiento de claves sinónimas: Secuencia de prueba lineal

class TablaHash:
    __dimension: int
    __Tabla: np.array
    
    def __init__(self,dimension,usarPrimo=False):
        if usarPrimo:
            self.__dimension = self.__getPrimo(int(dimension/0.7)) #0.7 factor de carga
        else:
            self.__dimension = dimension
        self.__Tabla = np.full(self.__dimension,None)
    
    def insertar(self,clave):
        index = self.__PruebaLineal(clave)
        
        if index != -1:
            self.__Tabla[index] = clave
        else:
            #Peor caso: recorrer todo el arreglo y no encontrar posición disponible
            print("Tabla llena, no es posible almacenar la clave")
    
    def buscar(self,clave):
        index = self.__PruebaLineal(clave)
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
        total = np.count_nonzero(self.__Tabla != None) #Cuenta el número de elementos no nulos
        return (total / self.__dimension)
    
    #Metodos Auxiliares---------------------------------------------------------
    # FUNCIÓN DE TRANSFORMACIÓN H(K)
    def __hash(self,clave): #Método de la división (módulo) h(k) = k % m
        return clave % self.__dimension
    
    
    # POLÍTICA DE MANEJO DE COLISIONES
    def __PruebaLineal(self,clave): #Secuencia de prueba lineal - Retorna la posición donde se debe almacenar la clave
        IndexOrigen = index = self.__hash(clave)
        
        while self.__Tabla[index] != None and self.__Tabla[index] != clave:
            index = (index + 1) % self.__dimension
            
            if index == IndexOrigen:
                return -1 #Tabla llena
        
        return index
    
    
    def __getPrimo(self,numero):
        for i in range(2,numero):
            if numero % i == 0:
                return self.__getPrimo(numero+1)
        return numero
    
if __name__ == "__main__":
    Tabla1 = TablaHash(100)
    Tabla2 = TablaHash(100,True)
    
    for i in range(100):
        Tabla1.insertar(random.randint(0,1000))
        Tabla2.insertar(random.randint(0,1000))
    
    print("Tabla 1 (sin usar numero primo)")
    print("Longitud de la secuencia de búsqueda: ",Tabla1.longSecuencia_Busqueda(100))
    print("Factor de carga: {:.2f} %".format(Tabla1.calcularFactorCarga()*100))
    
    print("\nTabla 2 (usando numero primo)")
    print("Longitud de la secuencia de búsqueda: ",Tabla2.longSecuencia_Busqueda(100))
    print("Factor de carga: {:.2f} %".format(Tabla2.calcularFactorCarga()*100))