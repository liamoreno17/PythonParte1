# Lista doble: [nombre, habilidad, horas disponibles]

estudiantes = [

    ["Ana", "decoración", 5],

    ["Luis", "logística", 3],

    ["María", "comunicación", 6],

    ["Pedro", "decoración", 2],

    ["Sofía", "logística", 4]

]
 
# Diccionario de tareas

tareas = {

    "decoración": [],

    "logística": [],

    "comunicación": []

}
 
# Asignación de tareas según habilidad y horas

for nombre, habilidad, horas in estudiantes:

    # Solo asignar si tiene al menos 3 horas disponibles

    if horas >= 3 and habilidad in tareas:

        tareas[habilidad].append(nombre)
 
# Mostrar resultados

print("=== ASIGNACIÓN DE TAREAS ===\n")
 
for tarea, lista in tareas.items():

    print(f"Tarea: {tarea}")

    if len(lista) > 0:

        for persona in lista:

            print(f" - {persona}")

    else:

        print(" - No hay asignados")

    print()
