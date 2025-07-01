class Tarea:
    def __init__(self, id, titulo, position):
        self.id = id
        self.titulo = titulo
        #self.descripcion = descripcion
        self.position = position

    def crear_tarea(self, conexion):
        query = "INSERT INTO task (titulo, descripcion, importancia) VALUES (?, ?, ?)"
        conexion.execute_query(query, (self.titulo,  self.position))

    def editar_tarea(self, conexion):
        query = "UPDATE tasks SET titulo = ?, descripcion = ?, importancia = ? WHERE id = ?"
        conexion.execute_query(query, (self.titulo,  self.position, self.id))

    def eliminar_tarea(self, conexion):
        query = "DELETE FROM tasks WHERE id = ?"
        conexion.open_connection()
        conexion.execute_query(query, (self.id,))
        conexion.close_connection()

    @staticmethod
    def obtener_tareas(conexion):
        query = "SELECT * FROM tareas"
        return query