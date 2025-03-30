personajes = [
    {"nombre": "Tony Stark", "alias": "Iron Man", "poder": 9, "es_heroe": True},
    {"nombre": "Steve Rogers", "alias": "Capitán América", "poder": 8, "es_heroe": True},
    {"nombre": "Natasha Romanoff", "alias": "Black Widow", "poder": 7, "es_heroe": True},
    {"nombre": "Thanos", "alias": None, "poder": 10, "es_heroe": False},
    {"nombre": "Loki", "alias": None, "poder": 9, "es_heroe": False},
    {"nombre": "Wanda Maximoff", "alias": "Scarlet Witch", "poder": 9, "es_heroe": True},
]

# --- Funciones a implementar ---
def filtrar_personajes(lista_personajes, es_heroe):

    # Retorna una lista de héroes si es_heroe=True, o villanos si es_heroe=False.
    lista_heroes=[] #Lista vacía para almacenar héroes
    lista_villanos=[] #Lista vacía para almacenar villanos

    for super in personajes: #iteramos la lista de diccionarios con un bucle for
        
        if super["es_heroe"]==True: #Si el campor es_heroe es igual a True...
            lista_heroes.append(super["nombre"]) #...añadimos a la lista de héroes el nombre del super
        else:
            lista_villanos.append(super["nombre"]) #de lo contrario añadimos el nombre del super a villanos

    print (lista_heroes if es_heroe==True else lista_villanos) #imprime lista según el caso
    return lista_heroes if es_heroe==True else lista_villanos #retorna los valores

filtrar_personajes(personajes,False) #Ejecuta la función

def encontrar_mas_poderoso(lista_personajes):
    # Retorna el personaje con mayor poder (si hay empate, retorna cualquiera de ellos).
    #mas_poderoso=sorted(lista_personajes, key=lambda x: x["poder"],reverse="True")[0]
    mas_poderoso=(max(lista_personajes,key=lambda x:x["poder"]))

    print(f'* * * El más poderoso es: {mas_poderoso["nombre"]}* * *')
    return mas_poderoso


encontrar_mas_poderoso(personajes)

def formar_equipo(lista_personajes, es_heroe, poder_minimo):
    # Retorna un equipo (lista) de héroes o villanos con poder >= poder_minimo.
    # Ej: formar_equipo(personajes, True, 8) -> [Iron Man, Scarlet Witch]
    pass

# --- ¡Extra opcional! ---
def encontrar_rivales(lista_personajes, diferencia_maxima=1):
    # Retorna parejas [héroe, villano] cuyos poderes difieran en <= diferencia_maxima.
    # Ej: ("Iron Man", "Loki") (poder 9 vs 9).
    pass