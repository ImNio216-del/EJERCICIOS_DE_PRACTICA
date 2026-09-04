"""
35 — Primer problema un poco más "real"

Ahora vamos a combinar lista de diccionarios + procesamiento + 
creación de una nueva lista.

Tenemos:

productos = [
    {"nombre": "Laptop", "precio": 3000},
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Teclado", "precio": 150},
    {"nombre": "Monitor", "precio": 900},
    {"nombre": "Audifonos", "precio": 250}
]

Crea una lista vacía:

productos_caros = []

Recorre los productos.

Si el precio es mayor o igual a 500, agrega a productos_caros 
solamente el nombre del producto.
"""

productos = [
    {"nombre": "Laptop", "precio": 3000},
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Teclado", "precio": 150},
    {"nombre": "Monitor", "precio": 900},
    {"nombre": "Audifonos", "precio": 250}
]


productos_caros = []

for producto in productos:
    if producto["precio"] >= 500:
        productos_caros.append(producto["nombre"])
print(productos_caros)
