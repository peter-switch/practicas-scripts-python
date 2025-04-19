#Lo primero instalar lo siguiente: pip install mysql-connector-python
import mysql.connector #una vez instalado el modulo de mysql connector importamos la  biblioteca


#creamos objeto con los datos de conexión
personas_db=mysql.connector.connect(
    host="***",
    user="****",
    password="****",
    database="****"

)

#Es necesario crear un objeto cursor. Será que se encargue de mantener abierta la conexión y ejecutar sentencias
cursor=personas_db.cursor()
#una vez creado con el método execute, ejecutamos la sentencia sql
cursor.execute("SELECT * FROM personas")
#con el método fetchall obtenemos los datos de la sentencia ejecutada y lo guardamos en una variable
resultado=cursor.fetchall()

#recorremos resultado e imprimimos
for persona in resultado:
    print(persona)

cursor.close() #cerramos el cursor
personas_db.close() #cerramos conexion

