

from control.GestorTareas import GestorTareas


def main():
    gestor = GestorTareas()
    
    while True:
        print("\n--- FLUJO DE PRIORIDAD ---")
        print("1. Crear Tarea")
        print("2. Ver Tareas Pendientes")
        # print("3. Completar Tarea")
        # print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            desc = input("Descripción: ")
            prio = int(input("Prioridad (1-Alta, 3-Baja): "))
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            gestor.crear_tarea(titulo, desc, prio, fecha) 

        elif opcion == "2":
            print("\nLISTA DE PENDIENTES:")
            for i, t in enumerate(gestor.tareas_pendientes):
                print(f"{i}. {t}")
        #
        # elif opcion == "3":
        #     idx = int(input("Índice de la tarea a completar: "))
        #     #gestor.completar_tarea(idx)
        #
        elif opcion == "4":
            break

if __name__ == "__main__":
    main()
