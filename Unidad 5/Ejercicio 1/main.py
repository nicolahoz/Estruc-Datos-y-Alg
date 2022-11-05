from TablaHash import TablaHash
from random import randint


if __name__ == "__main__":
    # Crear tabla hash
    tabla1 = TablaHash(1000,True)
    tabla2 = TablaHash(1000,False)
    # Llenar tabla con 1000 claves aleatorias
    for i in range(1000):
        tabla1.insertar(randint(0, 1000))    
    tabla1.Motrar()
    for i in range(1000):
        tabla2.insertar(randint(0, 1000))    
    tabla2.Motrar()

    print("Longitud de secuencia de Busqueda Tabla Primo:",tabla1.LongSecuenciaBuscar(5))
    print("Longitud de secuencia de Busqueda Tabla No Primo:",tabla2.LongSecuenciaBuscar(10))