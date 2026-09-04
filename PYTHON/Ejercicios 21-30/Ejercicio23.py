"""
Ejercicio 24 — Separar y transformar
Tienes esta lista:
numeros = [5, 12, 8, 21, 30, 7, 16, 3, 40, 11]
Recorre la lista con un for y crea dos listas nuevas:
mayores = []
menores = []

Reglas
Para cada número:
Si es mayor o igual a 15, agrégalo a mayores.
Si es menor que 15, agrégalo a menores.
Pero hay una condición adicional:
Los números que sean pares deben guardarse multiplicados por 2.

Por ejemplo:

12 → es menor que 15 y es par → 24
5  → es menor que 15 e impar → 5
30 → es mayor que 15 y es par → 60

Al final deberías obtener:

Mayores: [42, 60, 32, 80]
Menores: [5, 24, 16, 7, 6, 22]
"""

numeros = [5, 12, 8, 21, 30, 7, 16, 3, 40, 11]
mayores = []
menores = []

for numero in numeros:
    if numero % 2 ==0: 
        numero*=2
    if numero >= 15:mayores.append(numero)
    else: menores.append(numero)
print(mayores)
print(menores)