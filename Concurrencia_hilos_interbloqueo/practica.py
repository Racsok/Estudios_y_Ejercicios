import threading
import time
import queue

# Cola compartida entre hilos
tareas = queue.Queue()

# Función que simula trabajo concurrente
def trabajador(id):
    while not tareas.empty():
        tarea = tareas.get()
        print(f"Hilo {id} procesando: {tarea}")
        time.sleep(1)
        tareas.task_done()

# Llenamos la cola con tareas
for i in range(10):
    tareas.put(f"Tarea {i}")
    
# Creamos y lanzamos hilos
hilos = []
for i in range(4): # Tres hilos trabajadores
    t = threading.Thread(target=trabajador, args=(i,))
    t.start()
    hilos.append(t)
    
# Esperamos a que terminen todas las tareas
for h in hilos:
    h.join()
    
print("Todas las tareas han sido procesadas.")