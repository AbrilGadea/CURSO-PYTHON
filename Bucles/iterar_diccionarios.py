diccionario = {
    "nombre" : "Lucas",
    "apellido" : "Dalto",
    "susb" : 100000
}

#Recorriendo diccionarios para obtener claves
for keys in diccionario :
  print(f'la clave es: {keys}')
    
    
#Recorriendo diccionarios con item() para obtener la clave y el valor
for datos in diccionario.items() :
    keys = datos [0]
    value = datos [1]
    print(f'la clave es: {keys} y el valor es: {value}')