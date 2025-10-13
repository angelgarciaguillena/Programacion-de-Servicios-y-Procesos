#Abrimos el fichero
f = open('C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema 0\\Files\\Exercise3\\datos.txt', 'a', encoding="utf8")

#Pedimos al usuario que introduzca su nombre
name = input("Introduce your name: ")

#Pedimos al usuario que introduzca su edad
age = input("Introduce your age: ")

#Escribimos los datos en el fichero
f.write(name + " " + age + "\n")

#Cerramos el fichero
f.close()