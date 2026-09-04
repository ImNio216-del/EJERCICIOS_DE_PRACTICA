"""
Ejercicio 6 — Tabla de multiplicar

Crea un programa que le pida al usuario un número y muestre su tabla de multiplicar del 1 al 10.
"""

print("Digita el numero que quieras saber su tabla de multiplicar.")
num=int(input())
operando = 1
while operando < 11:
    resultado=num*operando
    print(str(operando)+ " * " + str(num)+ " = "+ str(resultado))
    operando +=1
