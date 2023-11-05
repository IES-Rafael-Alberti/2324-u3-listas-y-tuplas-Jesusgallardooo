''' Escribir un programa que pregunte por una muestra de números, separados por comas, 
    los guarde en una lista y muestre por pantalla su media y desviación típica.'''

def calcular_media(numeros):
    suma = 0
    for numero in numeros:
        suma = suma + numero
    media = suma / len(numeros)
    return media

def calcular_desviación_típica(numeros, media):
    sumaCuadrados = 0
    for numero in numeros:
        sumaCuadrados = sumaCuadrados + (numero - media) ** 2
    varianza = sumaCuadrados / (len(numeros))
    desviaciónTípica = (varianza) ** 0.5
    return desviaciónTípica

if __name__ == "__main__":
    #Entrada
    numeros_str = input("Introduzca una lista de números separados por comas: ")
    numeros = [float(x) for x in numeros_str.split(',')]

    #proceso
    
    '''Calcular media = Suma / numero de datos introducidos'''
    media = calcular_media(numeros)

    '''Calcular desviación típica = varianza ** 0.5  '''
        #varianza = media de los numeros menos la media
        #Elevar a 1/2 (0.5) es lo mismo que hacer la raíz cuadrada
    desviaciónTípica = calcular_desviación_típica(numeros, media) 

    #Salida
    print("La media de los datos introducidos equivale a --> " + str(media))
    print("La desviación típica de los datos introducidos equivale a --> " + str(desviaciónTípica))