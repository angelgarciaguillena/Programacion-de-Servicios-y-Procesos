"""Importamos la clase Empleado"""
from Empleado import *

"""Clase que hereda de Empleado encargada de representar un directivo y sus funciones basicas"""
class Directivo(Empleado):

    """Constructor que inicializa los atributos de la clase Directivo comprobando
    que sus valores son validos antes de asignarlos"""
    def __init__(self, name):
        super().__init__(name)

    """Funcion encargada de devolver la informacion del directivo"""
    def __str__(self):
        return super().__str__() + " -> Directivo"