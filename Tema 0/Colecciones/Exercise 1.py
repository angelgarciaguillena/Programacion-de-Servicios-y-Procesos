#Importamos la libreria random
import random

#Creamos una lista para almacenar 10 numeros
numbers = [] 

#Creamos un bucle for para generar 10 numeros aleatorios y añadirlos a la lista
for i in range (0, 10):

    #Añadimos numeros aleatorios a la lista
    numbers.append(random.randint(1, 100))

#Creamos un bucle for para imprimir los numeros
for i in range (0, 10):

    #Imprimimos el numero
    print(numbers[i])