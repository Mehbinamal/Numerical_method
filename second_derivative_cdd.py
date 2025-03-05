import math

def second_derivative_cdd(f,x,h):
    return (f(x+h)-(2*f(x))+f(x-h))/(h**2)

def string_to_function(expression):
    return lambda x: eval(expression, {"x": x, "sin": math.sin, "cos": math.cos, "exp": math.exp, "log": math.log, "sqrt": math.sqrt})


input_function = input("Enter the function f(x) (use 'x' as the variable, e.g., 'sin(x)' or 'x**2 + 3*x + 2'): ")

f = string_to_function(input_function)

x = float(input("Enter the point x at which to compute the second derivative: "))
h = float(input("Enter the step size h (e.g., 0.01): "))

second_derivative = second_derivative_cdd(f, x, h)

print(f"The estimated second derivative of f(x) = {input_function} at x = {x} with h = {h} is: {second_derivative}")