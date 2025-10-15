# =================== DATOS INICIALES ===================
mis_asignaturas = []
mis_notas = []

historial = []
solicitudes = []  # Solo simulación

# =================== MENÚ ===================
def menu():
    print("""
***** GESTOR DE NOTAS SIMPLE *****
1. Agregar asignatura
2. Listar asignaturas
3. Calcular promedio
4. Aprobadas / Reprobadas
5. Buscar asignatura
6. Cambiar nota
7. Borrar asignatura
8. Ordenar por nota
9. Ordenar por nombre
10. Búsqueda binaria
11. Simular solicitudes
12. Ver historial
13. Salir
*********************************
""")

# =================== FUNCIONES ===================

# 1 Registrar un curso
def agregar_asignatura():
    nombre = input("Nombre de la asignatura: ").strip()
    if nombre in mis_asignaturas:
        print("Ya existe esa asignatura.")
        return
    try:
        nota = float(input("Nota: "))
        if 0 <= nota <= 100:
            mis_asignaturas.append(nombre)
            mis_notas.append(nota)
            print(f"{nombre} agregada con nota {nota}.")
        else:
            print("Nota inválida.")
    except:
        print("Número inválido.")

# 2 Mostrar
def listar_asignaturas():
    if not mis_asignaturas:
        print("No hay cursos ni notas registradas.")
        return
    print("\n--- LISTA DE ASIGNATURAS ---")
    for a, n in zip(mis_asignaturas, mis_notas):
        print(f"{a} -> {n}")
    print("-----------------------------")

# 3 Promedio
def promedio():
    if not mis_notas:
        print("No hay cursos ni notas registradas.")
        return
    prom = sum(mis_notas)/len(mis_notas)
    print(f"Promedio: {prom:.2f}")

# 4 Aprobadas/Reprobadas
def aprobadas_reprobadas():
    if not mis_asignaturas:
        print("No hay cursos ni notas registradas.")
        return
    aprob = [a for a,n in zip(mis_asignaturas, mis_notas) if n>=61]
    repro = [a for a,n in zip(mis_asignaturas, mis_notas) if n<61]
    print("Aprobadas:", aprob or "Ninguna")
    print("Reprobadas:", repro or "Ninguna")

# 5 Buscar lineal
def buscar_asignatura():
    if not mis_asignaturas:
        print("No hay cursos registrados.")
        return
    nombre = input("Asignatura a buscar: ").strip()
    if nombre in mis_asignaturas:
        idx = mis_asignaturas.index(nombre)
        estado = "Aprobada" if mis_notas[idx]>=61 else "Reprobada"
        print(f"{nombre} -> {mis_notas[idx]} ({estado})")
    else:
        print("No encontrada.")

# 6 Cambiar nota
def cambiar_nota():
    if not mis_asignaturas:
        print("No hay cursos registrados.")
        return
    nombre = input("Asignatura: ").strip()
    if nombre in mis_asignaturas:
        idx = mis_asignaturas.index(nombre)
        print(f"Nota actual: {mis_notas[idx]}")
        try:
            nueva = float(input("Nueva nota: "))
            if 0 <= nueva <= 100:
                historial.append(f"{nombre}: {mis_notas[idx]} -> {nueva}")
                mis_notas[idx] = nueva
                print("Nota actualizada.")
            else:
                print("Nota inválida.")
        except:
            print("Número inválido.")
    else:
        print("Asignatura no encontrada.")

# 7 Borrar
def borrar_asignatura():
    if not mis_asignaturas:
        print("No hay cursos registrados.")
        return
    nombre = input("Asignatura a borrar: ").strip()
    if nombre in mis_asignaturas:
        idx = mis_asignaturas.index(nombre)
        mis_asignaturas.pop(idx)
        mis_notas.pop(idx)
        print(f"{nombre} eliminada.")
    else:
        print("No encontrada.")

# 8 Ordenar por nota (burbuja)
def ordenar_por_nota():
    if not mis_asignaturas:
        print("No hay cursos ni notas registradas.")
        return
    n = len(mis_notas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if mis_notas[j] > mis_notas[j + 1]:
                mis_notas[j], mis_notas[j + 1] = mis_notas[j + 1], mis_notas[j]
                mis_asignaturas[j], mis_asignaturas[j + 1] = mis_asignaturas[j + 1], mis_asignaturas[j]
    print("\nAsignaturas ordenadas por nota (menor a mayor):")
    listar_asignaturas()

# 9 Ordenar por nombre (burbuja)
def ordenar_por_nombre():
    if not mis_asignaturas:
        print("No hay cursos ni notas registradas.")
        return
    n = len(mis_asignaturas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if mis_asignaturas[j].lower() > mis_asignaturas[j + 1].lower():
                mis_asignaturas[j], mis_asignaturas[j + 1] = mis_asignaturas[j + 1], mis_asignaturas[j]
                mis_notas[j], mis_notas[j + 1] = mis_notas[j + 1], mis_notas[j]
    print("\nAsignaturas ordenadas alfabéticamente:")
    listar_asignaturas()

# 10 Búsqueda binaria
def buscar_binaria():
    if not mis_asignaturas:
        print("No hay cursos registrados.")
        return
    ordenar_por_nombre()
    nombre = input("Asignatura a buscar: ").strip()
    izq, der = 0, len(mis_asignaturas)-1
    while izq <= der:
        medio = (izq + der) // 2
        if mis_asignaturas[medio].lower() == nombre.lower():
            print(f"Encontrada: {mis_asignaturas[medio]} -> {mis_notas[medio]}")
            return
        elif nombre.lower() < mis_asignaturas[medio].lower():
            der = medio - 1
        else:
            izq = medio + 1
    print("No encontrada.")

# 11 Simular solicitudes
def simular_solicitudes():
    nombre = input("Asignatura solicitada: ").strip()
    solicitudes.append(nombre)
    print("Solicitud simulada:", solicitudes)

# 12 Mostrar historial
def ver_historial():
    if not historial:
        print("Historial vacío.")
        return
    for h in reversed(historial):
        print(h)

# =================== EJECUTAR OPCIONES ===================
opciones = {
    1: agregar_asignatura,
    2: listar_asignaturas,
    3: promedio,
    4: aprobadas_reprobadas,
    5: buscar_asignatura,
    6: cambiar_nota,
    7: borrar_asignatura,
    8: ordenar_por_nota,
    9: ordenar_por_nombre,
    10: buscar_binaria,
    11: simular_solicitudes,
    12: ver_historial,
    13: lambda: False
}

# =================== BUCLE PRINCIPAL ===================
while True:
    menu()
    try:
        op = int(input("Elija opción: "))
        if op in opciones:
            if opciones[op]() == False:
                print("Saliendo del programa...")
                break
        else:
            print("Opción inválida")
    except:
        print("Número inválido")
