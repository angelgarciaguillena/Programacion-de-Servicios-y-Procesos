from multiprocessing import Process, Queue
import os
import time

def sumarNumeros(cola):
    
    while True:

        total = 0

        numeros = cola.get()
        
        if numeros is None:
            break

        numero1, numero2 = numeros

        inicio = min(numero1, numero2)
        final = max(numero1, numero2)

        for i in range (inicio, final + 1):
            total = total + i

        print(f"La suma de {inicio} a {final} es {total}")


def leerNumeros(fichero, numeros):

    f = open(fichero, 'rt', encoding="utf8")

    for linea in f.readlines():
        numero1, numero2 = linea.split()
        numeros.put((int(numero1), int(numero2)))

    f.close()


if __name__ == "__main__":

    inicio = time.time()

    fichero = 'C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema2\\Boletin1\\numeros2.txt'

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