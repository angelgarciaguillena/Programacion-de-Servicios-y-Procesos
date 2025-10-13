"""Clase encargada de representar un Libro y sus funciones basicas"""
class Libro:

    """Constructor que inicializa los atributos de la clase Libro comprobando
    que los valores son validos antes de asignarlos"""
    def __init__(self, title, author, copies_book, copies_borrowed):
        
        if title is not None and title != "":
            self.title = title

        if author is not None and author != "":
            self.author = author

        if copies_book is not None and copies_book >= 0:
            self.copies_book = copies_book

        if copies_borrowed is not None and copies_borrowed >= 0:
            self.copies_borrowed = copies_borrowed

    """Funcion encargada de realizar el prestamo del libro siempre que haya copias 
    disponibles de ese libro y devuelve true si se ha realizado la operacion o false 
    si no se ha realizado"""
    def borrow(self):

        correct = False

        if self.copies_book > 0:
            self.copies_book -= 1
            self.copies_borrowed += 1
            correct = True

        return correct
    
    """Funcion encargada de realizar la devolucion del libro si hay copias prestadas 
    de ese libro y devuelve true si se ha realizado la operacion o false si no se ha
    realizado"""
    def devolution(self):

        correct = False

        if self.copies_borrowed > 0:
            self.copies_borrowed -= 1
            self.copies_book += 1
            correct = True

        return correct
    
    """Funcion encargada de devolver los datos de la cuenta corriente"""
    def __str__(self):

        string = "Titulo: " + self.title + "\n"
        string += "Author: " + self.author + "\n"
        string += "Copies of the book: " + str(self.copies_book) + "\n"
        string += "Borrowed copies: " + str(self.copies_borrowed) + "\n"

        return string
    
    """Funcion encargada de comprobar si dos libros son iguales segun
    su titulo y devuelve true si son iguales o false si no son iguales"""
    def __eq__(self, object):

        equals = False

        if self.title == object.title:
            equals = True

        return equals
    
    """Funcion encargada de ordenar los libros de menor a mayor
    segun el nombre del autor"""
    def __lt__(self, object):
        
        minor = False

        if self.author < object.author:
            minor = True

        return minor