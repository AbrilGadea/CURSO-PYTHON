frase = input("Decime una frase y te calculo cuanto tardarías si tuvieras que decirlo: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarías {cantidad_de_palabras / 2} en decirlo')
print(f'Dalto lo diría en {cantidad_de_palabras*100 //2 *1.3 /100} segundos')
if cantidad_de_palabras > 120:
 print("Para flaco, tampoco te pedí un testamento")