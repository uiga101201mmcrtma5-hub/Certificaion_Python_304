#creando un diccionario
persona={
    "Nombre":"mery",
    "Edad":15,
    "Profesion":"Estudiante",
    "Estudiante":True 
}
print(persona)
#accediendo a un valor especifico 
print(persona["Nombre"])
#Se puede usar el metodo get(),es util porque no marca error si el valor no exista
print(persona.get("Profesion"))
#Modficar un valor existente 
persona["Edad"]=43
print(persona["Edad"])
#Agregar un par(clave:valor)
persona["Ciudad"]="San Pepe ranch"
print(persona)
#Recorrer un diccionario con un bucle
