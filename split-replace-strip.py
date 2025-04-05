"""

Dividir: Utiliza split(',') para dividir la cadena_productos en una lista de productos individuales.

Limpiar e Iterar: Recorre cada elemento de la lista resultante. Para cada elemento:

Utiliza strip() para eliminar cualquier espacio en blanco al principio o al final del nombre del producto.

Estandarizar: Dentro del bucle, verifica si el nombre del producto (después de limpiarlo y convirtiéndolo a minúsculas
para la comparación) es "platano".
Si es "platano", utiliza replace() (o simplemente asigna el nuevo valor) para cambiar ese elemento específico de la lista a "banana tropical". Asegúrate de que el reemplazo se haga sobre el elemento limpio que obtuviste en el paso anterior.
Si no es "platano", mantén el nombre del producto limpio tal como está.
Reconstruir: Guarda los productos (limpios y, si aplica, estandarizados) en una nueva lista.
Unir: Utiliza join() para unir todos los elementos de la nueva lista en una única cadena de texto, usando " - " (un guion rodeado de espacios) como separador.
Mostrar: Imprime la cadena de texto final resultante."""

cadena_productos = "  manzana , pera, PLATANO , uva, melon , platano, NARANJA, kiwi  "
productos_pharse=[]
productos_lista=cadena_productos.split(",") #extra cada elemento de la cadena separado por comas

for producto in productos_lista:
    productos_pharse.append(producto.strip().upper()) #Limpiamos elemento de espacios y añadimos a una nueva lista

print(productos_pharse)
