from multiprocessing import Pool
import os
import time

def sumarNumeros(limite):
    total = 0
    
    for i in range (0, limite + 1):
        total = total + i

    print(f"Proceso {os.getpid()}: La suma de 1 a {limite} es {total}")

    return total


if __name__ == "__main__":

    inicio = time.time()

    valores = [10, 20, 30, 40] 
    procesos = []

    with Pool(processes = len(valores)) as pool:
        resultados = pool.map(sumarNumeros, valores)

    print(f"Resultados: {resultados}") 

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio} segundos")