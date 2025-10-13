"""Clase encargada de representar una Cuenta Corriente y sus funciones basicas"""
class CuentaCorriente:

    """Constructor que inicializa el dni y el saldo la clase Cuenta Corriente comprobando
    que los valores son validos antes de asignarlos"""
    def __init__(self, dni, balance):

        if dni is not None and dni != "" and len(dni) == 9:
            self.dni = dni
            
        if balance is not None and balance >= 0:
            self.balance = balance
    
    """Constructor que inicializa los atributos de la clase Cuenta Corriente comprobando
    que los valores son validos antes de asignarlos"""
    def __init__(self, dni, name, balance):
        
        if dni is not None and dni != "" and len(dni) == 9:
            self.dni = dni
            
        if name is not None and name != "":
            self.name = name

        if balance is not None and balance >= 0:
            self.balance = balance

    """Funcion encargada de sacar dinero en la cuenta del usuario mientras
    que haya saldo en la cuenta y devuelve true si la operacion es correcta 
    o false si la operacion no se ha podido realizar"""
    def withdraw_money(self, money):

        correct = False

        if self.balance > money:
            self.balance -= money
            correct = True

        return correct
    
    """Funcion encargada de depositar dinero enla cuenta del usuario mientras
    que el saldo introducido por el usuario sea mayor a 0 y devuelve true si 
    la operacion es correcta o false si la operacion no se ha podido realizar"""
    def deposit_money(self, money):

        correct = False

        if money > 0:
            self.balance += money
            correct = True

        return correct

    """Funcion encargada de devolver los datos de la cuenta corriente"""
    def __str__(self):

        string = "DNI: " + self.dni + "\n"
        string += "Name: " + self.name + "\n"
        string += "Balance: " + str(self.balance) + "\n"

        return string
    
    """Funcion encargada de comprobar si dos cuentas corrientes son iguales segun
    su dni y devuelve true si son iguales o false si no son iguales"""
    def __eq__(self, object):

        equals = False

        if self.dni == object.dni:
            equals = True

        return equals
    
    """Funcion encargada de ordenar las cuentas corrientes de menor a mayor
    segun su saldo"""
    def __lt__(self, object):
        
        minor = False

        if self.balance < object.balance:
            minor = True

        return minor