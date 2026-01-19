from multiprocessing import Pool
import os
import time

def sumarNumeros(numero1, numero2):
    total = 0

    inicio = min(numero1, numero2)
    final = max(numero1, numero2)

    for i in range (inicio, final + 1):
        total = total + i

    print(f"Proceso {os.getpid()}: La suma de {inicio} a {final} es {total}")

    return total


if __name__ == "__main__":

    inicio = time.time()

    valores = [(1, 10), (10, 20), (30, 40), (50, 60)]

    with Pool(processes = len(valores)) as pool:
        resultados = pool.starmap(sumarNumeros, valores)

    print(f"Resultados: {resultados}") 

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio} segundos")