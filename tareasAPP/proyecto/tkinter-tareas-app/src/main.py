import sys
import os
main_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(main_dir, '..')
print("Parent directory:", parent_dir)
sys.path.append(parent_dir)

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../instance/Tarea.db'))

import tkinter as tk
from tkinter import messagebox
from db.connection import DatabaseConnection
from src.ui.task_board import TaskBoard



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("800x600")

        self.db =  DatabaseConnection(db_path)
        self.task_board = TaskBoard(self.root, self.db)
        self.task_board.pack(fill=tk.BOTH, expand=True)

    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Quieres salir de la aplicación?"):
            print("Closing the application...")
            self.db.close_connection()
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()