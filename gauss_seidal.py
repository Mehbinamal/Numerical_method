import numpy as np

def guass_seidal(A,b,x0=None, tol= 1e-10, max_iter = 100):
    n = len(b)
    x = np.zeros(n) if x0 is None else np.copy(x0)

    for iter_count in range(max_iter):
        x_new =  np.copy(x)
        for i in range(n):
            sigma = sum(A[i][j] * x_new[j] for j in range(n) if j!= i)
            x_new[i] = (b[i] - sigma)/A[i][i]
        
        if np.linalg.norm(x_new - x) < tol:
            return x_new ,iter_count +1
        
        x = x_new
    
    print("Warning: Maximum iterations reached without convergence.")
    return x, max_iter

def get_input():
    print("Enter the number of variables (n):")
    n = int(input())  # Number of variables
    
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    print(f"Enter the coefficients of the matrix A ({n}x{n}):")
    for i in range(n):
        row = input(f"Row {i+1} (enter {n} numbers separated by space): ").split()
        A[i] = list(map(float, row))
    
    print(f"Enter the right-hand side vector b ({n} values):")
    b = list(map(float, input().split()))
    
    return A, b

A, b = get_input()


x_solution, iterations = guass_seidal(A, b)
print(f"Solution: {x_solution}")
print(f"Iterations: {iterations}")