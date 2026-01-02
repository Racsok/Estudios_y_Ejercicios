# esta es la clase que gestiona las tareas
from models.tarea import Tarea


class GestorTareas:
    def __init__(self) -> None:
        self.tareas_pendientes = []
        self.tareas_completadas = []

    def crear_tarea(self, titulo, descripcion, prioridad, fecha):
        nueva_tarea = Tarea(titulo, descripcion, prioridad, fecha) 
        self.tareas_pendientes.append(nueva_tarea)
        print("Tarea creada con exito")

    def listar_tareas(self, tupla):
        self.ordenar_tareas()
        if tupla == ():
            return self.tareas_pendientes
        return self.tareas_completadas

    def ordenar_tareas(self):
        self.tareas_pendientes.sort(key=lambda Tarea: Tarea.prioridad)
        self.tareas_completadas.sort(key=lambda Tarea: Tarea.prioridad)

    def eliminar_tarea(self, Tarea):
        if Tarea in self.tareas_pendientes:
            self.tareas_pendientes.remove(Tarea)
            return True
        return False
    
    def actualizar_tarea(self, Tarea, titulo, descripcion, prioridad, fecha):
        Tarea.titulo = titulo
        Tarea.descripcion = descripcion
        Tarea.prioridad = prioridad
        Tarea.fecha_limite = fecha
        return True

    def completar_tarea(self, Tarea):
        Tarea.completada = True
        self.tareas_pendientes.remove(Tarea)
        self.tareas_completadas.append(Tarea)
        return True

