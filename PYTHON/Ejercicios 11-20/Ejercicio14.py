"""
Ejercicio 14 — Contar pares e impares

Pide al usuario 5 números y determina:

Cuántos son pares
Cuántos son impares
"""
cont    = 0
pares   = 0
impares = 0
while cont < 5: 
    print("Digita los 5 numeros")
    num = int(input())
    if num % 2 == 0: pares+=1
    else: impares +=1

    cont+=1
print(str(impares)+" Son impares " )
print(str(pares)+" Son pares " )
