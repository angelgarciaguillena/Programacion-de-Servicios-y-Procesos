from multiprocessing import Process, Pipe
import time
import random

def generarDireccion(conexion):
    
    ip = ""
    
    for i in range(10):
        
        for j in range(4):
            secuencia = random.randint(0, 255)
            
            ip += str(secuencia)
            
            if j < 3:
                ip += "."
                
        conexion.send(ip)
        ip = ""
        
    conexion.send(None)
    conexion.close()
    
    
def clasificarDireccion(entrada, salida):

    direccion = entrada.recv()
    contador = 0

    print("\nClasificación de IPs:")
    
    while direccion is not None:
        secuencia = int(direccion.split('.')[0])
        
        if (1 <= secuencia <= 126) or (128 <= secuencia <= 191) or (192 <= secuencia <= 223):
            print(f"IP válida: {direccion}")
            salida.send(direccion)
            contador += 1
        else:
            print(f"IP descartada: {direccion}")
        
        direccion = entrada.recv()
    
    salida.send(None)
    entrada.close()
    salida.close()
    
    
def mostrarDireccion(conexion):
    direccion = conexion.recv()

    print("\nLista de IPs:")

    while direccion is not None:
        secuencia = int(direccion.split('.')[0])
        
        if 1 <= secuencia <= 126:
            clase = "A"
        elif 128 <= secuencia <= 191:
            clase = "B"
        elif 192 <= secuencia <= 223:
            clase = "C"
        
        print(f"{direccion} - Clase {clase}")
        
        direccion = conexion.recv()
    
    conexion.close()
    

if __name__ == "__main__":
    
    inicio = time.time()

    left, right = Pipe()
    left2, right2 = Pipe()

    p1 = Process(target = generarDireccion, args = (left,))
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