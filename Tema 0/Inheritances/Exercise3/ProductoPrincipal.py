#Importamos la clase Perecedero
from Perecedero import *

#Importamos la clase NoPerecedero
from NoPerecedero import *

#Creamos un producto perecedero
perishable_product = Perecedero("Yogurt", 5, 2)

#Creamos un producto no perecedero
non_perishable_product = NoPerecedero("Water Bottle", 2.5, "Drinks")

#Mostramos la informacion del producto perecedero
print("\n" + "Perishable product:")
print(perishable_product.__str__())

#Mostramos el precio del total del producto perecedero
print("The total price of the perishable product is:", str(perishable_product.calcular(2)) + "€")

#Mostramos la informacion del producto no perecedero
print("\n" + "Non-perishable product:")
print(non_perishable_product.__str__())

#Mostramos el precio del total del producto no perecedero
print("The total price of the non-perishable product is:", str(non_perishable_product.calcular(2)) + "€")