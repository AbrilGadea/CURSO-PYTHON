#Creando diccionarios con dict()
diccionario = dict(nombre = "lucas", apellido = "dalto")


#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "rancio"]) : "Jajajaj"}
print(diccionario)

#Creando diccionarios con fromkeys() el primer dato es a lo que vcamos a iterar, el segundo a lo que vamos a igualar
diccionario = dict.fromkeys(["nombre", "apellido"])
print(diccionario)
