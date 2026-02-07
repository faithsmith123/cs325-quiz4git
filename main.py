
         # 🔴 LINE TO RENAME LATER



def multiply(a, b):
    return a * b

        



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operator"

print("Result:", result)
