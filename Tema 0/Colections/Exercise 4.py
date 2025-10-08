#Creamos una lista para almacenar los numeros
numbers = []

#Creamos un bucle for para pedir 10 numeros al usuario y introducirlos en la lista
for i in range(0, 10):

    #Pedimos al usuario que introduzca un numero y lo añadimos a la lista
    numbers.append(int(input("Introduce a number ")))

#Ordenamos los numeros de la lista de mayor a menor
numbers.sort(reverse = True)

#Imprimimos la lista
print(numbers)