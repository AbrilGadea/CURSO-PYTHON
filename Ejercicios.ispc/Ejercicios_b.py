
#1)      Escribir un programa que permita validar el ingreso a un sistema. 
#Se deberá solicitar el ingreso por teclado de nombre de usuario y contraseña. 
# Será valido como nombre de usuario “admin” y como contraseña “1234”.
# Si el ingreso es correcto deberá mostrar por pantalla el mensaje “Ingreso exitoso”.
#Opcional 1: permitir como usuario valido también su propio nombre y su propia contraseña.
#Opcional 2: solamente permitir el ingreso incorrecto de los datos 3 veces, luego de ello, 
# no permitir más ingresos y mostrar por pantalla “Cuenta bloqueada”.


#usuario = input('Ingrese usuario: ')
#contraseña = input('Ingrese contraseña: ')
#contador = 0
#max_intentos = 3

#while contador < 3:
    #if usuario == "Admin" and contraseña == "1234":
        #print("Ingreso exitoso")
        #break  # Sale del bucle si se ingresa exitosamente

    #contador += 1
#else:
    #print("Tu contraseña o usuario son incorrectos. Por favor, intenta nuevamente.")
    #contador += 1


#if contador == 3: #No cumple la funcion de poner el ultimo mensaje de advertencia
   #print("Superó el límite de intentos diarios. Por favor, comuníquese al 0800-000-000.")
    
  
#2)      Mostrar por pantalla el siguiente menú:
#CAJERO AUTOMATICO
#ISPC
#Listado de opciones:
#1)      Ingreso de dinero
#2)      Extracción de dinero
#3)      Consulta de saldo
#4)      Salir
#Ingrese su selección: _
#El programa deberá mostrar luego del ingreso de cada opción “Usted ha seleccionado la opción x”, 
# por ejemplo, en el caso de ingresar un 1, deberá mostrar por pantalla “Usted ha seleccionado la opción 1” 
# y así sucesivamente. Al seleccionar la opción 4 se debe terminar la ejecución del programa.
 



print("CAJERO AUTOMATICO")
print("ISPC")
print("Listado de opciones:")
print("1)      Ingreso de dinero")
print("2)      Extracción de dinero")
print("3)      Consulta de salto")
print("4)      Salir")

    
ingreso = input("Ingrese su selección: ")
saldo_inicial = 10000

while ingreso != '4':
    if ingreso == "1":
        print("Usted ha ingresado la opción 1")
        deposito = int(input("Ingrese un importe a depositar: "))
        saldo_inicial += deposito
        print('Su nuevo saldo es:', saldo_inicial)
        # contador = 1
        # callbacks()

    elif ingreso == "2":
        print("Usted ha ingresado la opción 2")
        extraccion = int(input("Ingrese un importe a extraer: "))

        if extraccion <= saldo_inicial:
            saldo_inicial -= extraccion
            print('Su nuevo saldo es:', saldo_inicial)
            # contador = 2
        else:
            print('Lo ingresado es mayor a lo disponible')

    elif ingreso == "3":
        print('Su saldo es:', saldo_inicial)

    ingreso = input("Ingrese su selección: ")

    #if ingreso == "1" or ingreso == "2":
        #saldo_inicial += int(ingreso)

print("Retire su tarjeta")

    
    #3)      Deberá continuar con el ejercicio 2 y escribir la lógica del cajero automático de la siguiente manera.
#a.       Su saldo inicial será de $10000.
#b.       Al seleccionar la opción 1 se pedirá al usuario que ingrese un importe por teclado el cual se sumará a su 
# saldo inicial.
#c.       De la misma manera al seleccionar la opción 2, se solicitará un importe por teclado el cual se 
# restará al saldo inicial.
#d.       Con la opción 3 se consultará su saldo actual.
#e.       En todo momento se deberá controlar que no se pueda extraer dinero, si no se cuentan con fondos suficientes.


    