import threading

class ContadorVocal(threading.Thread):

    def __init__(self, vocal):
        threading.Thread.__init__(self)
        self.vocal = vocal
        self.resultado = 0

    def run(self):
        with open("texto.txt", 'r') as f:
            for linea in f.readlines():
                self.resultado += linea.lower().count(self.vocal)