import threading
import time
import random

class Filosofo(threading.Thread):
    def __init__(self, nombre, tenedor_izq, tenedor_der, id_tenedor_izq, id_tenedor_der):
        super().__init__()
        self.nombre = nombre
        self.comida = 0
        self.tenedor_izq = tenedor_izq
        self.tenedor_der = tenedor_der
        self.id_tenedor_izq = id_tenedor_izq
        self.id_tenedor_der = id_tenedor_der
        
    def comer(self):
        """Simula el acto de comer."""
        self.comida += 1
        print(f"{self.nombre} ha comido. Total comidas: {self.comida}")

    def run(self):
        while True:
            if self.comida >= 3:
                print(f"{self.nombre} ha comido suficiente y se retira de la mesa.\n")
                break
            print(f"{self.nombre} está pensando...")
            time.sleep(random.uniform(1, 3))

            # Determinar el orden de adquisición de tenedores por índice
            primer_tenedor, segundo_tenedor = None, None
            if self.id_tenedor_izq < self.id_tenedor_der:
                primer_tenedor = self.tenedor_izq
                segundo_tenedor = self.tenedor_der
                nombre_primer_tenedor = f"tenedor {self.id_tenedor_izq}"
                nombre_segundo_tenedor = f"tenedor {self.id_tenedor_der}"
            else:
                primer_tenedor = self.tenedor_der
                segundo_tenedor = self.tenedor_izq
                nombre_primer_tenedor = f"tenedor {self.id_tenedor_der}"
                nombre_segundo_tenedor = f"tenedor {self.id_tenedor_izq}"

            print(f"{self.nombre} intenta tomar {nombre_primer_tenedor}")
            with primer_tenedor:
                print(f"{self.nombre} tomó {nombre_primer_tenedor}")
                time.sleep(0.00001) 
                print(f"{self.nombre} intenta tomar {nombre_segundo_tenedor}")
                with segundo_tenedor:
                    print(f"{self.nombre} está comiendo...")
                    self.comer()
                    time.sleep(random.uniform(1, 5))
                    print(f"{self.nombre} terminó de comer (soltó {nombre_segundo_tenedor} y {nombre_primer_tenedor})\n")

# --- Configuración para Prevención por Jerarquía de Recursos ---
print("Iniciando simulación con Prevención por Jerarquía de Recursos...\n")
NUM_FILOSOFOS = 5
tenedores = [threading.Lock() for _ in range(NUM_FILOSOFOS)]
filosofos = []

for i in range(NUM_FILOSOFOS):
    id_tenedor_izq = i
    id_tenedor_der = (i + 1) % NUM_FILOSOFOS
    # El último filósofo tendrá un orden de tenedores invertido si no se maneja la jerarquía
    # pero la lógica dentro de run() lo maneja correctamente.
    f = Filosofo(f"Filósofo {i+1}", tenedores[id_tenedor_izq], tenedores[id_tenedor_der], id_tenedor_izq, id_tenedor_der)
    filosofos.append(f)
    f.start()

