"""Importamos la clase Empleado"""
from Empleado import *

"""Clase que hereda de Empleado encargada de representar un operario y sus funciones basicas"""
class Operario(Empleado):

    """Constructor que inicializa los atributos de la clase Operario comprobando
    que sus valores son validos antes de asignarlos"""
    def __init__(self, name):
        super().__init__(name)

    """Funcion encargada de devolver la informacion del operario"""
    def __str__(self):
        return super().__str__() + " -> Operario"