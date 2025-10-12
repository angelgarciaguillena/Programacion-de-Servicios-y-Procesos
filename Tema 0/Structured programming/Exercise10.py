#Creamos una funcion para devolver el numero mayor de entre los dos que se han pasado por parametro
def max_number(number1, number2):

    #Si el numero 1 es mayor al numero 2 se almacenara en una variable
    if(number1 > number2):

        #Almacenamos el numero 1 en una variable
        max = number1
    
    #Si no se almacenara el numero 2
    else:

        #Almacenamos el numero 2 en una variable
        max = number2
    
    #Devolvemos el numero maximo
    return max


#Pedimos al usuario que introduzca un numero
number1 = int(input("Introduce a number "))

#Pedimos al usuario que introduzca otro numero 
number2 = int(input("Introduce other number "))

#Llamamos a la funcion para que nos devuelva el numero maximo
final_number = max_number(number1, number2)

#Imprimimos el numero maximo
print(final_number)