from multiprocessing import Process, Pipe
import os
import time

def sumarNumeros(conexion):
    
    total = 0

    while True:

        numero = conexion.recv()

        if numero is None:
            break

        total = total + numero

        print(f"Sumando {numero}, el total es {total}")

    conexion.close()    


def leerNumeros(fichero, conexion):

    f = open(fichero, 'rt', encoding="utf8")

    for numero in f.readlines():
        conexion.send(int(numero))

    f.close()
    conexion.send(None)
    conexion.close()


if __name__ == "__main__":

    inicio = time.time()

    fichero = 'C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema2\\numeros.txt'

    left, right = Pipe()

    p1 = Process(target = leerNumeros, args = (fichero, right))
    p2 = Process(target = sumarNumeros, args = (left,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    print("Todos los procesos han terminado")

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio} segundos")