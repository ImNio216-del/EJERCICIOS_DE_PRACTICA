"""
Ejercicio 13 — Promedio de números

Pide al usuario 5 números y calcula el promedio de esos números.
"""
cont  = 0
sumatoria = 0
while cont < 5: 
    print("Digita los 5 numeros")
    num = int(input())
    sumatoria+=num

    cont+=1
promedio = sumatoria/5
print("El promedio es: " + str(promedio))