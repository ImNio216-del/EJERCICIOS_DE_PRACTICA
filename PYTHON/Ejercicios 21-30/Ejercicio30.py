"""
Ejercicio 30 — Ahora vamos a hacerlo más interesante
Esta vez no quiero que modifiques los estudiantes.
Tenemos:
estudiantes = [
    {"nombre": "Nicolas", "edad": 22, "nota": 85},
    {"nombre": "Juan", "edad": 17, "nota": 92},
    {"nombre": "Maria", "edad": 21, "nota": 65},
    {"nombre": "Pedro", "edad": 19, "nota": 78},
    {"nombre": "Laura", "edad": 16, "nota": 95}
]
Crea estas listas:

aprobados = []
mayores_de_edad = []
excelentes = []
Recorre estudiantes.
Debes guardar:

En aprobados:

Los estudiantes cuya nota sea >= 70.

En mayores_de_edad:

Los estudiantes cuya edad sea >= 18.

En excelentes:

Los estudiantes cuya nota sea >= 90.

Pero esta vez quiero que guardes el nombre, no todo el diccionario.
"""

estudiantes = [
    {"nombre": "Nicolas", "edad": 22, "nota": 85},
    {"nombre": "Juan", "edad": 17, "nota": 92},
    {"nombre": "Maria", "edad": 21, "nota": 65},
    {"nombre": "Pedro", "edad": 19, "nota": 78},
    {"nombre": "Laura", "edad": 16, "nota": 95}
]

aprobados = []
mayores_de_edad = []
excelentes = []

for estudiante in estudiantes:
    if estudiante["nota"] >= 70:
        aprobados.append(estudiante["nombre"])
    if estudiante["edad"] >= 18:
        mayores_de_edad.append(estudiante["nombre"])
    if estudiante["nota"] >= 90:
        excelentes.append(estudiante["nombre"])
    

print(aprobados)
print(mayores_de_edad)
print(excelentes)