#Creamos un diccionario para almacenar las palabras
words = {}

#Pedimos al usuario que introduzca una frase
string = input("Introduce a phrase ")

#Convertimos la frase en un array que contenga todas las palabras
string_splited = string.split(" ")

#Creamos un bucle for para recorrer el array y ir almacenando las palabras en el diccionario
for word in string_splited:

    #Transformamos la palabra a minuscula
    word = word.lower()

    #Si la palabra no se encuentra en el diccionario la añadimos
    if word not in words:

        #Añadimos la palabra con el numero inicial de veces
        words[word] = 1

    #Si se encuentra en el diccionario le sumamos 1 a las veces que el numero ha salido
    else:

        #Sumamos 1 al numero de veces que ha aparecido la palabra
        words[word] += 1
        
#Imprimimos el diccionario
print(words)