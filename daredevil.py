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
def encontrar_kingpin(lista_criminales):

# ¡Completa aquí!
    kingpin_encontrado=False
    for dict in lista_criminales:
      
        if dict["nombre"]=="Wilson Fisk":
            
            kingpin_encontrado=True
            break
        else:    
            kingpin_encontrado=False

    return "¡Kingpin encontrado!" if kingpin_encontrado else "Kingpin no está en la lista."

# 4. Generar mensaje de advertencia
def mensaje_advertencia(lista_peligrosos):
    # Ejemplo: "¡Cuidado! Los criminales más peligrosos son: Wilson Fisk, Bullseye."
    # ¡Completa aquí!
    return mensaje

# --- Ejecución ---
#print(filtrar_peligrosos(criminales))
#print(ordenar_peligrosos(criminales))
print(encontrar_kingpin(criminales))