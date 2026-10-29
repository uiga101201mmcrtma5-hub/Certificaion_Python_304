#REALIZAR UN PROGRAMA QUE CALCULE
#LA COMPRA TOTAL DE 4 PRODUCTOS,SI LA COMPRA TOTAL
#ES MAYOR  A 2000 PESOS ME HAGA UN DESCUENTP
#DEL 10%
#DATOS DE ENTRADA
precio1=float(input("Introduce el precio del producto 1:"))
precio2=float(input("Introduce el precio del producto 2:"))
precio3=float(input("Introduce el precio del producto 3:"))
precio4=float(input("Introduce el precio del producto 4:"))
#PROCESO
total=precio1+precio2+precio3+precio4
if total>2000:
    total=(total-(total*.10))
    #total=(3000-(3000*.10)) total=2700
    print(total)
else:
    print("NO TIENES DESCUENTO")
    print("tu total final es:",total)