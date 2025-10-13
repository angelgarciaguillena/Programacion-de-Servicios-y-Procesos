"""Importamos la clase Animal"""
from Animal import * 

"""Clase que hereda de Animal encargada de representar un perro y sus funciones basicas"""
class Perro(Animal):

    """Constructor que inicializa los atributos de la clase Perro comprobando
    que sus valores son validos antes de asignarlos"""
    def __init__(self, name, number_legs):
        super().__init__(name, number_legs)

    """Funcion que se encarga de devolver el sonido que hace el perro"""
    def habla(self):
        return "Guau"
    
    """Funcion encargada de devolver la informacion del perro"""
    def __str__(self):
        return "Soy un perro. " + super().__str__()