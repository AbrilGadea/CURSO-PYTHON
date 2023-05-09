animales = ["gato", "perro", "loro", "cocodrilo"]
for animal in animales :
    #Recorriendo la lista animales
    print( f'ahora la variable animal es igual a: {animal}')
   
   #Recorriendo lista números y multiplicando cada valor por 10
numeros =  [1, 2, 3, 4]
for numero in numeros :
    resultado = numero *10
    print(resultado)
    
    #Iterando dos listas del mismo tamaño al mismo tiempo
    for animal, numero in zip (animales, numeros) :
        print(f'Recorriendo lista 1 {animal}')
        print(f'Recorriendo lista 2 {numero}')
        
    for num in range (5,10) :
        print (num)
        
        #Forma correcta de recorrer una lista con su índice
for num in enumerate (numeros) : 
    indice = num [0]
    valor = num [1]
    print(f'el índice es: {indice} y el valor es: {valor}')
    
    #usando el else
    for numero in numeros :
        print(f' ejecutando el ultimo bucle, valor actual: {numero}')
    else:
        print('el bucle terminó')
        
        #Todo lo anterior funciona igual para tuplas y conjuntos