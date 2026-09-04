"""
Ejercicio 16 — Adivinar hasta acertar 

El programa tendrá un número secreto:

numero_secreto = 25

El usuario debe intentar adivinarlo sin límite de intentos.

Después de cada intento:

Si el número es menor → "El número secreto es mayor."
Si el número es mayor → "El número secreto es menor."
Si acierta → "¡Acertaste!" y el programa termina.
"""
numero_secreto = 25
adivina = 0
while adivina != numero_secreto:
    print("Digita un numero")
    num = int(input())
    if   num>numero_secreto: print("El número secreto es menor.")
    elif num<numero_secreto: print("El número secreto es mayor.")
    else: 
        print ("¡Acertaste!")
        adivina=numero_secreto