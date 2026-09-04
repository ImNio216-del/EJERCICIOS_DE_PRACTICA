"""
Ejercicio 18 — Promedio hasta introducir 0

Ahora vamos a combinar varias cosas que ya aprendiste.

El programa debe pedir números continuamente y calcular su promedio.

La entrada de 0 debe indicar que el usuario terminó.

Importante: el 0 no debe incluirse en el promedio.
"""

sumatoria=0
conteo=0
prohibido=1
while prohibido != 0:
    print("Digita un numero")
    num = int(input())
    if num==0:break
    else:
        sumatoria+=num
        prohibido=num
        conteo+=1

total=sumatoria/(conteo)
print(total)