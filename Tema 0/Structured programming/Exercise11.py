#Creamos una funcion para que devuelva si la letra pasada por parametros es una vocal o no
def is_vowel(letter):

    #Creamos una variable que servira como contador
    counter = 0

    #Creamos una variable para almacenar si la letra es una vocal o no 
    vowel = False

    #Creamos una lista con las vocales
    letters = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    #Creamos un bucle while para recorrer la lista mientras no se haya enconnrado la vocal y no haya terminado la lista
    while counter < len(letters) and not vowel:

        #Si la vocal de la lista coincide con la letra se asigna que la letra es una vocal
        if(letters[counter] == letter):

            #Asignamos que la letra es una vocal
            vowel = True

        #Sumamos 1 al contador
        counter += 1
        
    #Devolvemos si la letra es una vocal o no
    return vowel


#Pedimos al usuario que introduzca una letra
letter = input("Introduce a letter ")

#Llamamos a la funcion para que devuelva si la letra es una vocal o no
vowel = is_vowel(letter)

#Si la letra es una vocal indicamos al usuario que es una vocal
if vowel:

    #Mostramos al usuario que la letra es una vocal
    print("The letter is a vowel")

#Si no indicamos al usuario que no es una vocal
else:

    #Mostramos al usuario que la letra no es una vocal
    print("The letter is not a vowel")