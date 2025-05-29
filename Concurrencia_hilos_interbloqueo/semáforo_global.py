import threading
import time
import random

class Filosofo(threading.Thread):
    def __init__(self, nombre, tenedor_izq, tenedor_der, arbitro):
        super().__init__()
        self.nombre = nombre
        self.tenedor_izq = tenedor_izq
        self.tenedor_der = tenedor_der
        self.arbitro = arbitro

    def run(self):
        while True:
            print(f"{self.nombre} está pensando...")
            time.sleep(random.uniform(1, 3))
            
            print(f"{self.nombre} espera permiso del árbitro...")
            with self.arbitro: # Adquirir permiso del semáforo global
                print(f"{self.nombre} obtuvo permiso del árbitro.")
                print(f"{self.nombre} intenta tomar tenedor izquierdo")
                with self.tenedor_izq:
                    print(f"{self.nombre} tomó tenedor izquierdo")
                    time.sleep(2) # Pequeña pausa
                    print(f"{self.nombre} intenta tomar tenedor derecho")
                    with self.tenedor_der:
                        print(f"{self.nombre} está comiendo...")
                        time.sleep(random.uniform(1, 5))
                        print(f"{self.nombre} terminó de comer (soltó tenedores y permiso del árbitro)\n")
            # El permiso del árbitro se libera automáticamente al salir del bloque 'with self.arbitro'

# --- Configuración para Semáforo Global (Árbitro) ---
print("Iniciando simulación con Semáforo Global (Árbitro)...\n")
NUM_FILOSOFOS = 5
# El árbitro permite que NUM_FILOSOFOS - 1 intenten comer a la vez
arbitro = threading.BoundedSemaphore(NUM_FILOSOFOS - 1) 
tenedores = [threading.Lock() for _ in range(NUM_FILOSOFOS)]
filosofos = []

for i in range(NUM_FILOSOFOS):
    f = Filosofo(f"Filósofo {i+1}", tenedores[i], tenedores[(i + 1) % NUM_FILOSOFOS], arbitro)
    filosofos.append(f)
    f.start()
