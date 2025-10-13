"""Importamos la clase Producto"""
from Producto import *

"""Clase encargada de representar un producto perecedero y sus funciones basicas"""
class Perecedero(Producto):

    """Constructor que inicializa los atributos de la clase Perecedero comprobando
    que sus valores son validos antes de asignarlos"""
    def __init__(self, name, price, day_expiration):

        super().__init__(name, price)

        if day_expiration > 0:
            self.day_expiration = day_expiration

    """Funcion encargada de calcular y devolver el precio del producto"""
    def calcular(self, quantity_product):

        total_price = super().calcular(quantity_product)

        match self.day_expiration:

            case 1:
                total_price = total_price / 4
            
            case 2:
                total_price = total_price / 3

            case 3:
                total_price = total_price / 2

        return total_price
    
    """Funcion encargada de devolver la informacion del producto perecedero"""
    def __str__(self):

        return super().__str__() + " - " + str(self.day_expiration) + " days"