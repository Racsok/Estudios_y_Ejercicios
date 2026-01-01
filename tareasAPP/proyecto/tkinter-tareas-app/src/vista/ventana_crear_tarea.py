# Interfaz para crear tarea
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class VistaCrearTarea(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear Tarea")
        # self.geometry("300x200")
        
        ttk.Label(self, text="Titulo").pack(pady=5)
        self.titulo = ttk.Entry(self)
        self.titulo.pack(pady=5)

        ttk.Label(self, text="Descripción").pack(pady=5)
        self.descripcion = ttk.Entry(self)
        self.descripcion.pack(pady=5)

        ttk.Label(self, text="Prioridad:", font=("Arial", 10, "bold")).pack(pady=5)
        self.prioridad = tk.IntVar(value=1)
        ttk.Radiobutton(self, text="Alta (1)", variable=self.prioridad, value=1).pack()
        ttk.Radiobutton(self, text="Media (2)", variable=self.prioridad, value=2).pack()
        ttk.Radiobutton(self, text="Baja (3)", variable=self.prioridad, value=3).pack()

        ttk.Label(self, text="Fecha límite:", font=("Arial", 10, "bold")).pack(pady=5)
        self.ent_fecha = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.ent_fecha.pack(pady=5)

        btn_crear = tk.Button(self, text="Crear Tarea", bg="#4CAF50", fg="white", command=self.guardar_datos)
        btn_crear.pack(pady=20)

    def guardar_datos(self):
        try:
            self.data = {
                    "titulo":  self.titulo.get(),
                    "descripcion": self.descripcion.get(),
                    "prioridad": self.prioridad.get(),
                    "ent_fecha":  self.ent_fecha.get_date(), 
                    }
            self.destroy()
        finally:
            pass




