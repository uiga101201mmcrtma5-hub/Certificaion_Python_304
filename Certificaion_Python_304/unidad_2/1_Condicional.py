promedio=float(input("Ingresa tu promedio:"))
#El numero ingresado es 6
if promedio<0:
    print("Tu promedio no es valido")
elif promedio<=5:
    print("Tu promedio es muy bajo")
elif promedio>5 and promedio<=6:
    print("Tu promedio es muy bajo")
elif promedio>7 and promedio<=9:
    print("Tu promedio es muy bueno")
elif promedio>9 and promedio<=10:
    print("Tu promedio es perfecto")
else:
    print("Ese promedio no existe")