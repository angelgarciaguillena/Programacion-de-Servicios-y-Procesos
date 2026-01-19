from multiprocessing import Process, Queue
import os
import time

def sumarNumeros(numeros):
    
    total = 0

    while True:

        numero = numeros.get()

        if numero is None:
            break

        total = total + numero

        print(f"Sumando {numero}, el total es {total}")


def leerNumeros(fichero, numeros):

    f = open(fichero, 'rt', encoding="utf8")

    for numero in f.readlines():
        numeros.put(int(numero))

    f.close()


if __name__ == "__main__":

    inicio = time.time()

    fichero = 'C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema2\\Boletin1\\numeros.txt'

    queue = Queue()

    p1 = Process(target = leerNumeros, args = (fichero, queue))
    p2 = Process(target = sumarNumeros, args = (queue,))

    p1.start()
    p2.start()

    p1.join()
    queue.put(None)

    p2.join()
    
    print("Todos los procesos han terminado")

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio} segundos")