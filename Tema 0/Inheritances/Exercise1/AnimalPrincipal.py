#Importamos la clase Gato
from Gato import *

#Importamos la clase Perro
from Perro import *

#Creamos un gato
cat = Gato("Cat", 4)

#Creamos un perro
dog = Perro("Dog", 4)

#Mostramos la informacion del gato
print("\n" + "Cat:")
print(cat.__str__())

#Mostramos el sonido del gato
print("Cat sound:",cat.habla())

#Mostramos la informacion del perro
print("\n" + "Dog:")
print(dog.__str__())

#Mostramos el sonido del perro
print("Dog sound:", dog.habla())