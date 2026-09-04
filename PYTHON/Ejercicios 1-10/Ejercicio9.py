"""
Ejercicio 9 — Factorial

Pide al usuario un número entero positivo y calcula su factorial.

El factorial de un número se obtiene multiplicándolo por todos los 
números anteriores hasta llegar a 1.
"""


print("Digite un numero:")

num = int(input())

contador = 1
suma = 1

while contador <= num:

    suma *= contador

    contador += 1

print("La suma total es: " + str(suma))