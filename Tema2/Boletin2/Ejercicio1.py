from multiprocessing import Process
import os
import time
    
def leerFichero(fichero, vocalRecibida):
    
    contador = 0
    
    f = open(fichero, 'rt', encoding="utf8")
    
    for linea in f.readlines():
        contador += linea.strip().lower().count(vocalRecibida)

    print(f"Proceso {os.getpid()}: La vocal {vocalRecibida} aparece {contador} veces")
    
    f.close()

    
if __name__ == "__main__":
    
    inicio = time.time()
    
    fichero = 'C:\\Users\\angel.garcia\\Documents\\GitHub\\Programacion-de-Servicios-y-Procesos\\Tema2\\Boletin2\\vocales.txt'
    
    letras = ["a", "e", "i", "o", "u"]
    procesos = []
    
    for letra in letras:
        p = Process(target = leerFichero, args = (fichero, letra))
        procesos.append(p)
        p.start()
        
    for proceso in procesos:
        proceso.join()
        
    print("Todos los procesos han terminado")

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio} segundos")