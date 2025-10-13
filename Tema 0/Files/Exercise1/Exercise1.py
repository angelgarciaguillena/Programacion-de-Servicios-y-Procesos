#Abrimos el fichero
f = open('C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema 0\\Files\\Exercise1\\Alumnos.txt', 'rt')

#Creamos un bucle for para leer todas las lineas del fichero
for line in f.readlines():

    #Imprimimos por pantalla cada linea del fichero
    print(line, end = '')

#Cerramos el fichero
f.close