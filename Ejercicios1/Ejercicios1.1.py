#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5
#Duración de crudos
crudo_promedio = 5
crudo_dalto= 3.5

#Diferencias de duración
diferencias_con_min = 100 - dalto_curso / otros_cursos_min *100
diferencias_con_max = 100 - dalto_curso * 1000 // otros_cursos_max /10
diferencias_con_promedio = 100 - dalto_curso / otros_cursos_promedio *100

#Mostrando las diferecias de duración EJERCICIO A
print(f' - El curso de dalto dura:')
print(f' - El curso de Dalto dura un {diferencias_con_min}% menos que el más rápido')
print(f' - El curso de Dalto dura un {diferencias_con_max}% menos que el más lento')
print(f' - El curso de Dalto dura un {diferencias_con_promedio}% menos que el promedio')
print("...............")

#Calculando el porcentaje de tiempo vacío removido
tiempo_vacio_promedio =  100 - otros_cursos_promedio * 1000 // crudo_promedio /10
tiempo_vacio_dalto =  100 - dalto_curso * 1000 // crudo_dalto /10

#Mostrando la cantidad de espacios vacíos que se remueven EJERCICIO B

print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío')
print(f'Este curso eliminó {tiempo_vacio_dalto}% de tiempo vacío')
print("...............")
#Mostrando diferencias si los cursos duraran 10 horas LA DOBLE DIVISIÓN Y MULTIPLICACIÓN POR 100 ES PARA REDONDEAR FLOTANTES
print(f' Ver 10 horas de este curso equivale a ver {otros_cursos_promedio *100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de este curso equivale a ver {dalto_curso *100 // otros_cursos_promedio / 10} horas de otros cursos')
print("...............")