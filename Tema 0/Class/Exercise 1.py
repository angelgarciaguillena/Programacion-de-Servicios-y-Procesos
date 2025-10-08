class CuentaCorriente:
    def __init__(self, dni, balance):

        if dni is not None and dni != "" and len(dni) == 9:
            self.dni = dni
            
        if balance is not None and balance >= 0:
            self.balance = balance
    
    def __init__(self, dni, name, balance):
        
        if dni is not None and dni != "" and len(dni) == 9:
            self.dni = dni
            
        if name is not None and name != "":
            self.name = name

        if balance is not None and balance >= 0:
            self.balance = balance

    def withdraw_money(self, money):

        correct = False

        if self.balance > money:
            self.balance -= money
            correct = True

        return correct
    
    def deposit_money(self, money):

        correct = False

        if money > 0:
            self.balance += money
            correct = True

        return correct

    def __str__(self):

        string = "DNI: " + self.dni + "\n"
        string += "Name: " + self.name + "\n"
        string += "Balance: " + str(self.balance) + "\n"

        return string
    
    def __eq__(self, object):

        equals = False

        if self.dni == object.dni:
            equals = True

        return equals
    
    def __lt__(self, object):
        
        minor = False

        if self.balance < object.balance:
            minor = True

        return minor
    

if __name__ == "__main__":

    account = CuentaCorriente("12345678A", "Angel", 120)
    account2 = CuentaCorriente("87654321A", "Angel", 120)

    correct = account.withdraw_money(200)
    string = account.__str__()

    print(correct)
    print("\n" + "Account:")
    print(string)

    correct = account.deposit_money(-4)
    string = account.__str__()

    print(correct)
    print("\n" + "Account:")
    print(string)

    equals = account.__eq__(account2)
    print(equals)