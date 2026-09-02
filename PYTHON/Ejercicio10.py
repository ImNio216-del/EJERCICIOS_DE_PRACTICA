"""
Ejercicio 10 — Número de dígitos

Pide al usuario un número entero positivo y determina cuántos dígitos tiene.
"""


print("Digite un numero:")

num = int(input())

contador = 0

while num > 0:
    num //= 10
    contador += 1

print("El número tiene " + str(contador) + " dígitos.")