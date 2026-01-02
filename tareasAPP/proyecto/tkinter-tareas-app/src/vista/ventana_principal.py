import tkinter as tk
from tkinter import ttk

from vista.ventana_crear_tarea import VistaCrearTarea
from vista.ventana_tarea import VistaTarea

class Ventana(tk.Tk):
    def __init__(self, control) -> None:
        super().__init__()
        self.title("Flujo de trabajo")
        self.geometry("500x500")
        self.configure(bg="#f0f0f0")
        self.control = control
        
        # Estilo para botones y etiquetas
        style = ttk.Style()
        style.configure("Card.TFrame", background="white", relief="flat")

        # Frame de botones superiores
        frame_menu = tk.Frame(self, bg="#ffffff", borderwidth=1, relief="groove", pady=15, padx=15)
        frame_menu.pack(fill="x")

        # Frame para botones
        ttk.Button(frame_menu, text="Pendientes").grid(column=0, row=0, padx=5)
        ttk.Button(frame_menu, text="Completadas").grid(column=1, row=0, padx=5)
        ttk.Button(frame_menu, text="+ Nueva Tarea", command=self.crear_tarea).grid(column=2, row=0, padx=20)

        #Contenedor Tareas
        self.contenedor_tareas = tk.Frame(self, bg="#f0f0f0", padx=10, pady=10)
        self.contenedor_tareas.pack(fill="both", expand=True)

        #primera carga de tareas
        self.mostrar_tareas()


    def crear_tarea(self):
        crear_tarea = VistaCrearTarea(self)
        crear_tarea.grab_set() # bloquea la ventana principal
        self.wait_window(crear_tarea)
        data = crear_tarea.data
        self.control.crear_tarea(data.get("titulo"), data.get("descripcion"), data.get("prioridad"), data.get("ent_fecha"))
        self.mostrar_tareas()

    def ver_tarea(self, Tarea):
        ventana_tarea = VistaTarea(self, Tarea)
        ventana_tarea.update_idletasks() # pide esperar a que termine de cargar la ventana
        ventana_tarea.grab_set()
        self.wait_window(ventana_tarea)
        cambio = False
        if ventana_tarea.data != None and ventana_tarea.data.get("evento") == "eliminar":
            tarea = ventana_tarea.data.get("tarea")
            cambio = self.control.eliminar_tarea(tarea)
        
        if ventana_tarea.data != None and ventana_tarea.data.get("evento") == "actualizar":
            data = ventana_tarea.data
            cambio = self.control.actualizar_tarea(data.get("tarea"), data.get("titulo"), data.get("descripcion"), data.get("prioridad"), data.get("ent_fecha"))

        if cambio:
            self.mostrar_tareas()
        
    def mostrar_tareas(self):
        #limpiar widget contenedor
        for widget in self.contenedor_tareas.winfo_children():
            widget.destroy()

        #lista actualizada de tareas
        lista_tareas = self.control.listar_tareas()

        for i, Tarea in enumerate(lista_tareas):
            # Creamos la tarjeta
            tarjeta = tk.Frame(self.contenedor_tareas, bg="white", highlightbackground="#e0e0e0", highlightthickness=1, bd=0, padx=15, pady=15)
            tarjeta.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")
            
            # Dentro de la tarjeta
            tk.Label(tarjeta, text=Tarea.titulo.upper(), font=("Arial", 9, "bold"), bg="white", fg="#333333").pack(anchor="w")
            tk.Label(tarjeta, text=Tarea.descripcion, font=("Arial", 8), bg="white", fg="#666666", wraplength=150, justify="left").pack(anchor="w", pady=(5, 0))

            # agregar funcionalidad con bind para click
            for hijo in tarjeta.winfo_children():
                hijo.bind("<Button-1>", lambda _, tarea=Tarea, t=tarjeta: self.ver_tarea(tarea))
            #agreagr resaltado Usamos t=tarjeta para "congelar" la variable en el lambda
            tarjeta.bind("<Button-1>", lambda _, tarea=Tarea, t=tarjeta: self.ver_tarea(tarea))
            tarjeta.bind('<Enter>', lambda _, t=tarjeta: t.config(bg='#f9f9f9'))
            tarjeta.bind('<Leave>', lambda _, t=tarjeta: t.config(bg="white"))


#             # Prioridad visual (Badge)
#             color_prio = {1: "#ffcccc", 2: "#fff4cc", 3: "#ccffcc"}.get(Tarea.prioridad, "#eeeeee")
#             lbl_prio = tk.Label(tarjeta, text=f"Prio: {Tarea.prioridad}", font=("Arial", 7, "bold"), bg=color_prio, padx=5)
#             lbl_prio.pack(anchor="e", pady=(10, 0))
#
