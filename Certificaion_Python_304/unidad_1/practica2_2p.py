try:
    alumnos=["Carlos 67","Kimberly","Brian","Leonel","Sdana"]
    calificaciones=[6,7,8,9,5]
    print("alumno:", alumnos[2],"calificacion",calificaciones[2])
    print("alumno:", alumnos[4],"calificacion",calificaciones[4])
except IndexError:
    print("No se encontro el alumno o texto")
