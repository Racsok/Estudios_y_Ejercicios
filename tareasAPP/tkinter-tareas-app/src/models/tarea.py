# definicion de la clase tarea 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Date

Base = declarative_base()
class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True) # Obligatorio: Una llave primaria
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    prioridad = Column(Integer)
    fecha_limite = Column(Date) # O puedes usar Date
    completada = Column(Boolean, default=False)

    def __str__(self):
        try:
            estado = "✅" if self.completada is True else "⏳"
            return f"[{self.prioridad}] {self.titulo} - {estado} (Fin: {self.fecha_limite})"

        except Exception as e:
            raise e

