from multiprocessing import Process
import os
import time

def sumarNumeros(numero1, numero2):
    total = 0

    inicio = min(numero1, numero2)
    final = max(numero1, numero2)

    for i in range (inicio, final + 1):
        total = total + i

    print(f"Proceso {os.getpid()}: La suma de {inicio} a {final} es {total}")


if __name__ == "__main__":

    inicio = time.time()

    valores = [(1, 10), (10, 20), (30, 40), (50, 60)]
    procesos = []

    for valor1, valor2 in valores:
        p = Process(target = sumarNumeros, args = (valor1, valor2))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("Todos los procesos han terminado")

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio} segundos")