import numpy as np

def gauss_elimination(A):
    
    n = A.shape[0]  
    for i in range(n-1):
        p = i
        for j in range(i+1, n):
            if abs(A[j, i]) > abs(A[i, i]):
                A[[i, j]] = A[[j, i]]
        while (A[p, i] == 0 and p < n):
            p += 1
        if p == n:
            print('No unique solution')
            return None
        else:
            if p != i:
                A[[i, p]] = A[[p, i]]
        for j in range(i+1, n):
            m = A[j, i] / A[i, i]  
            A[j, i:] = A[j, i:] - m * A[i, i:] 
    if A[n-1, n-1] == 0:
        print('No unique solution')
        return None
    x = np.zeros(n)
    x[n-1] = A[n-1, n] / A[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i, j] * x[j]
        x[i] = (A[i, n] - sum_ax) / A[i, i]

    return x
