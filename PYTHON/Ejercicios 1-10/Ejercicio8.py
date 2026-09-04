"""
Ejercicio 8 — Suma acumulativa

Pide al usuario un número y calcula la suma de todos los números desde 1 hasta ese número.

"""

print("Digite un numero:")

num = int(input())

contador = 1
suma = 0

while contador <= num:

    suma += contador

    contador += 1

print("La suma total es: " + str(suma))