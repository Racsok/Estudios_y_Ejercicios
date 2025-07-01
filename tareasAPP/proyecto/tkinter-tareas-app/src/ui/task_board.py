from tkinter import Frame, Canvas, Scrollbar, Button, simpledialog
from tkinter import messagebox
from .task_card import TaskCard
from ..models.tarea import Tarea

class TaskBoard(Frame):
    def __init__(self, master, db_connection, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.pack()
        
        # --- Menú superior ---
        self.menu_frame = Frame(self)
        self.menu_frame.pack(fill="x")
        add_btn = Button(self.menu_frame, text="Agregar tarea", command=self.add_task_dialog)
        add_btn.pack(side="left", padx=5, pady=5)

        
        # Área de trabajo con desplazamiento
        self.canvas = Canvas(self)
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.tasks = []
        self.db_connection = db_connection
        self.load_tasks()

    def load_tasks(self):
        tasks_data = self.db_connection.fetch_all("SELECT * FROM tasks")
        for task in tasks_data:
            id, titulo, position = task
            tarea = Tarea(id, titulo, position)
            self.add_task(tarea)

    def add_task(self, task_data):
        task_card = TaskCard(self.scrollable_frame, task_data, self.update_task_color, self.remove_task)
        self.tasks.append(task_card)

    def add_task_dialog(self):
        titulo = simpledialog.askstring("Nueva tarea", "Título de la tarea:")
        if titulo:
            # Puedes agregar más campos si lo deseas
            importancia = simpledialog.askinteger("Importancia", "Importancia (1=Alta, 4=Baja):", minvalue=1, maxvalue=4)
            if importancia:
                # Guardar en la base de datos
                tarea = Tarea(None, titulo, importancia)
                self.add_task(tarea)
                # Recargar tareas
                self.reload_tasks()
    
    def reload_tasks(self):
        # Elimina las tareas actuales del frame y recarga desde la BD
        for task_card in self.tasks:
            task_card.delete_task(self.db_connection)
        self.tasks.clear()
        self.load_tasks()
    
    def update_task_color(self, task_card):
        importance = task_card.task_data['importancia']
        color = self.get_color(importance)
        task_card.configure(bg=color)

    def get_color(self, importance):
        if importance == 1:
            return "red"
        elif importance == 2:
            return "orange"
        elif importance == 3:
            return "yellow"
        else:
            return "green"

    def remove_task(self, task_card):
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar esta tarea?"):
            task_card.delete_task()
            #self.tasks.remove(task_card)
            #self.db_connection.delete_task(task_card.task_data['id'])