cadena1='Hola'
cadena2='Mundo'
multilinea="""Esto es una cadena 
de varias lineas"""
print(cadena1+cadena2+multilinea)#print(f"{cadena1})
#cadenas y repeticion
eco='ja'*3
print(eco)
#cambiar una cadena de miniscula a mayuscula
tu_nombre='america'
print(tu_nombre.upper())
##cambiar una cadena de mayuscula a minuscula
print(tu_nombre.lower())
#remplazar texto en una cadena 
frase='me gusta la programacion'
print(frase.replace('orientacion','recreo'))
#formato de cadenas (F-string)
edad=15
nombre='america'
mensaje=f'Hola,me llamo {nombre} \ny tengo {edad} años'
print(mensaje)
#contar caracteres de una cadena
texto= '¡¡¡¡¡¡¡¡Felicidades por continuar en el CECY!!!!!!!,la peor prepa;(' 
cantidad_caracteres=len(texto)
print(texto,cantidad_caracteres)
#comprobar si un texto contiene una palabra
oracion='aprender python no es divertido'
if 'java' in oracion:
    print('encontrado')
else:
    print('no esta')
#validar contenido de una cadena
numerolista='america'
print(numerolista.isalpha())
print(numerolista.isdigit())