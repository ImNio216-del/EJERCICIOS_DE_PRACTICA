"""
Ejercicio 11 — Número mayor

Pide al usuario 5 números y determina cuál es el número mayor.
"""
cont = 0
mayor=0
while cont < 5: 
    
    print("Digita los 5 numeros")
    num = int(input())
    if cont==0:mayor=num
    elif num>mayor:mayor=num
    else:mayor

    cont+=1

print("El numero mayo es: " + str(mayor))
