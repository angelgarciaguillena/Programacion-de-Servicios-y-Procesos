#Creamos un diccionario con el codigo de cifrado
dictionary_letters = {
    "e" : "p", 
    "i" : "v", 
    "k" : "i",
    "m" : "u", 
    "p" : "m",
    "q" : "t",
    "r" : "e",
    "s" : "r",
    "t" : "k",
    "u" : "q",
    "v" : "s"}

#Pedimos al usuario quie introduzca una frase
phrase = input("Introduce a phrase to encrypt it: ")

#Convertimos la frase en minuscula
phrase.lower()

#Creamos una variable que almacenara la palabra transformada
encrypted_phrase = ""

#Creamos un bucle for para recorrer la palabra
for letter in phrase:

    #Si la letra esta en el diccionario añadimos la clave a la frase encriptada
    if letter in dictionary_letters:

        #Añadimos la letra encriptada a la frase
        encrypted_phrase += dictionary_letters[letter]

    #Si no añadimos la letra a la frase encriptada
    else:

        #Añadimos la letra a la frase encriptada
        encrypted_phrase += letter

#Mostramos la frase encriptada al usuario
print("The encrypted phrase is", encrypted_phrase)