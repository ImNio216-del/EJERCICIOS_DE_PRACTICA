"""
Ejercicio 26 — Analizador de números
numeros = [4, 15, 7, 22, 10, 31, 8, 19, 40, 3]

Crea estas listas:

pares = []
impares = []

Recorre numeros.

Para cada número, haz exactamente UNA transformación:

Si es par, multiplícalo por 2 y guárdalo en pares.
Si es impar, multiplícalo por 3 y guárdalo en impares.
"""

numeros = [4, 15, 7, 22, 10, 31, 8, 19, 40, 3]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0 :
        numero*=2
        pares.append(numero)
    else:
        numero*=3
        impares.append(numero)

print(pares)
print(impares)