"""
Ejercicio 37

Ahora vamos a dejar de trabajar solamente con precios.

Tenemos:

productos = [
    {"nombre": "Laptop", "precio": 3000, "stock": 5},
    {"nombre": "Mouse", "precio": 80, "stock": 20},
    {"nombre": "Teclado", "precio": 150, "stock": 0},
    {"nombre": "Monitor", "precio": 900, "stock": 3},
    {"nombre": "Audifonos", "precio": 250, "stock": 0}
]

Recorre la lista y agrega una nueva clave llamada "estado" a cada producto.

Si stock > 0:

"Disponible"

Si stock == 0:

"Agotado"
"""
productos = [
    {"nombre": "Laptop", "precio": 3000, "stock": 5},
    {"nombre": "Mouse", "precio": 80, "stock": 20},
    {"nombre": "Teclado", "precio": 150, "stock": 0},
    {"nombre": "Monitor", "precio": 900, "stock": 3},
    {"nombre": "Audifonos", "precio": 250, "stock": 0}
]

for producto in productos:

    if producto["stock"] > 0: 
        producto["Estado"] = "Disponible"
    else: 
        producto["Estado"] = "Agotado"
print(productos)