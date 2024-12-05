import numpy as np
def diagonally(X):
    n = X.shape[0]
    for i in range(n):
        sum_off_diag = np.sum(np.abs(X[i, :])) - np.abs(X[i, i])
        if np.abs(X[i, i]) < sum_off_diag:
            return False
    return True
def make_diagonally_dominant(X):
    n = X.shape[0]
    for i in range(n):
        max_row = np.argmax(np.abs(X[i:, i])) + i
        if max_row != i:
            X[[i, max_row]] = X[[max_row, i]]
    return X
def jacobi_method(matrix, tolerance, criteria):
    A = matrix[:, :-1]  
    b = matrix[:, -1] 
    matrix = make_diagonally_dominant(matrix)
    A = matrix[:, :-1]
    b = matrix[:, -1]
    if not diagonally(A):
        print("Warning: Matrix is not diagonally dominant. Convergence might not happen.")
    n = A.shape[0]
    x = np.zeros(n)
    error = np.inf
    while error > tolerance:
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_other_terms = np.sum(A[i, :] * x) - A[i, i] * x[i]
            x_new[i] = (b[i] - sum_other_terms) / A[i, i]
        if criteria == 'MAE':
            error = np.mean(np.abs(x_new - x))
        elif criteria == 'RMSE':
            error = np.sqrt(np.mean((x_new - x)**2))
        else:
            raise ValueError("Invalid criterion. Choose 'MAE' or 'RMSE'.")
        x = x_new.copy()
    return x
def gauss_seidel_method(matrix, tolerance, criteria):
    A = matrix[:, :-1]
    b = matrix[:, -1]
    matrix = make_diagonally_dominant(matrix)
    A = matrix[:, :-1]
    b = matrix[:, -1]
    if not diagonally(A):
        print("Warning: Matrix is not diagonally dominant. Convergence is not guaranteed.")
    n = A.shape[0]
    x = np.zeros(n)
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
        error = np.linalg.norm(x_new - x)
    return x

def main():
    v = int(input("Enter the number of variables (v): "))
    X = np.zeros((v, v + 1))  
    print("Enter the augmented matrix (each row as space-separated values, including the right-hand side):")
    for i in range(v):
        row = list(map(float, input(f"Enter row {i + 1}: ").split()))
        X[i, :] = row
    tolerance = float(input("Enter tolerance: "))
    criteria = input("Choose error criterion (MAE or RMSE): ")
    print("\n--- Jacobi Method ---")
    x_jacobi = jacobi_method(X, tolerance, criteria)
    print(f"Jacobi Method Solution: {x_jacobi}")
    print("\n--- Gauss-Seidel Method ---")
    x_gauss_seidel = gauss_seidel_method(X, tolerance, criteria)
    print(f"Gauss-Seidel Method Solution: {x_gauss_seidel}")
main()
