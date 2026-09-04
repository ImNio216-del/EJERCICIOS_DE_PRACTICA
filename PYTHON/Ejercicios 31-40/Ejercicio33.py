"""
Ejercicio 36 — Modificar datos

Ahora quiero cambiar una cosa importante: en lugar de crear otra 
lista, vamos a modificar los diccionarios originales.

Tenemos:

productos = [
    {"nombre": "Laptop", "precio": 3000},
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Teclado", "precio": 150},
    {"nombre": "Monitor", "precio": 900},
    {"nombre": "Audifonos", "precio": 250}
]

Recorre los productos.

Reglas

Si el precio es mayor o igual a 500:

➡️ Aplica un descuento del 10%.

Si es menor de 500:

➡️ Aplica un descuento del 5%.

Debes modificar directamente:

producto["precio"]
"""

productos = [
    {"nombre": "Laptop", "precio": 3000},
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Teclado", "precio": 150},
    {"nombre": "Monitor", "precio": 900},
    {"nombre": "Audifonos", "precio": 250}
]

for producto in productos:
    if producto["precio"] >= 500: producto["precio"]=producto["precio"]-(producto["precio"]/10)
    else:producto["precio"]=producto["precio"]-(producto["precio"]/5)

print(productos)