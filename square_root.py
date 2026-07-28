def square_root(num):
    if num < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return num ** 0.5