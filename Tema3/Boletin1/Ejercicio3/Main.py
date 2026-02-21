from Adivino import Adivino

print(f"Numero secreto generado: {Adivino.numero_secreto}\n")

hilos = [Adivino(f"Hilo {i+1}") for i in range(10)]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los hilos han terminado")