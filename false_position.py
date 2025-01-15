def find_sign_change(f, max_x=100):
    prev_value = f(0)
    for x in range(1, max_x + 1):
        current_value = f(x)
        if prev_value * current_value < 0:
            if prev_value < current_value:
                return x - 1, x
            else:
                return x, x - 1
        prev_value = current_value
    return None, None  

def false_position_method(f):
    a, b = find_sign_change(f)
    if a is None or b is None:
        print("No sign change found.")
        return
    
    for i in range(100):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        
        if abs(f(c)) < 1e-6:  
            print("Root = ", c)
            return
        
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    print("No root found after 100 iterations.")

def polynomial(x):
    return x**3 - x - 2

false_position_method(polynomial)  
