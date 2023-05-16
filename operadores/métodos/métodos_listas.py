#FUNCIÓN LIST, CREA UNA LISTA

lista = list(["hola", "dalto", 34])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregar un elemento a la lista

lista.append("JJAJAJAJA")

#agregando un elemento a la lista en un índice específico
lista.insert(2, "toma mama")

#agregando varios elementos a la lista
lista.extend([False, 2030])            
#eliminando un elemento dela lista (por su índice) si ponemos -1 se elimina l último elemento de la lista
lista.pop(0) 
     
 #invirtiendo los elementos de una lista (no necesariamente númerico, no la ordena primero como sort)
lista.reverse()        
  
  
#sort ordena los elementos de manera ascendente (númericos o true y false)
lista.sort()
#ordenando una lista de manera reversiva
lista.sort(reverse=True)
           
 #eliminando todos los elementos de la lista     
lista.crear()       
print(lista)


#CON LAS TUPLAS SOLO SE PUEDE BUSCAR ELEMENTOS Y CONTARLOS, NO REALIZAR TODAS LAS OTRAS FUNCIONES, SON INIMUTABLES#