# esta es la clase que gestiona las tareas
from models.tarea import Tarea


class GestorTareas:
    def __init__(self) -> None:
        self.tareas_pendientes = []

    def crear_tarea(self, titulo, descripcion, prioridad, fecha):
        nueva_tarea = Tarea(titulo, descripcion, prioridad, fecha) 
        self.tareas_pendientes.append(nueva_tarea)
        print("Tarea creada con exito")

    def listar_tareas(self):
        for Tarea in self.tareas_pendientes:
            print(Tarea)
