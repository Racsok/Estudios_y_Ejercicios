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
        self.ordenar_tareas()
        return self.tareas_pendientes

    def ordenar_tareas(self):
        self.tareas_pendientes.sort(key=lambda Tarea: Tarea.prioridad)

    def eliminar_tarea(self, Tarea):
        if Tarea in self.tareas_pendientes:
            self.tareas_pendientes.remove(Tarea)
            return True
        return False
    
    def actualizar_tarea(self, Tarea, titulo, descripcion, prioridad, fecha):
        # for tarea in self.tareas_pendientes:
        #     if tarea == Tarea:
        Tarea.titulo = titulo
        Tarea.descripcion = descripcion
        Tarea.prioridad = prioridad
        Tarea.fecha_limite = fecha
        return True
        #     pass

