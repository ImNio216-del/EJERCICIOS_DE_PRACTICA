"""
Ejercicio 22 — Análisis de una lista 

Crea una lista con estos números:

numeros = [12, 7, 25, 4, 18, 9, 30, 15]

Utilizando for, el programa debe determinar:

El número mayor.
El número menor.
Cuántos números son pares.
Cuántos números son impares.
La suma de todos los números.
El promedio.

"""

numeros = [12, 7, 25, 4, 18, 9, 30, 15]
mayor = 0
menor = 0
pares = 0
impares = 0
sumatoria = 0
conteo=0
for numero in numeros:
   #mayor y menores 
    if numero>=mayor:mayor=numero
    if menor==0:menor=numero
    elif menor>=numero:menor=numero
    #Numero de pares e impares
    if numero % 2 == 0:pares+=1
    else: impares+=1
    #Suma de los numeros
    sumatoria+=numero   
    conteo+=1               
promedio = sumatoria/conteo
    
print("El numero mayor: "+ str(mayor))
print("El numero menor: "+ str(menor))
print("El numero de pares: "+ str(pares))
print("El numero de impares: "+ str(impares))
print("El promedio: "+ str(promedio))