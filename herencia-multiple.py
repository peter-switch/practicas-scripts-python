""" Ejercicio: "Sistema de limpieza y estandarización de productos"

📝 Enunciado:
Tienes una lista de productos en forma de cadena larga. Crea un sistema modular y reutilizable que haga lo siguiente:

1. Clase base LimpiadorDeTexto
Tiene un método limpiar(producto: str) que:

Elimina espacios con .strip()

Convierte el texto a minúsculas con .lower()

2. Clase base Estandarizador
Tiene un atributo reglas (diccionario) que relaciona nombres originales con los estandarizados. Ejemplo:

python
Copiar
Editar
{'platano': 'banana tropical', 'manzana': 'apple deluxe'}
Tiene un método estandarizar(producto: str) que:

Usa una función lambda para verificar si el producto está en las reglas

Si está, lo reemplaza

3. Clase hija ProcesadorDeProductos
Hereda de ambas clases (LimpiadorDeTexto, Estandarizador) y:

Tiene un método procesar(cadena: str) que:

Divide la cadena por comas

Limpia y estandariza cada producto

Devuelve una nueva cadena con los productos finales unidos por " | " (barra vertical) """
