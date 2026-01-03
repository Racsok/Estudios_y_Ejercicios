import tkinter as tk 
from tkinter import ttk

from tkcalendar import DateEntry

class VistaTarea(tk.Toplevel):
    def __init__(self, parent, Tarea):
        super().__init__(parent)
        self.title("Tarea")
        self.configure(padx=20, pady=20)
        self.tarea = Tarea
        self.data = None

        # --- TÍTULO ---
        ttk.Label(self, text="Título de la Tarea", font=("Arial", 10, "bold")).pack(anchor="w")
        self.titulo = tk.Entry(self, font=("Arial", 11))
        self.titulo.insert(0, self.tarea.titulo)
        self.titulo.pack(fill="x", pady=(0, 15))

        # --- DESCRIPCIÓN ---
        ttk.Label(self, text="Descripción", font=("Arial", 10, "bold")).pack(anchor="w")
        self.descripcion = tk.Text(self, height=5, font=("Arial", 11))
        self.descripcion.insert("1.0", self.tarea.descripcion)
        self.descripcion.pack(fill="x", pady=(0, 15))

        # --- FILA PARA PRIORIDAD Y FECHA ---
        meta_frame = ttk.Frame(self)
        meta_frame.pack(fill="x", pady=(0, 20))

        # Prioridad
        prioridad_frame = ttk.Frame(meta_frame)
        prioridad_frame.pack(side="left", fill="x", expand=True)
        ttk.Label(prioridad_frame, text="Prioridad", font=("Arial", 10, "bold")).pack(anchor="w")
        self.prioridad = ttk.Combobox(prioridad_frame, values=["Baja", "Media", "Alta"], state="readonly")
        self.prioridad.set(self.tarea.prioridad)
        self.prioridad.pack(anchor="w", padx=(0, 10))

        # Fecha Límite
        fecha_frame = ttk.Frame(meta_frame)
        fecha_frame.pack(side="left", fill="x", expand=True)
        ttk.Label(fecha_frame, text="Fecha Límite", font=("Arial", 10, "bold")).pack(anchor="w")
        self.ent_fecha = DateEntry(fecha_frame)
        self.ent_fecha.insert(0, self.tarea.fecha_limite)
        self.ent_fecha.pack(anchor="w")

        # --- BOTONES DE ACCIÓN ---
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", side="bottom", pady=10)
        if not self.tarea.completada:

            # Botón Eliminar (Rojo)
            self.btn_eliminar = tk.Button(btn_frame, text="Eliminar", command=self.eliminar, bg="#ff4d4d", fg="white", relief="flat", padx=10, pady=5)
            self.btn_eliminar.pack(side="left")

            # Botón Cerrar (Gris)
            self.btn_cerrar = tk.Button(btn_frame, text="Cerrar", command=self.destroy, relief="flat", padx=10, pady=5)
            self.btn_cerrar.pack(side="right", padx=5)

            # Botón Actualizar (Azul/Principal)
            self.btn_actualizar = tk.Button(btn_frame, text="Actualizar Tarea", command=self.actualizar, bg="#2196F3", fg="white", font=("Arial", 10, "bold"), relief="flat", padx=15, pady=5)
            self.btn_actualizar.pack(side="right", padx=5)
            
            # Botón Completar (Verde)
            self.btn_completar = tk.Button(btn_frame, text="Completar Tarea", command=self.completar, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="flat", padx=15, pady=5)
            self.btn_completar.pack(side="right", padx=5)
        else:
            # Botón Cerrar (Gris)
            self.btn_cerrar = tk.Button(btn_frame, text="Cerrar", command=self.destroy, relief="flat", padx=10, pady=5)
            self.btn_cerrar.pack(side="right", padx=5)

            # Botón Descompletar (Verde)
            self.btn_completar = tk.Button(btn_frame, text="Descompletar Tarea", command=self.completar, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="flat", padx=15, pady=5)
            self.btn_completar.pack(side="right", padx=5)


    def eliminar(self):
        self.data = {
                "tarea": self.tarea,
                "evento": "eliminar"
                }
        self.destroy()
    
    def actualizar(self):
        t = self.tarea
        try:
            self.data = {
                    "tarea": self.tarea,
                    "titulo":  self.titulo.get(),
                    "descripcion": self.descripcion.get("1.0", "end-1c"),
                    "prioridad": self.prioridad.get(),
                    "ent_fecha":  self.ent_fecha.get_date(),
                    "evento": "actualizar"
                    }
            if t.titulo != self.data.get("titulo") or t.descripcion != self.data.get("descripcion") or t.prioridad != self.data.get("prioridad") or t.fecha_limite != self.data.get("ent_fecha"):
                self.destroy()
        finally:
            pass
    
    def completar(self):
        self.data = {
                "tarea": self.tarea,
                "evento": "alternar_estado"
                }
        self.destroy()



