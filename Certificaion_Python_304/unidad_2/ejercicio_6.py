tabla = [
    ["Nombre","Edad","Calificaciom"],
    ["america",15,6.0],
    ["emy",16,7.0],
    ["carlos",16,8.0],
    ["luis",16,9.0],
    ["casillas",16,10.0],
    ["sdana",16,1.0],
    ["brian",16,2.0],
    ["kim",15,3.0],
    ["leo",15,4.0]
]
nombre=input("ingresa tu nombre:")
filas=len(tabla)
columnas=len(tabla[0])
for i in range(filas):
    for j in range(columnas):
        if tabla[i][j] == nombre:
            print(f"Nombre encontrado en la posicion [{i}][{j}]")


