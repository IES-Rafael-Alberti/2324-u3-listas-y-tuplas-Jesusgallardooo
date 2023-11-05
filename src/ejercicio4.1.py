''' Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
    los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. '''

if __name__ == "__main__":
    #Entrada
    numeroGanador = []
    numeros = 6 

    for i in range(numeros):
        numeroAnumero = int(input("Introduzca el numero ganador " + str(i + 1) + ": "))
        numeroGanador.append(numeroAnumero)

    #proceso
    numeroGanador.sort()

    #Salida
    print("\n\n El numero ganador, mostrado de menor a mayor es: \n")

    for numero in numeroGanador:
        print(numero)