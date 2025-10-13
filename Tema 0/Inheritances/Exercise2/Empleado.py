"""Clase encargada de representar un empleado y sus funciones basicas"""
class Empleado:

    """Constructor que inicializa los atributos de la clase Empleado comprobando
    que sus valores son validos antes de asignarlos"""
    def __init__(self, name):
        
        if name is not None and name != "":
            self.name = name
        else:
            self.name = "Anonymous"

    """Funcion encargada de devolver el nombre del empleado"""
    def getName(self):

        return self.name
    
    """Funcion encargada de modificar el nombre del empleado mientras
    el valor que se va a modificar sea valido"""
    def setName(self, name):

        if name is not None and name != "":
            self.name = name

    """Funcion encargada de devolver la informacion del empleado"""
    def __str__(self):

        return "Empleado " + self.name