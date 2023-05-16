#1. Diseña un algoritmo que introduzca por teclado el nombre de 3 países, se almacenen en una lista y 
# los muestre por pantalla.
países = list(["Argentina", "Australia", "Grecia"])
#print(países)

#2. Diseña un algoritmo que almacene los precios de 4 productos que compré en una lista y
# luego me muestre el total en pantalla.
precios = list([200,500,600,700])
suma_de_precios = sum(precios)
print(suma_de_precios)

#3. Diseña un algoritmo que almacene las letra de tu nombre en una lista y luego muestre el nombre.
letras = list (['A,B,R,I,L'])
#resultado = letras.join(letras)
#print(resultado)?????????

#4. Diseña un algoritmo que introduzca por teclado el nombre, materia, profesor y nota. 
# Se almacene en una tupla y luego muestre los datos en pantalla.
tupla = ("Abril", "Literatura Argentina I", "Doc", "10")
nombre, materia, profesor, nota = tupla
resultado = f'Mi nombre es {nombre}, estudio {materia} con el prefesor {profesor} y me saqué un {nota}'
print(resultado)

#5. Diseña un algoritmo que introduzca por teclado el nombre de 3 materias y sus notas correspondientes.
# Deben almacenarse las materias en una tupla y las notas en otra.
# Luego muestre en pantalla la materia con su nota correspondiente.

Materias = ("Literatura Clásica", "Literatura Argentina", "Semiótica")
Notas = ("9", "10", "10")
for Materias, Notas in zip (Materias, Notas) :
        print(f'A {Materias} corresponde {Notas}')


#6. Diseña un algoritmo con un diccionario que contenga como clave 3 materias que estás cursando y
#como valores uses tuplas para almacenar 2 notas por materia. 
#Luego por pantalla muestres las notas de cada materia.

diccionario = {
    'Literatura Latianoamericana' : ('10, 9'),
    'Linguística' : ('9,10'),
    'Literatura francesa' : ('10, 10')
    }
notas1 = diccionario.get('Literatura Latianoamericana')
notas2 = diccionario.get('Linguística')
notas3 = diccionario.get('Literatura francesa')
print(notas1, notas2, notas3)
















