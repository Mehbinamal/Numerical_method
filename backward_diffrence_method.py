import math

def f(expression, x):
    if expression == 'e^x':
        return math.exp(x)
    else:
        return eval(expression)

def backward_difference(expression, x, h):
    return (f(expression, x) - f(expression, x-h)) / h

equation = input("Enter the equation (use 'x' for variable, e.g., 'x**3 + 2*x**2 - 5*x + 7'): ")
x = float(input("Enter the value of x: "))
h = float(input("Enter the step size h: "))


derivative = backward_difference(equation, x, h)

print(f"The derivative of {equation} at x = {x} with step size h = {h} is approximately {derivative}")