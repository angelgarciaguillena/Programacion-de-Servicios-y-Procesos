import threading
import random

class Adivino(threading.Thread):

    numero_secreto = random.randint(0, 100)
    acierto = False

    def __init__(self, nombre):
        threading.Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        intentos = 0
        print(f"{self.nombre} empieza a buscar el número secreto")

        while True:
            intento = random.randint(0, 100)
            intentos += 1

            if intento == Adivino.numero_secreto:
                Adivino.acierto = True
                print(f"\n{self.nombre} ha acertado el numero {intento} en {intentos} intentos\n")
                return

            elif Adivino.acierto:
                print(f"{self.nombre} se detiene: otro hilo ya acerto")
                return