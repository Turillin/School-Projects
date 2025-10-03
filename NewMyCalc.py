def NewCalc():
    while True: # While the statement is true of input number and operators, the loop will continue indefinitely.
        a = (input("Enter first number or type 'q' to quit: "))
        if a == "q":
            print("Calculator is now closed")
            break
        elif a == "": # If the user inputs nothing, they get a message about it here
            print("There is nothing to calculate")
            print("Try again")
        try:
            a = float(a)
        except ValueError:
            print("Invalid input, please enter a number")
            continue # Here, if the error does occur, we rerun the loop from the start.
        operator = input("Enter operator (+, -, *, /): ")
        try:
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, please enter a number")
            continue # Same thing here. if an error is raised, the loop starts over

# Below , with the help of the if, elif and else statements we can control
# that the correct functions is called back to. This method makes the code easier to read and maintain.
        
        if operator == "+":
            result = add(a, b)
            print(result)
        elif operator == "-":
            result = subtract(a, b)
            print(result)
        elif operator == "*":
            result = multiply(a, b)
            print(result)
        elif operator == "/":
            try:
                result = divide(a, b)
            except ZeroDivisionError:
                print("You cannot divide by zero")
                print("Try again")
                continue
            print(result)
        else:
            print((f"{operator} is not an operator"))
            continue
# could potentially include an if not statement here to catch invalid operators and start the loop over again.🤔
# I keep getting ValueError: could not convert string to float: everytime i rerun the code a second time.
# find a way to fix this. 
# ValueError is now fixed, it all happened because of not enough try and except blocks were used in the beginning.

# We call back the functions bellow everytime we want to calculate 2 numbers with a specific operator
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

# def compute(a,b,operator):
#     if operator == "+":
#         return a + b

# Potential function to use if id want to make the ones above shorter

# command + shift + 7 = comment mode
NewCalc()