"""
Ejercicio 1 — Presentación

Crea un programa que:

1. Le pida al usuario su nombre.
2. Le pida su edad.
3. Muestre un mensaje indicando su nombre, su edad y qué edad tendrá el próximo año.

"""


nombre = input()
print("Digite su edad: ")
edad = input()
proximo_año = int(edad) + 1
print("Hola " + nombre + ", tienes " + edad + " años.")
print("El próximo año tendrás " + str(proximo_año) + " años.")
