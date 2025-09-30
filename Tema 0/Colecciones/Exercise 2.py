#Creamos una lista para almacenar los numeros
numbers = [] 

#Creamos un bucle for para pedir al usuario 10 numeros y añadirlos a la lista
for i in range(0, 10):
    numbers.append(int(input("Introduce a number ")))

#Creamos una variable para almacenar el numero minimo
min = numbers[0]

#Creamos una variable para almacenar el numero maximo
max = numbers[0]

#Creamos un bucle for para recorrer la lista y ver cual es el numero mayor y cual es el numero menor
for i in range(0, 10):

    #Si el numero es menor al minimo se asigna como nuevo minimo
    if numbers[i] < min:

        #Guardamos el minimo
        min = numbers[i]

    #Si el numero es mayor al maximo se asigna como nuevo maximo
    if numbers[i] > max:
        
        #Guardamos el maximo
        max = numbers[i]

#Mostramos al usuario el numero maximo
print("The maximun number is", max)

#Mostramos al usuario el numero minimo
print("The minimum number is", min)