# simple calculator with different differrent function 

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b


def calculate():
    try:
        a = eval(input("Enter first number:"))
        b = eval(input("Enter second number:"))
        operator = input("Enter operator(+, -, *, /)")

        if operator == "+":
            print(f"The sum of {a} and {b} are: {add(a, b)}")
        elif operator == "-":
            print(f"The subtraction of {a} and {b} are: {sub(a, b)}")
        elif operator == "*":
            print(f"The multiplication of {a} and {b} are: {mul(a, b)}")
        elif operator == "/":
            try:
                print(f"The division of {a} and {b} are: {div(a, b)}")
            except ZeroDivisionError:
                print("Cannot divide by zero.")
    except Exception as e:
        print(e)


calculate()