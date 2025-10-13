"""Clase encargada de representar un producto y sus funciones basicas"""
class Producto:

    """Constructor que inicializa los atributos de la clase Producto comprobando
    que sus valores son validos antes de asignarlos"""
    def __init__(self, name, price):
        
        if name is not None and name != "":
            self.name = name

        if price > 0:
            self.price = price

    """Funcion encargada de calcular y devolver el precio del producto"""
    def calcular(self, quantity_product):
        
        return self.price * quantity_product
    
    """Funcion encargada de devolver la informacion del producto"""
    def __str__(self):

        return self.name + " - " + str(self.price) + "€"
    
    """Funcion encargada de ordenar los productos de menor a mayor segun su nombre y devuelve true
    si el producto es menor o false si el producto es mayor"""
    def __lt__(self, object):

        minor = False

        if self.name < object.name:
            minor = True

        return minor