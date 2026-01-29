from datetime import datetime
from multiprocessing import Process, Queue
import time
import os

def filtrar_por_ano(ruta_fichero, ano, queue):
    with open(ruta_fichero, 'r', encoding='utf-8') as f:

        for linea in f:

            linea = linea.strip()

            if not linea:
                continue
    
            nombre, anio_str = linea.split(';')

            if int(anio_str) == ano:
                queue.put(nombre)  
            
    queue.put(None) 
    print(f"Envío de películas del año {ano} completado")


def guardar_peliculas(queue, ano):
    nombre_fichero = f"C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema2\\Boletin2\\peliculas{ano}.txt"
    with open(nombre_fichero, 'w', encoding='utf-8') as f:

        while True:

            pelicula = queue.get()

            if pelicula is None:  
                break

            f.write(f"{pelicula}\n")
    print(f"Archivo {nombre_fichero} creado con las películas filtradas")


if __name__ == "__main__":

    ano_actual = datetime.now().year
    
    while True: 
        try:
            ano = int(input(f"Introduce un año (menor o igual a {ano_actual}): "))
            if ano > 0 and ano <= ano_actual:
                break
            else:
                print("Año inválido. Intenta de nuevo.")
        except ValueError:
            print("Debes introducir un número entero.")

    
    ruta_fichero = input("Introduce la ruta del fichero de películas: ").strip()

    import os

    if not os.path.exists(ruta_fichero):
        ruta_fichero = "C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema2\\Boletin2\\peliculas.txt"
        print(f"Usando el fichero por defecto: {ruta_fichero}")

    inicio = time.time()
    
    queue = Queue()

    p1 = Process(target=filtrar_por_ano, args=(ruta_fichero, ano, queue))
    p2 = Process(target=guardar_peliculas, args=(queue, ano))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Todos los procesos han terminado")
    fin = time.time()

