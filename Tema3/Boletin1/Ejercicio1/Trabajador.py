import threading
import time
import random

class Trabajador(threading.Thread):

    def __init__(self, nombre):
        threading.Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        while True:
            print(f"Soy {self.nombre} y estoy trabajando")

            espera = random.randint(1, 10)
            time.sleep(espera)

            print(f"Soy {self.nombre} y he terminado de trabajar")