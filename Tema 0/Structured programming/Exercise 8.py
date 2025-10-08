#Pedimos al usuario que introduzca un numero 
user_number = int(input("Introduce a number "))

#Creamos un bucle for para recorrer desde el 1 hasta el numero introducido por el usuario
for i in range(1, user_number+1):

    #Calculamos el numero de espacios restando al numero introducido por el usuario el numero del contador
    spaces = user_number - i

    #Mostramos el numero de espacios y el numero de estrellas correspondiente a la linea
    print(" " * spaces + "* " * i)