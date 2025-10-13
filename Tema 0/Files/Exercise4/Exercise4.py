#Abrimos el fichero de lectura
f = open('C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema 0\\Files\\Exercise4\\enteros.txt', 'rt')

#Creamos una lista que almacene los enteros
integers = []

#Creamos un bucle for para leer los enteros del fichero
for line in f.readlines():

    #Añadimos el numero del fichero de lectura a la lista
    integers.append(int(line))

#Ordenamos los numeros
integers.sort()

#Abrimos el fichero de escritura
f2 = open('C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema 0\\Files\\Exercise4\\numeros_ordenados.txt', 'a')

#Creamos un bucle for para recorrer la lista de numeros y escribirlos en el fichero
for number in integers:

    #Escribimos el numero en el fichero
    f2.write(str(number) + " ")

#Cerramos el fichero de lectura
f.close

#Cerramos el fichero de escritura
f2.close