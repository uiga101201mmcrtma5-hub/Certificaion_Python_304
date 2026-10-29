abecedario=[
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"],
    ["j","k","l"],
    ["m","n","ñ"],
    ["o","p","q"],
    ["r","s","t"],
    ["u","v","w"],
    ["x","y","z"]
]
filas=9
columnas=3
for i in range (filas):
    for j in range (columnas):
        print(f"[{i}] [{j}] = {abecedario[i][j]}")