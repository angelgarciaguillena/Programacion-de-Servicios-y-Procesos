#Pedimos el primer numero al usuario
first_number = int(input("What is your first number? "))

#Pedimos el segundo numero al usuario
second_number = int(input("What is your second number? "))

#Si el primer numero es mayor al segundo el segundo numero se muestra antes que el primero
if first_number >  second_number:

    #Mostramos al usuario el orden de los numeros
    print(second_number, first_number)

#Si el primer numero es mayor al segundo el segundo numero se muestra despues que el primero
elif second_number > first_number:

    #Mostramos al usuario el orden de los numeros
    print(first_number, second_number)

#Sino los numeros son iguales
else:
    
    #Mostramos al usuario que los numeros son iguales
    print("The numbers are same")