#interfaz grafica
# from tkinter import Tk
# from tkinter import ttk
from control.GestorTareas import GestorTareas
from vista import *
from vista.ventana_principal import Ventana
from vista import ventana_crear_tarea   

def main():
    control = GestorTareas()
    ventana = Ventana(control)
    ventana.mainloop() 
   
if __name__ == "__main__":
    main()
