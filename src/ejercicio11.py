''' Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas
    y muestre por pantalla su producto escalar. '''

def calcular_Producto_Escalar(vector1, vector2):
    productoEscalar = 0
    for i in range (len(vector1)):
        productoEscalar = productoEscalar + vector1[i] * vector2[i]
    return productoEscalar

if __name__ == "__main__":
    #Entrada
    vector1 = [1, 2, 3] # [x, y, z]
    vector2 = [-1, 0, 2]

    ''' producto escalar = Vx * Ux + Vy * Uy + Vz * Uz'''

    #Proceso
    productoEscalar = calcular_Producto_Escalar(vector1, vector2)
    
    #Salida
    print("El producto escalar de tus vectores es --> " + str(productoEscalar))