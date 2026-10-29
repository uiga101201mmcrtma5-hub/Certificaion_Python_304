#ejemplo 1 sin manejo de excepciones
numero1=float(input("Ingresa el primer numero:"))
numero2=float(input("Ingresa el segundo numero:"))
resultado=numero1/numero2
try:
    numero1=0
    numero2=67
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("Error:No se puede dividir un numero entre 0")
    try:
except ValueError:
    print("Error:solo se pueden resibir numeros")
 