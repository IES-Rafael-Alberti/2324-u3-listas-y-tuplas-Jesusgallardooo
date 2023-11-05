''' Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
    los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. '''

def ordenar_Numero_Ganador(numeroGanador):
    ordenado = False 
    while ordenado == False: 
        ordenado = True 
        for i in range(len(numeroGanador)-1): 
            if numeroGanador[i] > numeroGanador[i+1]: 
                numero = numeroGanador[i] 
                numeroGanador[i] = numeroGanador[i+1] 
                numeroGanador[i+1] = numero 
                ordenado = False
    return numeroGanador

if __name__ == "__main__":
    #Entrada
    numeroGanador = []
    numeros = 6 

    for i in range(numeros):
        numeroAnumero = int(input("Introduzca el numero ganador " + str(i + 1) + ": "))
        numeroGanador.append(numeroAnumero)

    #proceso (variante con el algoritmo burbuja de la tarea anterior)
    ordenar_Numero_Ganador(numeroGanador)

    #Salida
    print("\n\n El numero ganador, mostrado de menor a mayor es: \n")

    for numero in numeroGanador:
        print(numero)