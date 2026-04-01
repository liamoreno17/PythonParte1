import os

escuela, niveles = "Academia Python", ("Básico", "Intermedio", "Avanzado")
alumnos = [
    {"nombre": "Lía", "notas": [8, 9, 10], "nivel": niveles[1]},
    {"nombre": "Marcos", "notas": [4, 5, 6], "nivel": niveles[0]}
]

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print(f"--- {escuela.upper()} ---\n1. Ver alumnos\n2. Registrar\n3. Salir")
    op = input("\nElige: ")

    if op == "1":
        clear()
        for a in alumnos:
            prom = sum(a["notas"]) / len(a["notas"])
            est = "Aprobado" if prom >= 6 else "Reprobado"
            print(f"{a['nombre']} ({a['nivel']}) - Prom: {prom:.1f} [{est}]")
        input("\nEnter para volver...")

    elif op == "2":
        clear()
        nom = input("Nombre: ")
        nts = [float(input(f"Nota {i+1}: ")) for i in range(3)]
        print("0:Básico, 1:Intermedio, 2:Avanzado")
        idx = int(input("Nivel (0-2): "))
        alumnos.append({"nombre": nom, "notas": nts, "nivel": niveles[idx]})
        input("\nRegistrado. Enter...")

    elif op == "3":
        print("Chao!"); break
    else:
        input("Error. Enter...")