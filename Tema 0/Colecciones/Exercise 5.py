#Importamos la libreria random
import random

#Creamos una lista para almacenar los numeros
numbers = []

#Creamos un bucle for para generar 100 numeros aleatorios y añadirlos a la lista
for i in range(0, 100):

    #Generamos un numero aleatorio y lo añadimos a la lista
    numbers.append(random.randint(1,10))

#Pedimos al usuario que introduzca un numero
number = int(input("Introduce a number "))

#Creamos una variable para contar las veces que aparece el numero en la lista
counter = 0

#Creamos un bucle for para recorrer la lista
for i in range(0, 100):

    #Si el numero es igual al de la lista se suma uno al contador
    if numbers[i] == number:

        #Sumamos uno al contador de veces que ha aparecido el numero
        counter += 1

#Informamos al usuario de las veces que ha aparecido el numero en la lista
print("The number", number, "has appeared", counter, "times")