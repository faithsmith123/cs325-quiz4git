def add_function(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
            
        



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")

if operator == "+":
    result = add_function(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operator"

print("Result:", result)

