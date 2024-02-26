



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b


operations = { "+": add, "-": subtract, "*": multiply, "/": divide, "**": power}

def constructOperatorString():
    operatorString = " The operations are: \n"
    for operator, v in operations.items():
        operatorString += operator + " \n"
    return operatorString

def calculator():
    f_number = input("Enter the first number: ")
    operation = input(f"Enter the operation: {constructOperatorString()} \n Pick the operation: ").lower()
    s_number = input("Enter the second number: ")

    #print(calculate(float(f_number),operation, float(s_number)))
    function = operations[operation]
    result = function(float(f_number), float(s_number))
    print(result)
    choice = ""
    choice = input("Use the previous result as the first number for the next operation type 'yes' to continue or 'no' to stop")
    if choice == "yes":
        continuity = True
        while continuity:
            f_number = result
            operation = input(f"Enter the operation: {constructOperatorString()} \n Pick the operation: ").lower()
            t_number = input("Enter the third number: ")
            function = operations[operation]
            result = function(f_number, float(t_number))
            print(result)
            choice = input("Do you want to continue to use the first number for the next operation type 'y' to continue or 'n' to stop or 'g' to go back to a new calculation")
            if choice == "n":
                continuity = False
                break
            elif choice == "g":
                calculator()
    else:
        print("Goodbye")
calculator()