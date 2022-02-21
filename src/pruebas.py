from datetime import date
from mailbox import NoSuchMailboxError

sum = 1 + 2
product = sum * 2
print("El resultado de la operacion es: ", product)

print(type(product))

date.today()
print("Today's date is: " + str(date.today()))

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

print("\n------------------------------------\n")
print("Calculadora")
firstNum = input("Primer numero: ")
secondtNum = input("Segundo numero: ")
print(int(firstNum) + int(secondtNum))