
#1)      Escribir un programa que permita validar el ingreso a un sistema. 
#Se deberá solicitar el ingreso por teclado de nombre de usuario y contraseña. 
# Será valido como nombre de usuario “admin” y como contraseña “1234”.
# Si el ingreso es correcto deberá mostrar por pantalla el mensaje “Ingreso exitoso”.
#Opcional 1: permitir como usuario valido también su propio nombre y su propia contraseña.
#Opcional 2: solamente permitir el ingreso incorrecto de los datos 3 veces, luego de ello, 
# no permitir más ingresos y mostrar por pantalla “Cuenta bloqueada”.


    
usuario = input ('Ingrese usuario : ')
contraseña = input ('Ingrese contraseña : ')

#contador = 0
#while contador <3: 


if usuario == "Admin":
    if contraseña == "1234":
        print("Ingreso exitoso")
else:
    print("Tu contraseña o usuario son incorrectos")
    
    #if contador == 3:
        # print("Superó el límite de intentos diarios, le solicitamos por favor comunicarse al 0800-000-000")

 



