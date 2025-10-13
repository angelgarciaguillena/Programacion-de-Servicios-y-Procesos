#Abrimos el fichero
f = open('C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema 0\\Files\\Exercise2\\fichero.txt', 'w', encoding="utf8")

#Pedimos al usuario que introduzca una linea para escribirla en el fichero
line = input("Introduce a line: ")

#Creamos un bucle while para seguir pidiendo y escribiendo lineas hasta que el usuario introduzca 'fin'
while line != "fin":

    #Escribimos la linea en el fichero
    f.write(line + "\n")

    #Pedimos al usuario que introduzca otra linea
    line = input("Introduce other line: ")

#Cerramos el fichero
f.close