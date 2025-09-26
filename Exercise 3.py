#Creamos una variable para almacenar la suma de los numeros
sum = 0

#Pedimos al usuario que introduzca un numero
number = int(input("Introduce a number: "))

#Mientras el numero sea mayor a 0 seguiremos pidiendo numeros al usuario
while(number > 0):

    #Sumamos el numero introducido por el usuario al total
    sum += number

    #Pedimos al usuario que introduzca otro numero
    number = int(input("Introduce other number: "))

#Mostramos la suma de todos los numeros que ha introducido el usuario
print("The sum of the numbers is", sum)