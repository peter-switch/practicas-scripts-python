nombre_archivo='contactos.txt'


#Bloque with:una vez ejecutadas las líneas cierra el archivo automáticamente
try:
    with open(nombre_archivo,'x') as archivo:
        archivo.write('LODE\n')
        archivo.write('Un podcast muy recomendable\n')

except Exception as e:
    print(f"HAY UN ERROR: EL ARCHIVO YA EXISTE {e}")

#Método manual: hasta que no se ejecuta close no se cierra el archivo
archivo=open(nombre_archivo,'a')
archivo.write('Puedes escucharlo en Ivoox\n')
archivo.write('Y en Spotify\n')
archivo.close()