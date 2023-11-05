''' Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
    Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
    en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa
    debe mostrar por pantalla las asignaturas que el usuario tiene que repetir. '''

def detectar_suspensos(asignaturasSuspensas, asignatura, nota):
    if nota < 5:
        asignaturasSuspensas.append(asignatura)
    return asignatura

if __name__ == "__main__":
    #Entrada
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    asignaturasSuspensas = []
    for asignatura in asignaturas:
        nota = int(input("Introduzca su calificación obtenida en " + asignatura + " : "))
        
    #Proceso    
        detectar_suspensos(asignaturasSuspensas, asignatura, nota)

    #Salida
    if len(asignaturasSuspensas) > 0:
        print("\n Debes repetir: ")
        for asignatura in asignaturasSuspensas:
            print("  - " + asignatura)
    else:
        print("\n Enhorabuena, has pasado limpio.")