"""
Ejercicio 28 — Vamos a subir otro nivel
Ahora quiero que además de crear listas, tengas que llevar contadores y acumuladores.
Tenemos:
numeros = [10, 25, 8, 33, 14, 40, 7, 19, 30, 5]
Crea:
pares = []
impares = []
cantidad_pares = 0
cantidad_impares = 0
suma_pares = 0
suma_impares = 0
Recorre la lista.
Para cada número:

Si es par:

Agrégalo a pares.
Aumenta cantidad_pares.
Súmalo a suma_pares.

Si es impar:

Agrégalo a impares.
Aumenta cantidad_impares.
Súmalo a suma_impares.

Al final imprime:

Pares: [...]
Impares: [...]
Cantidad de pares: X
Cantidad de impares: X
Suma de pares: X
Suma de impares: X
"""

numeros = [10, 25, 8, 33, 14, 40, 7, 19, 30, 5]

pares = []
impares = []

cantidad_pares = 0
cantidad_impares = 0

suma_pares = 0
suma_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        cantidad_pares+=1
        suma_pares+=numero
    else:
        impares.append(numero)
        cantidad_impares+=1
        suma_impares+=numero

print("Pares:", pares)
print("Impares:", impares)
print("Cantidad de pares:", cantidad_pares)
print("Cantidad de impares:", cantidad_impares)
print("Suma de pares:", suma_pares)
print("Suma de impares:", suma_impares)