#Pedimos al usuario que introduzca un numero entero positivo
user_number = int(input("Introduce a positive integer"))

#Si el numero es menor o igual a 1 avisamos al usuario que el numero no es primo
if user_number <= 1:

    #Informamos al usuario que el numero no es primo
    print("The number is not prime")

#Si el numero es mayor a 1
else:

    #Creamos una variable para almacenar si el numero es primo o no
    is_prime = True

    #Creamos una variable que servira como contador y la igualamos a 2 
    counter = 2

    #Creamos un bucle while para recorrer desde el 2 hasta el numero introducido por el usuario mientras sea menor al numero del usuario y el numero no se pueda dividir
    while counter < user_number and is_prime:

        #Si el numero del usuario es divisible entre un numero del rango el numero no es primo
        if user_number % counter == 0:

            #Asignamos que el numero no es primo
            is_prime = False

        #Sumamos 1 al contador
        counter += 1

    #Si el numero es primo informamos al usuario
    if is_prime:

        #Informamos al usuario que el numero es primo
        print("The number is prime")

    #Si no el numero no es primo
    else:

        #Informamos al usuario que el numero no es primo
        print("The number is not prime")