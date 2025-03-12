def euler_method(f, x0, y0, x_end, h):
    x_values = [x0]
    y_values = [y0]

    n = int((x_end - x0) / h)

    x = x0
    y = y0

    for i in range(n):
        y += h * f(x, y) 
        x += h  
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

def create_function_from_input(function_input):
    return lambda x, y: eval(function_input)

function_input = input("Enter the function f(x, y) for dy/dx (e.g., 'x + y'): ")

f = create_function_from_input(function_input)


x0 = float(input("Enter the initial value of x (x0): "))
y0 = float(input("Enter the initial value of y (y0): "))
x_end = float(input("Enter the final value of x (x_end): "))
h = float(input("Enter the step size (h): "))


x_values, y_values = euler_method(f, x0, y0, x_end, h)

print("\nApproximate solution using Euler's method:")
print(f"{'x':>10} {'y':>10}")
for x, y in zip(x_values, y_values):
    print(f"{x:10.4f} {y:10.4f}")
