"""
Ejercicio 32 — Analizar estudiantes

Tenemos:

estudiantes = [
    {"nombre": "Nicolas", "edad": 22, "nota": 85},
    {"nombre": "Juan", "edad": 17, "nota": 92},
    {"nombre": "Maria", "edad": 21, "nota": 65},
    {"nombre": "Pedro", "edad": 19, "nota": 78}
]

Recorre la lista utilizando:

for estudiante in estudiantes:

Para cada estudiante:

1. Imprime su nombre
2. Comprueba su nota:
Si nota >= 90 → "Excelente"
Si nota >= 70 → "Aprobado"
Si nota < 70 → "Reprobado"
3. Comprueba su edad:
Si tiene 18 o más → "Mayor de edad"
Si tiene menos de 18 → "Menor de edad"
"""

estudiantes = [
    {"nombre": "Nicolas", "edad": 22, "nota": 85},
    {"nombre": "Juan", "edad": 17, "nota": 92},
    {"nombre": "Maria", "edad": 21, "nota": 65},
    {"nombre": "Pedro", "edad": 19, "nota": 78}
]

for estudiante in estudiantes:
    print(estudiante["nombre"])

    if   estudiante ["nota"] >= 90: estudiante ["nota"]="Excelente"
    elif estudiante ["nota"] >= 70: estudiante ["nota"]="Aprobado"
    else: estudiante ["nota"]="Reprobado"

    if estudiante ["edad"] >= 18: estudiante ["edad"]="Mayor de edad"
    else:estudiante ["edad"]="Menor de edad"

print(estudiantes)