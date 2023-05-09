numeros =[4,7,42,15]

#Encontrando el número mayor de una lista (aplicable también a tuplas y conjuntos)
numero_mas_alto = max(numeros)

#Encontrando el número menor de una lista (aplicable también a tuplas y conjuntos)
numero_mas_bajo = min(numeros)

#Redondeando a 6 decimales
numero = round(12.565888, 2)
print(numero)

#Retorna False -> 0, vacío, False o ninguno
resultado_bool = bool(2)

#Retorna true si todos los valores son verdaderos
resultado_all = all([10, "true", [1,2,3]])

#Suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)