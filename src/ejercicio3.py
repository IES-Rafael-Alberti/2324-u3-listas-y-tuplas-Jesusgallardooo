''' Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
    Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
    en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has
    sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada 
    una de las correspondientes notas introducidas por el usuario.'''


if __name__ == "__main__":
    #Entrada
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    calificaciones = []
    for asignatura in asignaturas:
        nota = int(input("Introduzca su calificación obtenida en " + asignatura + " : "))
        calificaciones.append(nota)

    #Salida
    for i in range(len(asignaturas)):
        asignatura = asignaturas[i]
        nota = calificaciones[i]
        print( "- " + asignatura + " --> " + str(nota) ) 
