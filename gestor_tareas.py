import json
import os

ARCHIVO_TAREAS = "tareas.json"


def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        try:
            with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []


def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, ensure_ascii=False, indent=4)


def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def ver_tareas(tareas):
    if not tareas:
        print("\nNo hay tareas registradas.")
        return

    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['nombre']} - {estado}")


def agregar_tarea(tareas):
    nombre = input("\nIngrese el nombre de la tarea: ").strip()

    if nombre == "":
        print("No se puede agregar una tarea vacía.")
        return

    nueva_tarea = {
        "nombre": nombre,
        "completada": False
    }

    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print("Tarea agregada correctamente.")


def completar_tarea(tareas):
    ver_tareas(tareas)

    if not tareas:
        return

    try:
        numero = int(input("\nIngrese el número de la tarea a completar: "))
        if 1 <= numero <= len(tareas):
            if tareas[numero - 1]["completada"]:
                print("Esa tarea ya estaba completada.")
            else:
                tareas[numero - 1]["completada"] = True
                guardar_tareas(tareas)
                print("Tarea marcada como completada.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Debe ingresar un número válido.")


def eliminar_tarea(tareas):
    ver_tareas(tareas)

    if not tareas:
        return

    try:
        numero = int(input("\nIngrese el número de la tarea a eliminar: "))
        if 1 <= numero <= len(tareas):
            tarea_eliminada = tareas.pop(numero - 1)
            guardar_tareas(tareas)
            print(f"Tarea eliminada: {tarea_eliminada['nombre']}")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Debe ingresar un número válido.")


def main():
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            ver_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()