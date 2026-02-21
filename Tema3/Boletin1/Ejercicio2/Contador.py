import threading

class Contador(threading.Thread):

    contador = 0

    def __init__(self, nombre):
        threading.Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        while Contador.contador < 1000:
            Contador.contador += 1
            print(f"{self.nombre}: {Contador.contador}")

        print(f"{self.nombre} ha terminado (contador = {Contador.contador})")