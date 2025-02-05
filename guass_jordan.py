import numpy as np

def Gauss_Jordan(A):
    n = len(A)
    
    for i in range(n):
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[[i, max_row]] = A[[max_row, i]]
        
        A[i] = A[i] / A[i][i]
        
        for j in range(n):
            if i != j:  
                factor = A[j][i]
                A[j] -= factor * A[i]
    return A[:, -1]

def input_matrix():
    n = int(input("Enter number of Equations :"))
    A = []
    print("Enter coefficient & constant terms:")
    for i in range(n):
        row = list(map(float, input(f"Row {i+1} (Space separated values): ").split()))
        A.append(row)
    return np.array(A, dtype=float)

A = input_matrix()

solution = Gauss_Jordan(A)
print("Solution =", solution)
