import numpy as np


class TablaHash():
    __tabla:np.array
    __dimension:int

    def __primo(self,numero):
        for i in range(2,numero):
            if numero % i == 0:
                return self.__primo(numero+1)
        return numero

    def __init__(self,dimension,UsarPrimo=False) -> None:
        if UsarPrimo:
            self.__dimension = self.__primo(int(dimension/0.7))
        else:
            self.__dimension = dimension
    
        self.__tabla = np.full(self.__dimension,None)
    
    def insertar(self,clave):
        indexO = indice = self.hash(clave)
        if self.__tabla[indice] == None:
            self.__tabla[indice] = clave
        else:
            while self.__tabla[indice] != None:
                indice = (indice + 1) % self.__dimension
                if indexO == indice:
                    return -1
            self.__tabla[indice] = clave

    def hash(self,clave):
        return clave % self.__dimension

    def LongSecuenciaBuscar(self,clave):
        contador = 1
        indice = self.hash(clave)
        if self.__tabla[indice] == clave:
            return contador
        else:
            self.__tabla[indice] == None
            while self.__tabla[indice] != clave and contador < self.__dimension:
                indice = (indice + 1) % self.__dimension
                contador += 1
            if contador >= self.__dimension:
                return -1
            else: 
                return contador

    def Motrar(self):
        print(self.__tabla)
