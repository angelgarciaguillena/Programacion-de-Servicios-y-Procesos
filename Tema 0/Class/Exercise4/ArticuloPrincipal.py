#Importamos la clase Articulo
from Articulo import *

#Creamos un articulo
item1 = Articulo("PC", 50, 8)

#Creamos otro articulo
item2 = Articulo("Tablet", 20, 1)

#Mostramos el precio del artculo 1
print("Price of the item 1:", item1.getPVP())

#Mostramos el precio del artculo 1 con descuento
print("Price of the item 1 with discount:", item1.getPVPDescuento(20))

#Hacemos una venta en el articulo 1
print(item1.vender(8))

#Mostramos la informacion del articulo 1
print("\n" + "Item:")
print(item1.__str__())

#Hacemos una entrada de stock en el articulo 1
print(item1.almacenar(-2))

#Mostramos la informacion del articulo 1
print("\n" + "Item:")
print(item1.__str__())

#Mostramos si dos articulos son iguales
print(item1.__eq__(item2))