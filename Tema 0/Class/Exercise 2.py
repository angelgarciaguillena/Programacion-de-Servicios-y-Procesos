class Libro:

    def __init__(self, title, author, copies_book, copies_borrowed):
        
        if title is not None and title != "":
            self.title = title

        if author is not None and author != "":
            self.author = author

        if copies_book is not None and copies_book >= 0:
            self.copies_book = copies_book

        if copies_borrowed is not None and copies_borrowed >= 0:
            self.copies_borrowed = copies_borrowed


    def borrow(self):

        correct = False

        if copies_book > 0:
            copies_book -= 1
            copies_borrowed += 1
            correct = True

        return correct
    
    def devolution(self):

        correct = False

        if copies_borrowed > 0:
            copies_borrowed -= 1
            copies_book += 1
            correct = True

        return correct
    
    def __str__(self):

        string = "Titulo: " + self.title

