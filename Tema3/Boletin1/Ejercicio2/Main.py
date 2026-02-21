from Contador import Contador

hilos = [Contador(f"Hilo {i+1}") for i in range(10)]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Valor final:", Contador.contador)
