"""
Ejercicio 19 — Máximo, mínimo y promedio

Ahora vamos a combinar varias cosas que ya sabes.

El programa debe pedir números continuamente hasta que el usuario introduzca 0.

Al terminar debe mostrar:

El número mayor
El número menor
El promedio
La cantidad de números introducidos
"""

mayor=0
menor=0
sumatoria=0
conteo=0
while True:
    print("Digita un numero")
    num = int(input())
    if num==0:
        break
    elif conteo==0: 
        menor=num
        mayor=num
    if num>mayor:mayor=num
    if num<menor:menor=num
    sumatoria+=num
    conteo+=1 
if conteo != 0:
    promedio=sumatoria/conteo     
    print("El numero mayor es: "+ str(mayor))
    print("El numero menor es: "+ str(menor))
    print("El promedio es: "+ str(promedio))
    print("La cantidad de números introducidos: "+ str(conteo))
else:print("Haz salido de la calculadora antes de tiempo")  
