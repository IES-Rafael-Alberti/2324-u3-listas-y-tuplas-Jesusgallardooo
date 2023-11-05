''' Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
    letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.'''


def eliminar_posiciones_multiplos_de_tres(abecedario):
    for i in range(len(abecedario), 1, -1):
        if i % 3 == 0:
            abecedario.pop(i-1)
    return abecedario

if __name__ == "__main__":
    #Entrada
    abecedario = list("abcdefghijklnmñopqrstuvwxyz")

    #proceso
    eliminar_posiciones_multiplos_de_tres(abecedario)
    
    #salida
    for letra in abecedario:
        print(letra, end= ", ")