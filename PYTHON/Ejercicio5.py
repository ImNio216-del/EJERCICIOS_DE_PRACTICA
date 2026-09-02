"""
Ejercicio 5 — Adivina el número 🔢

Crea un programa que tenga un número secreto.

El usuario debe intentar adivinarlo.

El programa debe indicar:

Si el número ingresado es menor que el número secreto.
Si el número ingresado es mayor que el número secreto.
Si acertó.

El usuario tendrá 3 intentos.
"""
numsec = 7
intentos = 1 

while intentos < 4:
    print("Intento" + str(intentos))
    num1 = int(input())
    if      num1 > numsec: print("El numero secreto es menor")
    elif    num1 < numsec: print("El numero secreto es mayor")
    else: 
        print("Acertaste el numero") 
        break
    intentos+=1

