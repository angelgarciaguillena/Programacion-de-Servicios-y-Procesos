from Trabajador import Trabajador
import time

nombres = ["Ana", "Luis", "Carlos", "Marta", "Sofia"]
hilos = []

for nombre in nombres:
    hilo = Trabajador(nombre)
    hilo.daemon = True 
    hilos.append(hilo)
    hilo.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario")