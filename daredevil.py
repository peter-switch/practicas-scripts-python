# Lista de criminales: cada uno es un diccionario con 'nombre' y 'peligrosidad' (1-10)
criminales = [
    {"nombre": "Wilson Fisk", "peligrosidad": 10},
    {"nombre": "Bullseye", "peligrosidad": 9},
    {"nombre": "Frank Castle", "peligrosidad": 8},  # ¿Criminal o aliado? ;)
    {"nombre": "Turk Barrett", "peligrosidad": 4},
    {"nombre": "Owl", "peligrosidad": 6},
    {"nombre": "Vanessa Marianna", "peligrosidad": 5},
]

# 1. Filtrar criminales con peligrosidad >= 7

def filtrar_peligrosos(lista_criminales):
    peligrosos = []
    for criminal in lista_criminales: #Recorremos la lista
        if criminal["peligrosidad"]>=7: #Preguntamos a cada elemento de la lista por su peligrosidad
            peligrosos.append(criminal) #Añadimos a el criminar a la lista de peligrosos
    return peligrosos

# 2. Ordenar de mayor a menor peligrosidad

def ordenar_peligrosos(lista_peligrosos): #funcion recibe lista de criminales
    
    lista_ordenada=sorted(lista_peligrosos,key=lambda criminal:criminal["peligrosidad"],reverse=True)
    #sorted ordena y devuelve un listado ordenado
    #primera parametro:lista,tupla o diccionario
    #segundo parametro key:en eesete coso una funcion lamdba que recibe cada dato del diccionario y extra la peligrosidad

    return lista_ordenada

# 3. Buscar al Kingpin (Wilson Fisk) en la lista

def encontrar_kingpin(lista_criminales): #La función recibe la lista de criminales(es una lista con diccionarios dentro)

    kingpin_encontrado=False #Usamos este booleano en False, si encontramos a Kinping lo pasamos a True

    for dict in lista_criminales: #Iteramos con bucle for la lista de criminales pasando cada elemento diccionario a la variable dict
      
        if dict["nombre"]=="Wilson Fisk": #Si el elemento del diccionario dict["nombre"] contiene el nombre de pila de Kingpin...
            
            kingpin_encontrado=True #Cambiamos el boleano a True
            break #Importante romper el bucle si encontramos a Kingping para que no machaque el valor en siguientes iteraciones
        else:    
            kingpin_encontrado=False

    return "¡Kingpin encontrado!" if kingpin_encontrado else "Kingpin no está en la lista." #Retornamos un if con los textos convenientes.

# 4. Generar mensaje de advertencia

def mensaje_advertencia(lista_peligrosos):
    #Ordenamos la lista con sorted.Para la key usamos una func lambfa que recibe cada  elemento y ordena en funcion del valor peligrosidad.[:2]nos devuelve los 2 primeros
    mas_peligrosos=sorted(lista_peligrosos,key=lambda criminal:criminal["peligrosidad"],reverse=True)[:2]

       #Iteramos la lista ordenada con un bucle for y almacenamos solo los nombres en una lista de nombres.
    nombres=[(villanos["nombre"]) for villanos in mas_peligrosos]
        
    mensaje=f"* * * Los criminales más peligrosos son: {nombres[0]} y {nombres[1]} * * *"
  
    return print(mensaje)

# --- Ejecución ---
#print(filtrar_peligrosos(criminales))
#print(ordenar_peligrosos(criminales))
# print(encontrar_kingpin(criminales))
mensaje_advertencia(criminales)