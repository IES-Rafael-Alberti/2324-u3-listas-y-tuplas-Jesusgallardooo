''' Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8
    y muestre por pantalla el menor y el mayor de los precios. '''

def ordenar_precios(precios):
    precios.sort()
    return precios

if __name__ == "__main__":
    #Entrada
    precios = [50, 75, 46, 22, 80, 65, 8]

    #Proceso
    ''' ordeno y selecciono la posicion inicial(precio menor) y la posición final(precio mayor). '''
    ordenar_precios(precios) 
    precioMenor = precios[0]
    precioMayor = precios[len(precios)-1]

    #Salida
    print("\nPrecio menor --> " + str(precioMenor))
    print("\nPrecio mayor --> " + str(precioMayor) +"\n")