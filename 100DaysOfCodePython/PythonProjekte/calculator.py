from arts.calculator_art import logo

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

# print(operations["*"](4, 8))

def calc():
    print(logo)
    repeat = True
    num1 = float(input("What's the first number?: "))

    while repeat:
        for symbol in operations:
            print(symbol)
        op = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operations[op](num1, num2)
        print(f"{num1} {op} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = result
        else:
            repeat = False
            print("\n" * 20)
            calc()

calc()