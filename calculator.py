# https://github.com/skoshy-sketch/lab-11-Sk_Ga
# Partner 1: Sam Koshy
# Partner 2: Gisele Amaral
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot calculate the square root of a negative number")


def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or b == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(a,b)


def exp(a, b):
    return a ** b

