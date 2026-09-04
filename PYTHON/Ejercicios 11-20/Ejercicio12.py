"""
Ejercicio 12 — Número menor

Ahora vamos a hacer prácticamente lo contrario.

Pide al usuario 5 números y determina cuál es el número menor.
"""
cont  = 0
menor = 0
while cont < 5: 
    print("Digita los 5 numeros")
    num = int(input())
    if cont==0:menor=num
    elif menor>num:menor=num
    else:menor

    cont+=1

print("El numero mayo es: " + str(menor))