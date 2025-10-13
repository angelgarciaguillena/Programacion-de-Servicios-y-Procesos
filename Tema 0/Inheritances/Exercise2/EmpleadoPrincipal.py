#Impoprtamos la clase Tecnico
from Tecnico import *

#Importamos la clase Oficial
from Oficial import * 

#Importamos la clase Directivo
from Directivo import *

#Importamos la clase Operaro
from Operario import *

#Importamos la clase Empleado
from Empleado import *

#Creamos un empleado
employee = Empleado("Rafa")

#Creamos un directivo
executive = Directivo("Mario")

#Creamos un operario
operator = Operario("Alfonso")

#Creamos un oficial
official = Oficial("Luis")

#Creamos un tecnico
technician = Tecnico("Pablo")

#Mostramos la informacion de los empleados
print("\n" + "Employees:")

#Mostramos la informacion del empleado
print(employee.__str__())

#Mostramos la informacion del directivo
print(executive.__str__())

#Mostramos la informacion del operario
print(operator.__str__())

#Mostramos la informacion del oficial
print(official.__str__())

#Mostramos la informacion del tecnico
print(technician.__str__())