#Creamos una funcion para mostrar los numeros que existen entre los dos numeros pasados por parametros
def show_numbers(number1, number2):

    #Creamos un bucle for para imprimir los numeros que hay entre el numero 1 y el numero 2
    for i in range(number1, number2+1):

        #Imprimimos el numero
        print(i)


#Creamos una funcion que servira como main
def main():
    #Pedimos al usuario que introduzca un numero entero
    number1 = int(input("Introduce a enter number "))

    #Pedimos al usuario que introduzca otro numero entero
    number2 = int(input("Introduce other enter number "))

    #Llamamos a la funcion para mostrar los numeros entre los dos que les hemos pasado
    show_numbers(number1, number2)

#Llamamos al metodo main
main()