"""Importamos la clase Producto"""
from Producto import * 

"""Clase encargada de representar un producto no perecedero y sus funciones basicas"""
class NoPerecedero(Producto):

    """Constructor que inicializa los atributos de la clase NoPerecedero comprobando
    que sus valores son validos antes de asignarlos"""
    def __init__(self, name, price, type):

        super().__init__(name, price)

        self.type = type

    """Funcion encargada de calcular y devolver el precio del producto"""
    def calcular(self, quantity_product):

        return super().calcular(quantity_product) 

    """Funcion encargada de devolver la informacion del producto no perecedero"""
    def __str__(self):

        return super().__str__() + " - " + self.type