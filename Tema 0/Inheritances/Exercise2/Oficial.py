"""Importamos la clase Operario"""
from Operario import *

"""Clase que hereda de Operario encargada de representar un oficial y sus funciones basicas"""
class Oficial(Operario):

    """Constructor que inicializa los atributos de la clase Oficial comprobando
    que sus valores son validos antes de asignarlos"""
    def __init__(self, name):
        super().__init__(name)

    """Funcion encargada de devolver la informacion del oficial"""
    def __str__(self):
        return super().__str__() + " -> Oficial"