from multiprocessing import Pipe, Process

"""Funcion encargada de leer el fichero salarios, separar los datos de cada linea con , y enviarlos al siguiente proceso
si el nombre del departamento introducido por parametros coincide con el nombre de departamento del fichero"""
def enviar_departamento(nombre_departamento, conexion):
    
    # Abrimos el fichero salarios.txt en modo lectura
    with open("salarios.txt", "r") as f:
        
        #Creamos un bucle for para recorrer cada linea del fichero
        for linea in f.readlines():
            
            #Almacenamos la linea en una lista separando la linea por punto y coma
            datos = linea.strip().split(";")
            
            #Almacenamos el nombre, apellido, salario y departamento almacenado en la lista de datos de la linea en variables independientes
            nombre, apellido, salario, departamento = datos
            
            #Si el departamento es igual al nombre del departamento que ha introducido por parametros, enviamos los datos
            if departamento.strip().lower() == nombre_departamento.lower():
                
                #Enviamos el nombre, apellido y salario al siguiente proceso
                conexion.send(f"{nombre},{apellido},{salario}")
    
    #Enviamos un None para asignar el final de la cola            
    conexion.send(None)
    
    #Cerramos la conexion            
    conexion.close()


"""Funcion encargada de recibir los datos del proceso anterior, controlar si el salario es mayor o igual al salario minimo introducido por
parametros y si es mayor o igual enviar los datos al siguiente proceso"""
def enviar_salario_mayor(salario_minimo, conexion_entrada, conexion_salida):
    
    #Recibimos los primeros datos del proceso anterior
    datos = conexion_entrada.recv()
    
    #Mientras que los datos no sean nulos seguir comprobando si el salario es mayor o igual al minimo para enviarlos
    while datos is not None:
        
        #Almacenamos el nombre, apellido y salario de los datos que recibimos
        nombre, apellido, salario = datos.split(",")
        
        #Convertimos el salario de string a float
        salario = float(salario)
        
        #Si el salario es mayor o igual al salario minimo, se envia al siguiente proceso el nombre, apellido y salario
        if(salario >= salario_minimo):
            
            #Enviamos los datos al siguiente proceso
            conexion_salida.send(f"{nombre},{apellido},{salario}")
        
        #Recibimos mas datos del proceso anterior
        datos = conexion_entrada.recv()
    
    #Enviamos un None para asignar el final de la cola
    conexion_salida.send(None)
    
    #Cerramos la conexion de entrada
    conexion_entrada.close()
    
    #Cerramos la conexion de salida
    conexion_salida.close()


"""Funcion encargada de recibir los datos y escribir en el fichero empleados.txt, los datos de los empleados"""
def escribir_datos(conexion):
    
    #Recibimos los primeros datos del proceso anterior
    datos = conexion.recv()
    
    #Abrimos el fichero donde se va a escribir los empleados
    with open("empleados.txt", "w") as f:
        
        #Mientras que los datos no sean nulos seguir escribiendo los datos en el fichero
        while datos is not None:
            
            #Almacenamos el nombre, apellido y salario de los datos que recibimos
            nombre, apellido, salario = datos.split(",")
            
            #Escribimos el empleado con el formato correcto
            f.write(f"{apellido} {nombre}, {salario}\n")
            
            #Recibimos mas datos del proceso anterior
            datos = conexion.recv()
            
    #Cerramos la conexion
    conexion.close()


"""Main del ejercicio"""
if __name__ == "__main__":
    
    #Pedimos al usuario que introduzca el nombre del departamento
    nombre_departamento = input("Introduce el nombre del departamento: ").strip()
    
    #Pedimos al usuario que introduzca el salario minimo
    salario_minimo = float(input("Introduce el salario minimo: "))

    #Creamos una Pipe entre proceso 1 y proceso 2
    left, right = Pipe()
    
    #Creamos una Pipe entre el proceso 2 y proceso 3
    left2, right2 = Pipe()

    #Creamos y almacenamos el proceso 1
    p1 = Process(target=enviar_departamento, args=(nombre_departamento, left))
    
    #Creamos y almacenamos el proceso 1
    p2 = Process(target=enviar_salario_mayor, args=(salario_minimo, right, left2))
    
    #Creamos y almacenamos el proceso 1
    p3 = Process(target=escribir_datos, args=(right2,))

    #Lanzamos el proceso 1
    p1.start()
    
    #Lanzamos el proceso 2
    p2.start()
    
    #Lanzamos el proceso 3
    p3.start()

    #Esperamos a que termine el proceso 1
    p1.join()
    
    #Esperamos a que termine el proceso 2
    p2.join()
    
    #Esperamos a que termine el proceso 3
    p3.join()

    #Informamos al usuario de que todos los procesos han terminado
    print("Todos los procesos han terminado")