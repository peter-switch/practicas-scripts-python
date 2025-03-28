"""
Vamos a crear una función que obtenga el factorial de un número dado.
Ejemplo de lo que es un factorial

Dado el número 5. ¿Cuál es su factorial?

1x2x3x4x5=120
1x1
1x2=2
2x3=6
6x4=24
24x5=120

"""

def factor(n):
    resultado=1
    for i in range(1,n+1):
        resultado=resultado*i
    print(f'El factor de {n} es {resultado}')

n=int(input("Introduce un número: "))
factor(n)
