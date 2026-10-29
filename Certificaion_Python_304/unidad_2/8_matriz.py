numeros=[   
    [1,2,3],
    [2,3,4],
    [5,6,7]
]
#obteniendo numero de filas 
filas=len(numeros)#filas=3
#Obteniendo el numero de columnas
columnas=len(numeros[0])
#ciclo externo para los indices de las filas(i)
for i in range(filas):
    #ciclo interno para los indices de las columnas (j)
    for j in range(columnas):
        print(f"[{i}] [{j}] = {numeros[i][j]}")