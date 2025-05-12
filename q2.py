
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Can't divide by Zero"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

calc = Calculator()
if op == "+":
    print("Result:", calc.add(a, b))
elif op == "-":
    print("Result:", calc.subtract(a, b))
elif op == "*":
    print("Result:", calc.multiply(a, b))
elif op == "/":
    print("Result:", calc.divide(a, b))
else:
    print("Invalid operation")
