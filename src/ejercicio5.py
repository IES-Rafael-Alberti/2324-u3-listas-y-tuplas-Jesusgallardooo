''' Escribir un programa que almacene en una lista los números del 1 al 10
    y los muestre por pantalla en orden inverso separados por comas. '''

def invertir_Orden(numeros):
    return list(reversed(numeros))  # Invierte la lista

if __name__ == "__main__":
    # Entrada
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Proceso
    numeros_invertidos = invertir_Orden(numeros)
    
    # Salida
    for numero in numeros_invertidos:
        print(numero, end= ", ")