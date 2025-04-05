"""La programación en Python es muy divertida y útil. Python es un lenguaje versátil que se utiliza en análisis de datos, desarrollo web, inteligencia artificial
y muchas otras áreas. La sintaxis de Python es clara y fácil de aprender, lo que hace que Python sea ideal para principiantes.


Debes crear un programa que realice las siguientes tareas:

Utiliza split() para dividir el texto en oraciones (ten en cuenta que las oraciones terminan con punto).
Para cada oración, utiliza find() para determinar si contiene la palabra "Python".
Si la oración contiene "Python", utiliza replace() para cambiar "Python" por "Python 3".
Finalmente, une todas las oraciones modificadas y muestra el resultado final.

Cuando hayas completado el ejercicio, comparte tu código y estaré encantado de corregirlo.
¡Buena suerte!"""

cadena="La programación en Python es muy divertida y útil. Python es un lenguaje versátil que se utiliza en análisis de datos, desarrollo web, inteligencia artificial y muchas otras áreas. La sintaxis de Python es clara y fácil de aprender, lo que hace que Python sea ideal para principiantes."
frase_rep=[]
frases=cadena.split(".")


for frase in frases:
    if frase.find("Python") != -1:
        frase_rep.append(frase.replace("Python","Python 3"))
        
for i in frase_rep:
   print(f'{i}.', end="")


 
        