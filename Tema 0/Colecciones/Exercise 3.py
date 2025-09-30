#Creamos una lista para almacenar los 8 numeros
numbers = []

#Creamos un bucle for para pedir los 8 numeros al usuario
for i in range(0, 8):

    #Añadimos los numeros introducidos por el usuario a la lista
    numbers.append(int(input("Introduce a number ")))

#Creamos un bucle for para recorrer la lista
for i in range(0, 8):
    
    #Si el numero es par se lo indicamos al usuario
    if numbers[i] % 2 == 0:

        #Mostramos al usuario que el numero es par
        print(numbers[i], "Even")

    #Si no el numero sera impar y se lo informamos al usuario
    else:

        #Mostramos al usuario que el numero es impar
        print(numbers[i], "Odd")
