# https://github.com/zmckirdy/lab11-ZM-AN.git
# Partner 1: Zach McKirdy
# Partner 2: Aditya Nair

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

def sub(a, b):
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    return b / a 

def log(a, b): 
    return math.log(b,a)

def exp(a, b): 
    return a^b

def subtract (a, b):
    return a - b

def multiply(a, b):
    return a * b


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
