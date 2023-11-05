''' Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de
    veces que contiene cada vocal. '''

def contar_Vocal(palabra, vocal):
    contador = 0
    for i in palabra:
        if vocal == i:
            contador = contador + 1
    return contador

if __name__ == "__main__":
    #Entrada
    palabra = input("Introduzca una palabra cualquiera: ")
    vocal = input("Introduzca la vocal que quiera contar en su palabra: ")

    #Proceso
    contador = contar_Vocal(palabra, vocal)

    #salida
    print( "la vocal " + vocal + " aparece " + str(contador) + " veces. ")