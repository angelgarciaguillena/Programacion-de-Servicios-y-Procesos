#Creamos una variable para almacenar el factorial del numero introducido por el usuario y establecemos su valor en 1 porque siempre empezara en 1
factorial_number = 1

#Pedimos al usuario que introduzca un numero 
user_number = int(input("Introduce a number "))

#Creamos un bucle for para calcular el factorial del numero introducido por el usuario
for i in range(2, user_number + 1):

    #Multiplicamos el numero en el que estamos por el factorial
    factorial_number *= i

#Mostramos el factorial del numero introducido por el usuario
print("The factorial of", user_number, "is", factorial_number)