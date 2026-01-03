import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, scoped_session

class DatabaseConnection:
    def __init__(self, db_name: str = "Tarea.sqlite"):
        self.bd_url = f"sqlite:///{db_name}"
        try:
            #es el punto de entrada principal para interactuar con una base de datos en Python
            self.engine = create_engine(self.bd_url, connect_args={"check_same_thread": False}) # para SQLite y multihilo
            # Fabricante de Sesiones: Es un objeto que produce instancias de Session. No es la sesión en sí, sino la "fábrica" de donde se obtienen las sesiones.
            self._session_factory = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

            self.Session = scoped_session(self._session_factory)
        except SQLAlchemyError as e:
            print(f"Error al conectar la base de datos: {e}")

    def get_session(self):
        return self.Session

    def crear_tablas(self, Base):
        # Esto es lo que realmente crea el archivo .sqlite si no existe
        Base.metadata.create_all(self.engine)
        
        

        
#         self.db_name = db_name
#         self.connection = None
#
#     def open_connection(self):
#         if self.connection is None:
#             try:
#                 self.connection = sqlite3.connect(self.db_name)
#             except sqlite3.Error as e:
#                 print(f"Error connecting to database: {e}")
#                 raise
#
#     def close_connection(self):
#         if self.connection is not None:
#             self.connection.close()
#             self.connection = None
#
#     def execute_query(self, query, params=()):
#         if self.connection is not None:
#             cursor = self.connection.cursor()
#             cursor.execute(query, params)
#             self.connection.commit()
#             return cursor
#
#     def fetch_all(self, query, params=()):
#         self.open_connection()
#         if self.connection is not None:
#             cursor = self.execute_query(query, params)
#             return cursor.fetchall() # type: ignore
#
#     def fetch_one(self, query, params=()):
#         self.open_connection  
#         if self.connection is not None:  
#             cursor = self.execute_query(query, params)
#             return cursor.fetchone() # type: ignore
