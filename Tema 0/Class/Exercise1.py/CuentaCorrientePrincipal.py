#Importamos la clase CuentaCorriente
from CuentaCorriente import *

#Creamos una cuenta corriente
account = CuentaCorriente("12345678A", "Angel", 120)

#Creamos otra cuenta corriente
account2 = CuentaCorriente("87654321A", "Angel", 120)

#Sacamos 200€ de la cuenta
correct = account.withdraw_money(200)

#Mostramos si la operacion se ha realizado
print(correct)

#Mostramos la informacion de la cuenta
print("\n" + "Account:")
print(account.__str__())

#Depositamos dinero en la cuenta
correct = account.deposit_money(-4)

#Mostramos si la operacion se ha realizado
print(correct)

#Mostramos la informacion de la cuenta
print("\n" + "Account:")
print(account.__str__())

#Comprobamos si las cuentas son iguales
equals = account.__eq__(account2)

#Mostramos si las cuentas son iguales
print(equals)