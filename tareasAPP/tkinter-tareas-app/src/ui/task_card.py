import tkinter as tk

class TaskCard:
    def __init__(self, master, tarea, on_edit, on_delete):
        self.master = master
        self.tarea = tarea
        self.on_edit = on_edit
        self.on_delete = on_delete
        
        self.frame = self.create_card()
        self.frame.bind("<Button-1>", self.start_move)
        self.frame.bind("<ButtonRelease-1>", self.stop_move)
        self.frame.bind("<B1-Motion>", self.move)

    def create_card(self):
        frame = tk.Frame(self.master, bg=self.get_color(), bd=2, relief=tk.RAISED)
        title_label = tk.Label(frame, text=self.tarea.titulo, bg=self.get_color())
        title_label.pack(padx=10, pady=5)

        edit_button = tk.Button(frame, text="Editar", command=self.edit_task)
        edit_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(frame, text="Eliminar", command=self.delete_task)
        delete_button.pack(side=tk.RIGHT, padx=5)

        frame.pack(padx=10, pady=10, fill=tk.X)
        return frame

    def get_color(self):
        from src.utils.color_utils import get_color
        return get_color(self.tarea.position)

    def edit_task(self):
        self.on_edit(self.tarea)

    def delete_task(self, db):
        self.tarea.eliminar_tarea(db)
        self.frame.destroy()

    def start_move(self, event):
        self.frame.x = event.x
        self.frame.y = event.y

    def stop_move(self, event):
        # Update color based on new position if needed
        self.frame.config(bg=self.get_color())

    def move(self, event):
        dx = event.x - self.frame.x
        dy = event.y - self.frame.y
        x = self.frame.winfo_x() + dx
        y = self.frame.winfo_y() + dy
        self.frame.place(x=x, y=y)