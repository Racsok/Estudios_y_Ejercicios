# definicion de la clase tarea
from datetime import datetime as dt

class Tarea:
    def __init__(self, titulo, descripcion, prioridad, fecha_limite) -> None:
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_limite = fecha_limite
        self.completada = False

    def __str__(self):
        estado = "✅" if self.completada else "⏳"
        return f"[{self.prioridad}] {self.titulo} - {estado} (Fin: {self.fecha_limite})"

