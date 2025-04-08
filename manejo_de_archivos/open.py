nombre_archivo='contactos.txt'


#Bloque with:una vez ejecutadas las líneas cierra el archivo automáticamente
with open(nombre_archivo,'w') as archivo:
    archivo.write('La Maniobra Adama\n')
    archivo.write('Un podcast muy recomendable\n')



#Método manual: hasta que no se ejecuta close no se cierra el archivo
archivo=open(nombre_archivo,'a')
archivo.write('Puedes escucharlo en Ivoox\n')
archivo.write('Y en Spotify\n')
archivo.close()