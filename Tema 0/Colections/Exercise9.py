#Creamos un diccionario con las letras del abecedario y las puntuaciones de cada letra
abecedary = {
    'a': 1, 
    'b': 3, 
    'c': 3, 
    'd': 2, 
    'e': 1, 
    'f': 4, 
    'g': 2, 
    'h': 4,
    'i': 1, 
    'j': 8, 
    'k': 5, 
    'l': 1, 
    'm': 3, 
    'n': 1, 
    'o': 1, 
    'p': 3,
    'q': 10, 
    'r': 1, 
    's': 1, 
    't': 1, 
    'u': 1, 
    'v': 4, 
    'w': 4, 
    'x': 8,
    'y': 4, 
    'z': 10
}

#Pedimos una palabra al usuario
word = input("Introduce a word: ")

#Creamos una variable que almacenara la puntuacion de la palabra
total_score = 0

#Creamos un bucle for para recorrer la palabra
for letter in word:

    #Si la letra se encuentra en el abecedario sumamos la puntuacion
    if letter in abecedary:

        #Sumamos la puntuacion de la letra
        total_score += abecedary[letter]

    #Si no esta en el abecedario informamos al usuario
    else:
        print("The letter '" + letter + "' has no punctuation")

#Mostramos al usuario la puntuacion de la palabra
print("The punctuation of the word is:", total_score, "points")