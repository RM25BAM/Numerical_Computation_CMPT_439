import numpy as np
def gauss_Elimination(X):
    n = X.shape[0] # get the rows and the column
    for i in range(n-1): # iterate but ignore the last one 
        o = np.argmax(abs(X[i:n, i])) + i  # Find the pivot (max element)
        if X[o, i] == 0:  # If the pivot is zero
            return None # return the value as None
        # Swap the current row with the pivot row
        if o != i: # pivot not equal to i
            X[[i, p]] = X[[o, i]] # swap val
        for j in range(i+1, n):  # take out entry below pivot
            m = X[j, i] / X[i, i]  # Multiplier
            X[j, i:] = X[j, i:] - m * X[i, i:]  # Eliminate the x-term from row j
    # Back substitution implementation
    x = np.zeros(n) # make a array Numpy with n # of elements
    if X[n-1, n-1] == 0:  # If the last pivot is zero, there's no unique solution
        return None # return None val
    x[n-1] = X[n-1, n] / X[n-1, n-1]  # Solvelast variable (z, xn-1)
    for i in range(n-2, -1, -1): # solve for the rest of the variables
        sum_val = 0 # max sum
        for j in range(i+1, n): # for loop iteration 
            sum_val += X[i, j] * x[j] 
        x[i] = (X[i, n] - sum_val) / X[i, i]
    return x # return x
