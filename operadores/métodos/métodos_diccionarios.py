diccionario = {
    "nombre" : "lucas",
    "apellido" : "dalto",
    "suscriptores" : 100000,
}
#devuelve claves y sirve para iterar
claves = diccionario.keys()
print(claves)
# obteniendo datos con get, si no encuentra no lanza error sino que continúa
claves = diccionario.get("nombre")
print(claves)

#eliminando todo el diccionario
#diccionario.clear()
#eliminando un elemento del diccionario
#diccionario.pop("nombre")
print(diccionario)

#obeteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)