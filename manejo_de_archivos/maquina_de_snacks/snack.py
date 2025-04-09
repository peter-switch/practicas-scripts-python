class Snack(): #Clase base para los snacks

    contador=0 #Contador de instancias de la clase Snack


    def __init__(self, nombre='', precio=0.0): #Constructor de la clase Snack
        self.nombre=nombre
        self.precio=precio
        Snack.contador+=1 #Incrementa el contador cada vez que se crea una instancia de Snack
        self.id=Snack.contador #Id de la instancia de Snack
    
    def __str__(self): #Método que devuelve una representación en cadena de la instancia de Snack
        
        return(f'Nombre del snack:{self.nombre} - Precio:{self.precio} - Id:{self.id} ')
        
    def escribirSnack(self): #Método que devuelve una representación en cadena de la instancia de Snack
        return f'Nombre del snack:{self.nombre} - Precio:{self.precio} - Id:{self.id}'
        
        
kitkat=Snack('Kit Kat', 3.5) #Instancia de la clase Snack

print(kitkat.__str__())#Método __str__ de la clase Snack
print(kitkat.escribirSnack()) #Método escribirSnack de la clase Snack
print(kitkat) #Método __str__ de la clase Snack
