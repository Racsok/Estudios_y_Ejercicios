#interfaz grafica
from control.GestorTareas import GestorTareas
from db.connection import DatabaseConnection
from vista import *
from vista.ventana_principal import Ventana

def main():
    db = DatabaseConnection()
    control = GestorTareas(db)
    ventana = Ventana(control)
    ventana.mainloop() 
   
if __name__ == "__main__":
    main()
