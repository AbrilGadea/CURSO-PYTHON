cadena1 = "Hola soy princesa"
cadena2 = "Bienvenida princesa"

#DIR (función de python)
print (dir (cadena1)) #Nos decuelve todo lo que podemos hacer con ese dato

#UPPER (método convierte a mayúscula )
mayusc = cadena1.upper()
print(mayusc)

#convierte en minúsculas
minus = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("D")

#buscamos cadenas en otras cadenas, si no hay coinidencias lanza una excepcion
busqueda_index = cadena1.index("a")

#si es numerico devolveos true, sino false
es_numerico = cadena1.isnumeric()


