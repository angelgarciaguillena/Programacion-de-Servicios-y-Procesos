"""Clase encargada de representar un articulo y sus funciones basicas"""
class Articulo:

    """Constante que representa el IVA"""
    VAT = 21

    """Constructor que inicializa los atributos de la clase Articulo comprobando
    que los valores son validos antes de asignarlos"""
    def __init__(self, name, price, stock):
        
        if name is not None and name != "":
            self.name = name

        if price > 0:  
            self.price = price
        
        if stock >= 0:
            self.stock = stock

    """Funcion encargada de calcular y devolver el precio del producto con el IVA
    incluido"""
    def getPVP(self):

        vat_price = (self.price * self.VAT) / 100
        pvp = self.price - vat_price

        return pvp

    """Funcion encargada de calcular y devolver el precio del producto con descuento"""
    def getPVPDescuento(self, discount):

        discount_price = (self.price * discount) / 100
        pvp_discount = self.getPVP() - discount_price

        return pvp_discount
    
    """Funcion que se encarga de realizar la venta de las unidades del articulo 
    si la cantidad introducida por parametroses se encuentra en el stock del articulo 
    y devuelve true si se ha realizado o false si no se ha realizado"""
    def vender(self, quantity_sales):

        correct = False

        if self.stock >= quantity_sales:
            self.stock -= quantity_sales
            correct = True

        return correct
    
    """Funcion que se encarga de añadir stock si la cantidad introducida 
    por parametroses mayor a 0 del articulo y devuelve true si se ha realizado 
    o false si no se ha realizado"""
    def almacenar(self, quantity_storage):

        correct = False

        if quantity_storage > 0:
            self.stock += quantity_storage
            correct = True

        return correct
    
    """Funcion encargada de devolver la informacion del articulo"""
    def __str__(self):
        
        string = "Name: " + self.name + "\n"
        string += "Price: " + str(self.price) + "\n"
        string += "Stock: " + str(self.stock) + "\n"

        return string
    
    """Funcion encargada de comprobar si dos articulos son iguales segun
    su nombre y devuelve true si son iguales o false si no son iguales"""
    def __eq__(self, object):

        equals = False

        if self.name == object.name:
            equals = True

        return equals
    
    """Funcion encargada de ordenar los articulos de menor a mayor
    segun su nombre"""
    def __lt__(self, object):

        minor = False

        if self.name < object.name:
            minor = True

        return minor