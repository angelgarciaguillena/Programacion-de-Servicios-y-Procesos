from multiprocessing import Process, Pipe
import time
import random

def generarDireccion():
    
    direcciones = []
    ip = ""
    
    for i in range(10):
        
        for j in range(4):
            secuencia = random.nextInt(0, 255)
            
            ip += str(secuencia)
            
            if j < 3:
                ip += "."
                
        direcciones.append(ip)
        ip = ""
        
    return direcciones   
    
    
def clasificarDireccion():
    
    
def mostrarDireccion():
    
if __name__ == "__main__":
    
    inicio = time.time()

    fichero = 'C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema2\\Boletin1\\numeros.txt'

    left, right = Pipe()
    left2, right2 = Pipe()

    p1 = Process(target = generarDireccion, args = (fichero, left))
    p2 = Process(target = clasificarDireccion, args = (right, left2))
    p3 = Process(target = mostrarDireccion, args = (right2,))
    

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    
    print("Todos los procesos han terminado")

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio} segundos")