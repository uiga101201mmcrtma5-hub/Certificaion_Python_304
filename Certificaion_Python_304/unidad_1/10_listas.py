#Declarando una 
try:
    materias=["Programacion","Filosofia","Matematicas","Ingles"]
    materias.append("Lengua y comunicacion")
    print(materias)
    materias[1]="Biologia"
    print(materias)
    materias.remove("Programacion")
    print(materias)
except IndexError:
    print("Ese indice no lleva materia")