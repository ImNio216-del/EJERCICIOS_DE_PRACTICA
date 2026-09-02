"""
Ejercicio 7 — Contador

Crea un programa que pida al usuario un número y cuente desde 1 hasta ese número.
"""
print("Digite un numero")
num = int(input())

end = 0
while end < num:

    cont = end+1
    print (cont)
    end += 1
print("Conteo terminado.")