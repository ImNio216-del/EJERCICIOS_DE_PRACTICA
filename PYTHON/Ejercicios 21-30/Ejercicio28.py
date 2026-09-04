"""
Ejercicio 31 — Analizar estudiantes

Tenemos este diccionario:

estudiante = {
    "nombre": "Nicolas",
    "edad": 22,
    "matematicas": 85,
    "programacion": 95,
    "ingles": 70
}

Recorre el diccionario utilizando:

for clave, valor in estudiante.items():
Debes hacer lo siguiente:

1. Si la clave es "edad":

Si valor >= 18, cambia su valor por "Mayor de edad".
Si valor < 18, cambia su valor por "Menor de edad".

2. Si la clave es una de estas:

matematicas
programacion
ingles

comprueba su nota:

>= 90 → cambia el valor por "Excelente"
>= 70 → cambia el valor por "Aprobado"
< 70 → cambia el valor por "Reprobado"

3. No modifiques "nombre".
"""
estudiante = {
    "nombre": "Nicolas",
    "edad": 22,
    "matematicas": 85,
    "programacion": 95,
    "ingles": 70
}

for clave, valor in estudiante.items():

    if clave == "edad":
        if valor >= 18 : estudiante[clave]="Mayor de edad"
        else: estudiante[clave]="Menor de edad"
    if clave == "matematicas" or clave == "programacion" or clave == "ingles":
        if valor >= 90 : estudiante[clave]="Excelente"
        elif valor >= 70:estudiante[clave]="Aprobado"
        else :estudiante[clave]="Reprobado"

print(estudiante)