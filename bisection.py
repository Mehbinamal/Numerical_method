import random
import math

# Function to apply the transformation g(x) = f(x) + x
def g(x, f):
    return f(x) + x  

# Bisection method to find the root of g(x) in interval [a, b]
def bisection_method(func, a, b, tol=1e-5, max_iter=100):
    # Check if the function has a different sign at the endpoints
    if func(a) * func(b) > 0:
        print("The bisection method requires a sign change in the interval.")
        return None
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        # Calculate the midpoint of the interval
        c = (a + b) / 2
        
        # If the midpoint is the root
        if func(c) == 0:  
            return c
        # Narrow the interval
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        
        iter_count += 1
    
    return (a + b) / 2

# Get user input for the function
user_input_function = input("Enter a mathematical function f(x) (e.g., x**3 - x - 2): ")

# Define the function f(x) using eval() with safety consideration for mathematical functions
def f(x):
    try:
        return eval(user_input_function)
    except Exception as e:
        print(f"Error in evaluating the function: {e}")
        return None

# Define the interval [a, b]
a = int(input("enter interval:"))
b =  int(input("enter interval:"))

# Ensure that a is less than b
if a > b:
    a, b = b, a

print(f"Interval: [{a}, {b}]")

# Define the transformed function g(x) = f(x) + x
def g_lambda(x):
    result = f(x)
    if result is None:
        return None  # Return None if function evaluation fails
    return result + x

# Find the root of g(x) using bisection method
root = bisection_method(g_lambda, a, b)

# Output the result
if root is not None:
    print(f"The root of the transformed function g(x) is: {root}")
    print(f"Corresponding zero of the original function f(x) is: {root}")
else:
    print("Root not found in the given interval.")
