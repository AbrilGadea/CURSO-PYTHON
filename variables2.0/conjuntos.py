#Creando un conjunto con set()
conjunto = set(["dato1", "dato2"])
print(conjunto)

#metiendo un conjunto dentro de otro conjunto
conjunto1= frozenset(["dato1", "dato2"])
conjunto2 = {"conjunto1", "dato" }
print(conjunto2)


#Teoría de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

#Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
#resultado = conjunto2 <= conjunto1

#Verificando si es un superconjunto
#resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#Verificar si hay algún número en común, si hay algún número que de igual, va a dar falso; si son todos distintos, true
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)



