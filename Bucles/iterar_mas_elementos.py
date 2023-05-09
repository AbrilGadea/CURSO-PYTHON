frutas = ["banana", "durazno", "manzana", "granada"]
cadena = 'hola dalto'
numeros = [2, 5, 8, 10]

    #Evitando que se coma una granada con la sentencia continue
for fruta in frutas :
    if fruta == "granada" :
        continue
    print(f'Me voy a comer una: {fruta}')
    
    #Evitando que el bucle siga ejecutandose  (el else tampoco se ejecuta)
    for fruta in frutas :
            print(f'Me voy a comer una: {fruta}')
            if fruta == "manzana" :
                break
    
    #Recorrer una cadena de texto
    for letra in cadena : 
        print (letra)
        
    #For en una sola línea de códigos (duplicamos los números)
    numeros_duplicados = [x *2 for x in numeros]
    print(numeros_duplicados)