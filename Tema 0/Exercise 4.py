#Improtamos la libreria random
import random

#Almacenamos el numero secreto generado aleatoriamente entre el 1 y el 100
secret_number = random.randint(1, 100)

#Pedimos al usuario que introduzca un numero 
user_number = int(input("Introduce a number "))

#Creamos un bucle while para que mientras no se acierte el numero y el usuario no se rinda, seguir pidiendo al usuario que introduzca un numero
while user_number != secret_number and user_number != -1:
    
    #Mostramos al usuario que el numero que ha introducido es incorrecto
    print("The number that you entered is incorrect")

    #Si el numero introducido por el usuario es mayor al numero secreto le informamos con un mensaje
    if user_number < secret_number:

        #Mostramos al usuario que el numero introducido es mayor al numero secreto
        print("The number entered is greater than the secret number")

    #Pero si el numero introducido por el usuario es menor al numero secreto le informamos con un mensaje
    else:

        #Mostramos al usuario que el numero introducido es menor al numero secreto
        print("The number entered is less than the secret number")

    #Pedimos al usuario que introduzca otro numero 
    user_number = int(input("Introduce other number "))

#Si el numero que ha introducido el usuario es igual al numero oculto le mostramos al usuario que ha ganado
if user_number == secret_number:

    #Mostramos al usuario que el numero que ha introducido es correcto
    print("The number that you entered is correct")

#Si no el usuario se ha rendido
else:

    #Mostramos un mensaje al usuario indicando que se ha rendido
    print("You have given up on the game")