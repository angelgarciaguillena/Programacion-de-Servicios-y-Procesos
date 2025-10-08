#Creamos una funcion para calcular y devolver la operacion que indica el usuario con los dos numeros que nos indica el usuario por parametros
def calculator(number1, number2, option):
    
    #Si la opcion que introduce el usuario es 1 se sumaran los dos numeros
    if(option == 1):

        #Almacenamos la suma de los dos numeros
        result = number1 + number2

    #Si la opcion que introduce el usuario es 2 se restaran los dos numeros
    elif(option == 2):

        #Almacenamos la resta de los dos numeros
        result = number1 - number2

    #Si la opcion que introduce el usuario es 3 se multiplicaran los dos numeros
    elif(option == 3):

        #Almacenamos la multiplicacion de los dos numeros
        result = number1 * number2

    #Si la opcion que introduce el usuario es 4 se dividiran los dos numeros
    elif(option == 4):

        #Almacenamos la division de los dos numeros
        result = number1 / number2

    #Devolvemos el resultado de la operacion
    return result

#Pedimos al usuario que introduzca el primer numero
number1 = int(input("Introduce the first number "))

#Pedimos al usuario que introduzca el segundo numero
number2 = int(input("Introduce the second number "))

#Pedimos al usuario que introduzca la opcion de la calculadora
option = int(input("Introduce the calculator option "))

#Llamamos a la funcion para que nos devuelva el resultado de la operacion
result_operation = calculator(number1, number2, option)

#Mostramos el resultado de la operacion al usuario
print("The result of the operation is", result_operation)