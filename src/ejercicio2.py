''' Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
    Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo
    estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.'''


def Yo_Estudio_X(asignaturas, Lista_Salida):
    for asignatura in asignaturas:
        mensaje = "Yo estudio " + asignatura
        Lista_Salida.append(mensaje)
    return mensaje

if __name__ == "__main__":
    #Entrada
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    Lista_Salida =  []


    #proceso
    Yo_Estudio_X(asignaturas, Lista_Salida)

    #Salida
    for mensaje in Lista_Salida:
        print(mensaje)