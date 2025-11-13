"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
from math import *

def square_root(a):
    try:
        return sqrt(a)
    except ValueError:
        print("Value Error")

def hypotenuse(a, b):
    hypot(a, b)

# First example
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Zero Division Error")

def log(a, b):
    try:
        return log(b, a)
    except ValueError:
        print("Value Error")

def exp(a, b):
    return a ** b







