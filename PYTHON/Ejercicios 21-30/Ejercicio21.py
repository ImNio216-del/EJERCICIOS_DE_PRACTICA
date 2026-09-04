"""
Ejercicio 21 — Validación de contraseña 

Crea un programa que tenga una contraseña almacenada:

contraseña = "python123"

El usuario debe introducir la contraseña.

Si es correcta → mostrar "Acceso concedido" y terminar.
Si es incorrecta → mostrar "Contraseña incorrecta" y volver a pedirla.
El usuario tendrá 3 intentos.
Si falla los 3 → mostrar "Cuenta bloqueada" y terminar.
"""

contraseña = "python123"
intentos = 3
while True:
    if intentos==0:
        print("Cuenta bloqueada")
        break

    print("Digita la contraseña")
    contraseña_ingresada = input()

    if contraseña_ingresada==contraseña:
        print("Acceso concedido")
        break
    else:
        print("Contraseña incorrecta")
    intentos-=1    