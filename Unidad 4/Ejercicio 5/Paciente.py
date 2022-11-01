class Paciente:
    __nombre = ""
    __prioridad = 0

    def __init__(self,prioridad,nombre):
        self.__nombre = nombre
        self.__prioridad = prioridad
    
    def getNombre(self):
        return self.__nombre
    
    def getPrioridad(self):
        return self.__prioridad
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def setPrioridad(self,prioridad):
        self.__prioridad = prioridad
