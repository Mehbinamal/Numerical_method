import math

def evaluate_expression(expression, x):
    return eval(expression)

def forward_difference(expression, x, h):
    return (evaluate_expression(expression, x + h) - evaluate_expression(expression, x)) / h

equation = input("Enter the equation (use 'x' for variable, e.g., 'x**3 + 2*x**2 - 5*x + 7'): ")
x = float(input("Enter the value of x: "))
h = float(input("Enter the step size h: "))


derivative = forward_difference(equation, x, h)

print(f"The derivative of {equation} at x = {x} with step size h = {h} is approximately {derivative}")