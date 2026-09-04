"""
Ejercicio 17 — Suma hasta introducir 0

Crea un programa que permita al usuario introducir números continuamente.

El programa debe:

Sumar todos los números introducidos.
Cuando el usuario introduzca 0, debe terminar.
Mostrar la suma total.
"""

sumatoria = 0
prohibido = 1
while prohibido != 0:
    print("Digita un numero")
    num = int(input())
    sumatoria+=num
    prohibido=num
print("Esta es la sumatoria: "+ str(sumatoria))  