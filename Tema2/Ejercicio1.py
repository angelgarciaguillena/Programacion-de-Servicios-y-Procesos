from multiprocessing import Process
import os

def sumarNumeros(limite):
    total = 0
    
    for i in range (0, limite):
        total = total + i
        
    print(f"Proceso {os.getpid()}: La suma de 1 a {i} es {total}")

if __name__ == "__main__":
    valores = [10, 20, 30, 40] 
    procesos = []

    for valor in valores:
        p = Process(target=sumarNumeros, args=(valor))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("Todos los procesos han terminado")