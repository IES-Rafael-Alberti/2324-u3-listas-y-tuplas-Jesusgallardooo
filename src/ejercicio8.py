''' Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.'''


def palíndromo_o_no(palabra):
    if palabra == palabra[::-1]:
        determinar = True
    else:
        determinar = False
    return determinar

if __name__ == "__main__":
    #Entrada
    palabra = list(input("Introduzca una palabra cualquiera: "))

    #proceso
    determinar = palíndromo_o_no(palabra)

    #salida
    if determinar == True:
        for letra in palabra:
            print("" + letra, end="")
        print(" es un palíndromo. ")
    else:
        for letra in palabra:
            print("" + letra, end="")
        print(" no es un palíndromo. ")