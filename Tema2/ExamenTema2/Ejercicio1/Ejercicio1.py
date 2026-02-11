import random 
from multiprocessing import Process

"""Funcion encargada de generar las temperaturas de un dia y de escribirlos en un 
fichero cuyo nombre sera la fecha correspondiente"""
def generar_temperatura(dia):

    #Creamos el nombre del fichero donde se van a escribir las temperaturas
    fichero = f"{dia:02d}-12.txt"
    
    #Creamos una lista que almacenara las temperaturas del dia
    temperaturas = [] 
    
    #Creamos un bucle for para generar la temperatura 24 veces y almacenarla en la lista de temperaturas
    for i in range(24):
        
        #Generamos la temperatura con decimales
        temperatura = round(random.uniform(0, 20), 2)
        
        #Almacenamos la temperatura
        temperaturas.append(temperatura)
    
    #Abrimos el fichero donde se van a escribir las temperaturas
    with open(fichero, 'w') as f:
        
        #Creamos un bucle for para recorrer la lista de temperaturas y escribirlas en el fichero
        for temp in temperaturas:
            
            #Escribimos la temperatura en el fichero
            f.write(f"{temp}\n")
        
        
"""Funcion encargada de leer un fichero donde estan registradas todas las temperaturas 
del dia y escribir en un fichero la temperatura maxima de ese dia y la fecha en la 
que se produjo"""       
def escribir_temperatura_maxima(dia):
    
    #Creamos el nombre del fichero donde se van a leer las temperaturas
    fichero = f"{dia:02d}-12.txt"
    
    #Almacenamos la fecha de la que se van a leer las temperaturas
    fecha = f"{dia:02d}-12"
    
    #Creamos una lista que almacenara las temperaturas del dia
    temperaturas = []
    
    #Abrimos el fichero donde vamos a leer todas las temperaturas y almacenarla en la lista de temperaturas
    with open(fichero, "r") as f:
        
        #Creamos un bucle for para recorrer todas las lineas del fichero
        for line in f.readlines():
            
            #Almacenamos la temperatura en la lista de temperaturas
            temperaturas.append(float(line.strip()))
    
    #Almacenamos la temperatura maxima de las temperaturas del fichero
    maxima = max(temperaturas)
    
    #Abrimos el fichero donde vamos a escribir la temperatura maxima del dia y la fecha del dia donde se produjo esa temperatura
    with open("maximas.txt", "a") as f:
        
        #Escribimos la fecha y la temperatura maxima del dia en el fichero
        f.write(f"{fecha}:{maxima}\n")
    
    
"""Funcion encargada de leer un fichero donde estan registradas todas las temperaturas 
del dia y escribir en un fichero la temperatura minima de ese dia y la fecha en la 
que se produjo"""    
def escribir_temperatura_minima(dia):
    
    #Creamos el nombre del fichero donde se van a leer las temperaturas
    fichero = f"{dia:02d}-12.txt"
    
    #Almacenamos la fecha de la que se van a leer las temperaturas
    fecha = f"{dia:02d}-12"
    
    #Creamos una lista que almacenara las temperaturas del dia
    temperaturas = []
    
    #Abrimos el fichero donde vamos a leer todas las temperaturas y almacenarla en la lista de temperaturas
    with open(fichero, "r") as f:
        
        #Creamos un bucle for para recorrer todas las lineas del fichero
        for linea in f.readlines():
            
            #Almacenamos la temperatura en la lista de temperaturas
            temperaturas.append(float(linea.strip()))
    
    #Almacenamos la temperatura minima de las temperaturas del fichero
    minima = min(temperaturas)
    
    #Abrimos el fichero donde vamos a escribir la temperatura minima del dia y la fecha del dia donde se produjo esa temperatura
    with open("minimas.txt", "a") as f:
        
        #Escribimos la fecha y la temperatura minima del dia en el fichero
        f.write(f"{fecha}:{minima}\n")
    

"""Main del ejercicio"""
if __name__ == "__main__":
    
    #Inicializamos la lista de procesos vacia
    procesos = []
    
    #Creamos un bucle for para ejecutar el proceso el numero de dias que tiene el mes
    for dia in range(1, 32):
        
        #Creamos y almacenamos el proceso encargado de generar las temperaturas del dia
        p = Process(target=generar_temperatura, args=(dia,))
        
        #Añadimos el proceso 1 a la lista de procesos
        procesos.append(p)
        
        #Iniciamos el proceso 1
        p.start()
        
    #Creamos un bucle for para esperar a que los procesos de generar la temperatura terminen
    for p in procesos:
        p.join()

    #Vaciamos la lista de procesos
    procesos = []
    
    #Creamos un bucle for para lanzar los procesos 
    for dia in range(1, 32):
        
        #Creamos y almacenamos el proceso que calcula la temperatura máxima del día
        p2 = Process(target=escribir_temperatura_maxima, args=(dia,))
        
        #Creamos y almacenamos el proceso que calcula la temperatura mínima del día
        p3 = Process(target=escribir_temperatura_minima, args=(dia,))
        
        #Almacenamos el proceso 2 en la lista de procesos
        procesos.append(p2)
        
        #Almacenamos el proceso 3 en la lista de procesos
        procesos.append(p3)
        
        #Iniciamos el proceso 2
        p2.start()
        
        #Iniciamos el proceso 3
        p3.start()

    #Creamos un bucle for para esperar a que los procesos de maximo y minimos terminen
    for p in procesos:
        p.join()
        
    #Informamos al usuario de que todos los procesos han terminado
    print("Todos los procesos han finalizado")