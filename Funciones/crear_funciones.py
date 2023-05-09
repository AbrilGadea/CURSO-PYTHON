#Creando una fcunción simple
#def saludar():
    #print('Hola Abril bonita')
    #Ejecutando la función simple
#saludar() 
#saludar()   
#saludar()   
#saludar()  

#Crear una función que tenga parámetros
def saludar(nombre, sexo):
    sexo = sexo.lower() #para que al print se lo pueda escribir con mayúsculas o minúsculas
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "titán"
        
    else:
        adjetivo = "crack"
    
    #print(f'Hola {nombre} mi {adjetivo}, ¿Cómo andas?')
    
#saludar("Abril", "mujer")   
 
 #Crear una función que nos retorne valores
def crear_contraseñas_random(num) :
     chars = "abcdefghij"
     num_entero = str(num)
     num = int(num_entero[0])
     c1 = num - 2
     c2 = num
     c3 = num -5
     contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num_entero *2}'
     return contraseña, num     
     
     #Desempaquetando la función
     
password, primer_numero = crear_contraseñas_random(981)

#Mostrando los resultados obtenidos y los datos utilizados para obtenerlos
print(f'Tu contraseña nueva es: {password}')
print(f'El número utilizado para crearla fue: {primer_numero}')
     
