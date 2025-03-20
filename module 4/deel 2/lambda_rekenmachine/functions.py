def addition(number1, number2):
    return float(number1 + number2)

def subtraction(number1, number2):
    return float(number1 - number2)

def multiplication(number1, number2):
    return float(number1 * number2)

def division(number1, number2):
    if number2 == 0:
        return "Error: Kan niet delen door nul"
    return float(number1 / number2)

dict = {}