"""Importamos la clase math"""
import math

"""Creamos la clase Punto encargada de representar un punto cardinal
y sus funciones basicas"""
class Punto:

    """Constructor que inicializa los atributos de clase Punto"""
    def __init__(self, x, y):

        self.x = x
        self.y = y

    """Metodo que modifica las coordenadas x e y de un punto"""
    def setXY(self, x, y):

        self.x = x
        self.y = y

    """Funcion encargada de desplazar el punto hacia la cantidad que se le 
    ha indicado por parametros"""
    def desplaza(self, dx, dy):

        self.x += dx
        self.y += dy 
    
    """Funcion encargada de calcular y devolver la distancia que existe 
    entre dos puntos"""
    def distancia(self, punto):

        dx = punto.x - self.x
        dy = punto.y - self.y

        distance = math.sqrt(dx ** 2 + dy ** 2)

        return distance
    
    """Funcion encargada de devolver la informacion de un objeto Punto"""
    def __str__(self):

        return ("(" + str(self.x) + "," + str(self.y) + ")" + "\n")