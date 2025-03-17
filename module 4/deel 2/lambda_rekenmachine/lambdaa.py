calculations = {
    "add": lambda num1, num2: int(num1 + num2),
    "subtract": lambda num1, num2: int(num1 - num2),
    "multiply": lambda num1, num2: int(num1 * num2),
    "divide": lambda num1, num2: "Error: Cannot divide by zero" if num2 == 0 else (int(num1 / num2) if num1 % num2 == 0 else num1 / num2)
}