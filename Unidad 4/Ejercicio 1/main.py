from ABB import ABB

if __name__ == "__main__":
    ArbolBB = ABB()
    ArbolBB.insertar(ArbolBB.getRaiz(),70)
    raiz = ArbolBB.getRaiz() #Obtiene la raiz del arbol != None
    ArbolBB.insertar(raiz,10)
    ArbolBB.insertar(raiz,20)
    ArbolBB.insertar(raiz,40)
    ArbolBB.insertar(raiz,35)
    ArbolBB.insertar(raiz,100)
    ArbolBB.insertar(raiz,90)
    ArbolBB.insertar(raiz,110)
    ArbolBB.insertar(raiz,15)
    ArbolBB.insertar(raiz,82)
    #print("Recorrido InOrden")
    #ArbolBB.inOrden(raiz)
    print("PreOrden")
    ArbolBB.preOrden(raiz)
    ArbolBB.suprimir(raiz,70)
    print("Eliminao")
    ArbolBB.preOrden(raiz)
    #print("PostOrden")
    #ArbolBB.postOrden(raiz)
