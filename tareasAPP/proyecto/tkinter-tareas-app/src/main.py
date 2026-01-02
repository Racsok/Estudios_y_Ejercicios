#interfaz grafica
from control.GestorTareas import GestorTareas
from vista import *
from vista.ventana_principal import Ventana

def main():
    control = GestorTareas()
    ventana = Ventana(control)
    ventana.mainloop() 
   
if __name__ == "__main__":
    main()
