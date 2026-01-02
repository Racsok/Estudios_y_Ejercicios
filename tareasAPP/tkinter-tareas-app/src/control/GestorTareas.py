# esta es la clase que gestiona las tareas
from models.tarea import Tarea

class GestorTareas:
    def __init__(self, db) -> None:
        self.db = db
        self.db.crear_tablas(Tarea)
        self.session = self.db.get_session()
        
        self.tareas_pendientes = []
        self.tareas_completadas = []

        self.cargar_desde_db()

    def crear_tarea(self, titulo, descripcion, prioridad, fecha):
        try:
            nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion, prioridad=prioridad, fecha_limite=fecha) 
            #agregar a la lista
            self.tareas_pendientes.append(nueva_tarea) 
            
            #agregar a la BD
            self.session.add(nueva_tarea)
            self.session.commit()
        except Exception as e:
            print(f"GestorTareas.crear_tarea: {e}")
            raise e 

    def listar_tareas(self, tupla):
        self.ordenar_tareas()
        return self.tareas_pendientes if tupla == () else self.tareas_completadas
        # return self.tareas_completadas if tupla == () else self.tareas_pendientes

    def ordenar_tareas(self):
        self.tareas_pendientes.sort(key=lambda Tarea: Tarea.prioridad)
        self.tareas_completadas.sort(key=lambda Tarea: Tarea.prioridad)

    def eliminar_tarea(self, tarea_obj):
        if tarea_obj in self.tareas_pendientes:
            #eliminar de la lista
            self.tareas_pendientes.remove(tarea_obj)

            #eliminar de la BD
            self.session.delete(tarea_obj)
            self.session.commit()
            return True
        return False
    
    def actualizar_tarea(self, tarea_obj, titulo, descripcion, prioridad, fecha):
        tarea_obj.titulo = titulo
        tarea_obj.descripcion = descripcion
        tarea_obj.prioridad = prioridad
        tarea_obj.fecha_limite = fecha
        return True

    def completar_tarea(self, tarea_obj):
        tarea_obj.completada = True
        self.tareas_pendientes.remove(tarea_obj)
        self.tareas_completadas.append(tarea_obj)
        return True

    def cargar_desde_db(self):
        todas = self.session.query(Tarea).all()
        self.tareas_pendientes = [t for t in todas if not t.completada]
        self.tareas_completadas = [t for t in todas if t.completada]

