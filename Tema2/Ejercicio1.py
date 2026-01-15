from multiprocessing import Process
import os
import time

def sumarNumeros(limite):
    total = 0
    
    for i in range (0, limite + 1):
        total = total + i

    print(f"Proceso {os.getpid()}: La suma de 1 a {limite} es {total}")


if __name__ == "__main__":

    inicio = time.time()

    valores = [10, 20, 30, 40] 
    procesos = []

    for valor in valores:
        p = Process(target = sumarNumeros, args = (valor,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("Todos los procesos han terminado")

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio} segundos")