"""
Ejercicio 20 — Cajero automático 

El usuario comienza con:

saldo = 100000

Debe aparecer un menú repetidamente:

===== CAJERO =====

1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir

El programa debe:

1: Mostrar el saldo actual.
2: Pedir una cantidad y sumarla al saldo.
3: Pedir una cantidad y restarla del saldo solo si hay suficiente dinero.
4: Salir.
Cualquier otra opción → "Opción inválida".
"""
saldo = 100000
while True:
    print("===== CAJERO =====")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    num = int(input())
    if num ==1:
        print("Tu saldo actual es de: " +str(saldo))
    elif num == 2:
        print("Digita la cantidad de dinero que quieres añadir a la cuenta")
        num2 = int(input())
        saldo+= num2
    elif num == 3:
        print("Digita la cantidad de dinero que quieres restar a la cuenta")
        num3 = int(input())
        if num3 > saldo: print("No hay fondo suficientes")
        else: saldo-=num3
    elif num==4:
        print("Adios !!!")
        break
    else: print("Opción inválida")