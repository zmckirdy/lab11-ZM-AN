import math

def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError("Error: Argument cannot be less than 0.")

def hypoteneuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract (a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Error: Cannot divide by 0.")
    else:
        return b / a

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Error: Logarithm's argument must be greater than 0.")
    elif b <= 0:
        raise ValueError("Error: Logarithm's base must be greater than 0.")
    elif b == 1:
        raise ValueError("Error: Logarithm's base cannot equal 1.")
    else:
        return math.log(a, b)

def exponent(a, b):
    return a ** b