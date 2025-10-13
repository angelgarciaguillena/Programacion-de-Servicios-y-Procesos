"""Clase encargada de representar un animal y sus funciones basicas"""
class Animal:

    """Constructor que inicializa los atributos de la clase Animal comprobando
    que sus valores son validos antes de asignarlos"""
    def __init__(self, name, number_legs):

        if name is not None and name != "":
            self.name = name

        if number_legs > 1:
            self.number_legs = number_legs

    """Funcion que se encarga de devolver el sonido que hace un animal"""
    def habla(self):
        return ""
    
    """Funcion encargada de devolver la informacion del animal"""
    def __str__(self):
        return "Me llamo " + self.name + ", tengo " + str(self.number_legs) + " patas y sueno asi: " + self.habla()