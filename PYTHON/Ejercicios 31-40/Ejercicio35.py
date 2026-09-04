"""
Ejercicio 39 — Sistema de inventario

Tenemos:

productos = [
    {"nombre": "Laptop", "precio": 3000, "stock": 5},
    {"nombre": "Mouse", "precio": 80, "stock": 20},
    {"nombre": "Teclado", "precio": 150, "stock": 0},
    {"nombre": "Monitor", "precio": 900, "stock": 3},
    {"nombre": "Audifonos", "precio": 250, "stock": 0},
    {"nombre": "Celular", "precio": 1800, "stock": 8}
]

Crea:

disponibles = []
agotados = []

valor_inventario = 0
cantidad_disponibles = 0
cantidad_agotados = 0

Recorre todos los productos.

Para cada producto:

Si tiene stock:

Agrégalo a disponibles.
Aumenta cantidad_disponibles.
Calcula el valor que representa ese producto en el inventario:
precio × stock

y súmalo a valor_inventario.

Si está agotado:

Agrégalo a agotados.
Aumenta cantidad_agotados.
Pero hay una condición adicional 

A cada producto debes agregarle una nueva clave:

"valor_total"

Su valor debe ser:

precio × stock

Por ejemplo:

{"nombre": "Laptop", "precio": 3000, "stock": 5}

se convierte en:

{"nombre": "Laptop", "precio": 3000, "stock": 5, "valor_total": 15000}

Incluso los agotados tendrán:

"valor_total": 0
Al final debes imprimir:
Productos disponibles: ...
Productos agotados: ...

Cantidad disponibles: ...
Cantidad agotados: ...

Valor total del inventario: ...
"""


productos = [
    {"nombre": "Laptop", "precio": 3000, "stock": 5},
    {"nombre": "Mouse", "precio": 80, "stock": 20},
    {"nombre": "Teclado", "precio": 150, "stock": 0},
    {"nombre": "Monitor", "precio": 900, "stock": 3},
    {"nombre": "Audifonos", "precio": 250, "stock": 0},
    {"nombre": "Celular", "precio": 1800, "stock": 8}
]

disponibles = []
agotados = []

valor_inventario = 0
cantidad_disponibles = 0
cantidad_agotados = 0
productos["Valor Total"] = 0
for producto in productos:
    if producto["stock"] > 0:
        producto["Estado"] = "Disponible"
        while producto["stock"]>0:
            valor_inventario+=producto["precio"]
            
            producto["Valor Total"]+= producto["precio"]
            producto["stock"]-=1
        cantidad_disponibles+=1

    elif producto["stock"] == 0:
        cantidad_agotados+=1
        producto["Valor Total"]+= producto["precio"]
print(productos)
print("------------------------------")
print("------------------------------")
print(valor_inventario)
print(cantidad_disponibles)
print(cantidad_agotados)