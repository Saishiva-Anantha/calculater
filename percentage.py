def percentage(num1, num2):
    try:
        result = (num1 / num2) * 100
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None