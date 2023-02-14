def add(num1, num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate():
    
    num1 = float(input("Enter your first number: "))
    
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operator = input("Pick the operator: ")
        num2 = float(input("Enter your second number: "))
        calculate = operations[operator]
        answer = calculate(num1,num2)
        
        print(f"{num1} {operator} {num2} = {answer}")
        
        if input("if you want to continue then please enter 'y' or enter 'n' to close: ") == 'y':
            should_continue = True
            num1 = answer
        else:
            should_continue = False
            print("Goodbye!")
    
calculate()