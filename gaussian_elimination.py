import numpy as np

def Gaussian_Elimination(A):
    n = len(A)
    
    for i in range(n):
        max_row = i
        for k in range(i+1,n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[[i,max_row]] = A[[max_row,i]]
        

        for j in range(i+1,n):
            factor = A[j][i] /A[i][i]
            A[j] -= factor*A[i]
    
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        x[i] = (A[i][-1] - np.dot(A[i][i+1:n],x[i+1:n]) )/A[i][i]
    return x
# Example usage
A = np.array([
    [2,1,-1,8],
    [-3,-1,2,-11],
    [-2,1,2,-3]
],dtype=float)

def input_matrix():
    n = int(input("Enter number of Equations :"))
    A = []
    print("enter coefficient & Constant terms :")
    for i in range(n):
        row = list(map(float,input(f"Row {i+1} (Space seperated Values) :").split()))
        A.append(row)
    return np.array(A, dtype=float)


A = input_matrix()

solution = Gaussian_Elimination(A)
print("Solution =",solution)

