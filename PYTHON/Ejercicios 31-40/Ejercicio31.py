"""
Ejercicio 31 — Ahora subimos otro nivel

Vamos a añadir contadores y acumuladores a nuestra lista de diccionarios.

Tenemos:

estudiantes = [
    {"nombre": "Nicolas", "edad": 22, "nota": 85},
    {"nombre": "Juan", "edad": 17, "nota": 92},
    {"nombre": "Maria", "edad": 21, "nota": 65},
    {"nombre": "Pedro", "edad": 19, "nota": 78},
    {"nombre": "Laura", "edad": 16, "nota": 95}
]

Crea:

cantidad_aprobados = 0
cantidad_reprobados = 0
suma_notas = 0

Recorre estudiantes.

Para cada estudiante:

1. Si su nota es >= 70:

cantidad_aprobados += 1

Si no:

cantidad_reprobados += 1

2. Independientemente de si aprobó o reprobó, agrega su nota a:

suma_notas

3. Al terminar el for, calcula:

promedio = suma_notas / cantidad de estudiantes
"""

estudiantes = [
    {"nombre": "Nicolas", "edad": 22, "nota": 85},
    {"nombre": "Juan", "edad": 17, "nota": 92},
    {"nombre": "Maria", "edad": 21, "nota": 65},
    {"nombre": "Pedro", "edad": 19, "nota": 78},
    {"nombre": "Laura", "edad": 16, "nota": 95}
]

cantidad_aprobados = 0
cantidad_reprobados = 0
suma_notas = 0
cantidad_estudiantes=0
for estudiante in estudiantes:
    if estudiante["nota"] >= 70:
        cantidad_aprobados+=1
    elif estudiante["nota"] < 70:
        cantidad_reprobados+=1 
    suma_notas+=estudiante["nota"]
    cantidad_estudiantes+=1
promedio=suma_notas/cantidad_estudiantes
print(cantidad_aprobados)
print(cantidad_reprobados)
print(promedio)