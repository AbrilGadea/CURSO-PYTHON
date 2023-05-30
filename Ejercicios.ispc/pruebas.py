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

