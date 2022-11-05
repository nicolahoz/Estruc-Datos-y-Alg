import random   
from TablaHash import TablaHash

if __name__ == "__main__":
    Tabla1 = TablaHash(1000)
    Tabla2 = TablaHash(1000,True)
    
    for i in range(1000):
        Tabla1.insertar(random.randint(0,10000))
        Tabla2.insertar(random.randint(0,10000))
    
    print("Tabla 1 (sin usar numero primo)")
    print("Longitud de la secuencia de búsqueda: ",Tabla1.longSecuencia_Busqueda(900))
    print("Factor de carga: {:.2f} %".format(Tabla1.calcularFactorCarga()*100))
    
    print("\nTabla 2 (usando numero primo)")
    print("Longitud de la secuencia de búsqueda: ",Tabla2.longSecuencia_Busqueda(900))
    print("Factor de carga: {:.2f} %".format(Tabla2.calcularFactorCarga()*100))