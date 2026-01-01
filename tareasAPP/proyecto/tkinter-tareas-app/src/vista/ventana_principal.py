import tkinter as tk
from tkinter import Canvas, ttk

from vista.ventana_crear_tarea import VistaCrearTarea

class Ventana(tk.Tk):
    def __init__(self, control) -> None:
        super().__init__()
        self.title("Flujo de trabajo")
        self.geometry("400x300")
        self.control = control
        
        # Frame de botones superiores
        frame_menu = ttk.Frame(self, padding=10)
        frame_menu.pack(fill="x") # Usamos pack arriba para separar áreas

        # Frame para botones
        ttk.Button(frame_menu, text="Tareas Pendientes").grid(column=0,row=0)
        ttk.Button(frame_menu, text="Tareas Completadas").grid(column=1, row=0)
        ttk.Button(frame_menu, text="Crear Tarea", command=self.crear_tarea).grid(column=0,row=1, columnspan=2, sticky="ew")

        # canvas y Scrol para las Tarea
        # tareas = Canvas(self)
        # scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=tareas.yview)
        # self.tareas_scroll = ttk.Frame(tareas)

        #Contenedor Tareas
        self.contenedor_tareas = ttk.Frame(self, padding=10)
        self.contenedor_tareas.pack(fill="both", expand= True)

        #primera carga de tareas
        self.mostrar_tareas()


    def crear_tarea(self):
        crear_tarea = VistaCrearTarea(self)
        crear_tarea.grab_set() # bloquea la ventana principal
        self.wait_window(crear_tarea)
        data = crear_tarea.data
        self.control.crear_tarea(data.get("titulo"), data.get("descripcion"), data.get("prioridad"), data.get("ent_fecha"))
        self.mostrar_tareas()

    def mostrar_tareas(self):
        #limpiar widget contenedor
        for widget in self.contenedor_tareas.winfo_children():
            widget.destroy()

        #lista actualizada de tareas
        lista_tareas = self.control.listar_tareas()

        for i, Tarea in enumerate(lista_tareas):
            # Creamos la tarjeta
            tarjeta = ttk.Frame(self.contenedor_tareas, relief="raised", borderwidth=2)
            tarjeta.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")
            
            # Dentro de la tarjeta, puedes usar pack para los labels
            ttk.Label(tarjeta, text=Tarea.titulo, font=("Arial", 10, "bold")).pack()
            ttk.Label(tarjeta, text=Tarea.descripcion).pack()


