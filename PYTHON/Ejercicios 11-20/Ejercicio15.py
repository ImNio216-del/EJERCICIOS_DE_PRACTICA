"""
Ejercicio 15 — Menú interactivo 

Crea un programa que muestre este menú:

===== MENÚ =====

1. Saludar
2. Mostrar un mensaje
3. Mostrar un número
4. Salir

Digite una opción:

El programa debe:

Si el usuario selecciona 1, mostrar "¡Hola!"
Si selecciona 2, mostrar "¡Estoy aprendiendo Python!"
Si selecciona 3, pedir un número y mostrarlo.
Si selecciona 4, terminar el programa.
Si introduce cualquier otra opción, mostrar "Opción inválida".

El menú debe seguir apareciendo después de cada opción, 
excepto cuando el usuario seleccione 4.
"""

numero=0

while numero != 4:
    print("===== MENÚ =====")
    print("1. Saludar")
    print("2. Mostrar un mensaje")
    print("3. Mostrar un número")
    print("4. Salir")
    print("Digita una opcion")
    num = int(input())

    if num==1:print("¡Hola!")
    elif num==2:print("¡Estoy aprendiendo Python!")
    elif num==3:
        print("Dame un numero")
        num2=int(input())
        print("Tu numero es: "+ str(num2))
    else:numero=4
