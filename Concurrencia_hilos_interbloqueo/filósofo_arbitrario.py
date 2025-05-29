import threading
import time
import random

class Filosofo(threading.Thread):
    def __init__(self, nombre, tenedor_izq, tenedor_der, es_arbitrario=False):
        super().__init__()
        self.nombre = nombre
        self.tenedor_izq = tenedor_izq
        self.tenedor_der = tenedor_der
        self.es_arbitrario = es_arbitrario

    def run(self):
        while True:
            print(f"{self.nombre} está pensando...")
            time.sleep(random.uniform(1, 3))

            if self.es_arbitrario:
                print(f"{self.nombre} (arbitrario) intenta tomar tenedor derecho")
                with self.tenedor_der:
                    print(f"{self.nombre} (arbitrario) tomó tenedor derecho")
                    time.sleep(2) # Pequeña pausa
                    print(f"{self.nombre} (arbitrario) intenta tomar tenedor izquierdo")
                    with self.tenedor_izq:
                        print(f"{self.nombre} (arbitrario) está comiendo...")
                        time.sleep(random.uniform(1, 5))
                        print(f"{self.nombre} (arbitrario) terminó de comer (soltó tenedor izquierdo y derecho)\n")
            else:
                print(f"{self.nombre} intenta tomar tenedor izquierdo")
                with self.tenedor_izq:
                    print(f"{self.nombre} tomó tenedor izquierdo")
                    time.sleep(0.1) # Pequeña pausa
                    print(f"{self.nombre} intenta tomar tenedor derecho")
                    with self.tenedor_der:
                        print(f"{self.nombre} está comiendo...")
                        time.sleep(random.uniform(1, 5))
                        print(f"{self.nombre} terminó de comer (soltó tenedor derecho e izquierdo)\n")

# --- Configuración para Filósofo Arbitrario ---
print("Iniciando simulación con Filósofo Arbitrario...\n")
NUM_FILOSOFOS = 5
tenedores = [threading.Lock() for _ in range(NUM_FILOSOFOS)]
filosofos = []

for i in range(NUM_FILOSOFOS):
    es_arbitrario = False
    if i == NUM_FILOSOFOS - 1: # El último filósofo será el arbitrario
        es_arbitrario = True
    
    f = Filosofo(f"Filósofo {i+1}", tenedores[i], tenedores[(i + 1) % NUM_FILOSOFOS], es_arbitrario)
    filosofos.append(f)
    f.start()

