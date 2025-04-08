nombre_archivo="leeme.txt"

with open('leeme.txt','r') as archivo:
    lista=archivo.readlines()

for linea in lista:
    print(linea)


with open('leeme.txt','r') as archivo:
    cadena=archivo.read()

print(cadena)    