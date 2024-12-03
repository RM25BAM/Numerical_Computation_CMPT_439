import numpy as np
def is_diagonally(X):
    n = X.shape[0]
    for i in range(n):
        sum_off_diag = np.sum(np.abs(X[i, :])) - np.abs(X[i, i])
        if np.abs(X[i, i]) < sum_off_diag:
            return False
    return True
def jacobi_method(matrix, tolerance, criteria):
    A = matrix[:, :-1]
    b = matrix[:, -1]
    
    n = A.shape[0]
    if not is_diagonally(A):
        print("Warning: Matrix is not diagonally dominant.")
    x = np.ones(n)
    x_new = np.zeros_like(x)
    error = np.inf
    while error > tolerance:
        for i in range(n):
            sum_other_terms = np.sum(A[i, :] * x) - A[i, i] * x[i]
            x_new[i] = (b[i] - sum_other_terms) / A[i, i]
        # Compute error based on the chosen criteria
        if criteria == 'MAE':
            error = np.mean(np.abs(x_new - x))
        elif criteria == 'RMSE':
            error = np.sqrt(np.mean((x_new - x)**2))
        else:
            raise ValueError("Invalid criterion. Choose 'MAE' or 'RMSE'.")
        x = x_new.copy()
    
    return x, error

# Gauss-Seidel Method for solving Ax = b
def gauss_seidel_method(matrix, tolerance, criteria):

    A = matrix[:, :-1]
    b = matrix[:, -1]
    
    n = A.shape[0]
    

    if not is_diagonally(A):
        print("Warning: Matrix is not diagonally dominant.")
    x = np.ones(n) # initial guess
    
    error = np.inf
    while error > tolerance:
        x_new = x.copy()
        for i in range(n):
            sum_other_terms = np.sum(A[i, :] * x_new) - A[i, i] * x_new[i]
            x_new[i] = (b[i] - sum_other_terms) / A[i, i]
        if criteria == 'MAE':
            error = np.mean(np.abs(x_new - x))
        elif criteria == 'RMSE':
            error = np.sqrt(np.mean((x_new - x)**2))
        else:
            raise ValueError("Invalid criterion. Choose 'MAE' or 'RMSE'.")
        
        x = x_new.copy()
    return x, error

def main():
    v = int(input("Enter the number of variables (v): "))
    X = np.zeros((v, v + 1))
    print("Enter the augmented matrix (each row as space-separated values, including the right-hand side):")
    for i in range(v):
        row = list(map(float, input(f"Enter row {i + 1}: ").split()))
        X[i, :] = row
    tolerance = float(input("Enter tolerance: "))
    criteria = input("Input for MAE and Input for RMSE:")
    print("\n--- Jacobi Method ---")
    x_jacobi, error_jacobi = jacobi_method(X, tolerance, criteria)
    print(f"Jacobi Method Solution: {x_jacobi}")
    print(f"Jacobi Method Error: {error_jacobi}")
    print("\n--- Gauss-Seidel Method ---")
    x_gauss_seidel, error_gauss_seidel = gauss_seidel_method(X, tolerance, criteria)
    print(f"Gauss-Seidel Method Solution: {x_gauss_seidel}")
    print(f"Gauss-Seidel Method Error: {error_gauss_seidel}")
main()