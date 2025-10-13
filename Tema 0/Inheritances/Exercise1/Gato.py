"""Importamos la clase Animal"""
from Animal import *

"""Clase que hereda de Animal encargada de representar un gato y sus funciones basicas"""
class Gato(Animal):

    """Constructor que inicializa los atributos de la clase Gato comprobando
    que sus valores son validos antes de asignarlos"""
    def __init__(self, name, number_legs):
        super().__init__(name, number_legs)

    """Funcion que se encarga de devolver el sonido que hace el gato"""
    def habla(self):
        return "Miau"
    
    """Funcion encargada de devolver la informacion del gato"""
    def __str__(self):
        return "Soy un gato. " + super().__str__()