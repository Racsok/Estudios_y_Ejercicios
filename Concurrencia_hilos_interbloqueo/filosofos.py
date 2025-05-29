import threading
import time
import random
class Filosofo(threading.Thread):
    def __init__(self, nombre, tenedor_izq, tenedor_der):
        super().__init__()
        self.nombre = nombre
        self.tenedor_izq = tenedor_izq
        self.tenedor_der = tenedor_der
    def run(self):
        while True:
            print(f"{self.nombre} está pensando...")
            time.sleep(random.uniform(1, 3))
            print(f"{self.nombre} intenta tomar tenedor izquierdo")
            with self.tenedor_izq:
                print(f"{self.nombre} tomó tenedor izquierdo")
                time.sleep(0.00001)
                print(f"{self.nombre} intenta tomar tenedor derecho")
                with self.tenedor_der:
                    print(f"{self.nombre} está comiendo...")
                    time.sleep(random.uniform(1, 5))
                    print(f"{self.nombre} terminó de comer\n")
        print()
tenedores = [threading.Lock() for _ in range(5)]
filosofos = []

for i in range(5):
    f = Filosofo(f"Filósofo {i+1}", tenedores[i], tenedores[(i+1) % 5])
    filosofos.append(f)
    f.start()