"""
Tenemos:

numeros = [10, 5, 20, 8, 15, 30, 3, 12, 25, 7]

Debes recorrer la lista y crear:

positivos = []

Pero esta vez:

Si el número es menor que 10, multiplícalo por 3.
Si está entre 10 y 20 inclusive, súmale 5.
Si es mayor que 20, divídelo entre 2.
Guarda todos los resultados en positivos.

Por ejemplo:

5  → 15
10 → 15
25 → 12.5

Al final imprime la lista.
"""

numeros = [10, 5, 20, 8, 15, 30, 3, 12, 25, 7]
positivos = []

for numero in numeros:
    if numero < 10 : numero *= 3
    if 10 <= numero <=20: numero += 5
    if numero > 20: numero/=2
    positivos.append(numero)
print(positivos)    