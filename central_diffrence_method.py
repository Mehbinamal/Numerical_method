import math

def f(x):
    return math.sin(x)

def central_diffrence (f,x,h):
    return ((f(x+h)-f(x-h))/(2*h))

x = math.pi /4
h = 0.05

derivative = central_diffrence(f,x,h)

print(f"The estimated derivative of sin(x) at x = π/4 with h = 0.05 is: {derivative}")