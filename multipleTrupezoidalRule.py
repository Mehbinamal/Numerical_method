def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)
    
    for i in range(1, n):
        integral += 2 * f(a + i * h)

    integral *= h / 2

    return integral

def create_function_from_input(function_input):
    return lambda x: eval(function_input)

function_input = input("Enter the function to integrate (use 'x' as the variable): ")

f = create_function_from_input(function_input)

a = float(input("Enter the lower limit of integration (a): "))
b = float(input("Enter the upper limit of integration (b): "))
n = int(input("Enter the number of subintervals (n): "))

result = trapezoidal_rule(f, a, b, n)

print(f"Approximate integral: {result}")
