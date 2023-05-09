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
    
    print(f'Hola {nombre} mi {adjetivo}, ¿Cómo andas?')
    
saludar("Abril", "mujer")   
 