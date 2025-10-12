#Importamos la clase Libro
from Libro import *

#Creamos un libro
book1 = Libro("Libro 1", "Autor 1", 8, 0)

#Creamos otro libro
book2 = Libro("Libro 2", "Autor 2", 4, 2)

#Realizamos el prestamo del libro 1
correct = book1.borrow()

#Mostramos si se ha realizado la operacion de prestamo
print(correct)

#Mostramos la informacion del libro 1
print("\n" + "Book:")
print(book1.__str__())

#Realizamos la devolucion del libro 2
correct = book2.devolution()

#Mostramos si se ha realizado la operacion de devolucion
print(correct)

#Mostramos la informacion del libro 2
print("\n" + "Book:")
print(book2.__str__())

#Comprobamos si los libros son iguales
equals = book1.__eq__(book2)

#Mostramos si los libros son iguales
print(equals)