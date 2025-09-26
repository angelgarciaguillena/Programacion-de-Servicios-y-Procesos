#Pedimos al usuario que introduzca un numero
number = int(input("What is your number? "))

#Si el numero dividido entre 2 es 0 el numero es par
if (number % 2 == 0):
    #Mostramos al usuario que el numero es par
    print("Your number is even")

#Sino es impar
else:
    #Mostramos al usuario que el numero es impar
    print("Your number is odd")