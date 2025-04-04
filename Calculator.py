def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "error"

def exponent(base, exp):
    return base ** exp

def squareroot(value):
    if value >= 0:
        return value ** 0.5
    else:
        return "error"

calculator = "Welcome to the calculator!"
print(calculator)

operation = input("Would you like to add, subtract, multiply, divide, use an exponent, or find the square root? Enter an option 1-6: ")

if operation in ['1', '2', '3', '4', '5', '6']:
    if operation == '6':
        value = float(input("Enter the number: "))
        print("Result:", squareroot(value))
    else:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if operation == '1':
            print("Result:", add(a, b))
        elif operation == '2':
            print("Result:", subtract(a, b))
        elif operation == '3':
            print("Result:", multiply(a, b))
        elif operation == '4':
            print("Result:", divide(a, b))
        elif operation == '5':
            print("Result:", exponent(a, b))
else:
    print("That's not an operation!!!!!")