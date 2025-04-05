"""
1. Dividir: Utiliza split(',') para dividir la cadena_productos en una lista de productos individuales.

2. Limpiar e Iterar: Recorre cada elemento de la lista resultante. Para cada elemento:

3. Utiliza strip() para eliminar cualquier espacio en blanco al principio o al final del nombre del producto.

4. Estandarizar: Dentro del bucle, verifica si el nombre del producto (después de limpiarlo
y convirtiéndolo a minúsculas para la comparación) es "platano".

5. Si es "platano", utiliza replace() (o simplemente asigna el nuevo valor)
para cambiar ese elemento específico de la lista a "banana tropical". Asegúrate de que el reemplazo
se haga sobre el elemento limpio que obtuviste en el paso anterior.

6. Si no es "platano", mantén el nombre del producto limpio tal como está.

7. Reconstruir: Guarda los productos (limpios y, si aplica, estandarizados) en una nueva lista.

8. Unir: Utiliza join() para unir todos los elementos de la nueva lista en una única cadena de texto, usando " - " 
(un guion rodeado de espacios) como separador. Mostrar: Imprime la cadena de texto final resultante.
"""

cadena_productos = "  manzana , pera, PLATANO , uva, melon , platano, NARANJA, kiwi  "
productos_pharse=[]
productos_lista=cadena_productos.split(",") #extra cada elemento de la cadena separado por comas
contador=0
for producto in productos_lista:
     productos_pharse.append(producto.strip().lower()) #Limpiamos elemento de espacios
     
for i in range(len(productos_pharse)): #Para modificar platano por banana necesitamos acceder a los indices de la lista con range(len)
     if productos_pharse[i]=="platano": #accedemos al indice de platano
        productos_pharse[i]="banana tropical" #sustituimos por banana
     else:
         pass #si no es platano, lo dejamos como está

nueva_cadena=" - ".join(productos_pharse) #Join une los elementos de una lista mediante el separador -

print(nueva_cadena)


"""
El siguiente código es una versión alternativa que utiliza un enfoque diferente para lograr el mismo resultado
sin usar índices en la lista

cadena_productos = "  manzana , pera, PLATANO , uva, melon , platano, NARANJA, kiwi  "
productos_lista = cadena_productos.split(",") 

productos_pharse = []

for producto in productos_lista:
    limpio = producto.strip().lower()
    if limpio == "platano":
        productos_pharse.append("banana tropical")
    else:
        productos_pharse.append(limpio)

nueva_cadena = " - ".join(productos_pharse)
print(nueva_cadena)


"""
