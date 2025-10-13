#Importamos la clase Punto
from Punto import *

#Creamos un punto
point1 = Punto(2, 5)

#Creamos otro punto
point2 = Punto(8, 2)

#Modificamos las coordenadas del punto 1
point1.setXY(1, 1)

#Mostramos la informacion del punto 1
print("\n" + "Point:")
print(point1.__str__())

#Desplazamos el punto 1
point1.desplaza(2, 5)

#Mostramos la informacion del punto 1
print("Point:")
print(point1.__str__())

#Calculamos y mostramos la distancia entre el punto 1 y el punto 2
print(point1.distancia(point2))