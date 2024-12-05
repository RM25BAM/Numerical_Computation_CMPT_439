import numpy as np
def is_dominant(matrix):
    for i in range(matrix.shape[0]):
        if abs(matrix[i, i]) < sum(abs(matrix[i, j]) for j in range(matrix.shape[0]) if i != j):
            return False
    return True
def jacobi(matrix, tol, stop_crit):
    size = matrix.shape[0]
    A, b = matrix[:, :-1], matrix[:, -1]
    if not is_dominant(A):
        print("Matrix is not diagonally dominant.")
        return None
    x = np.ones(size)
    while True:
        x_new = np.zeros(size)
        for i in range(size):
            x_new[i] = (b[i] - sum(A[i, j] * x[j] for j in range(size) if j != i)) / A[i, i]
        error = np.mean(np.abs(x_new - x)) if stop_crit == "MAE" else np.sqrt(np.mean((x_new - x)**2))
        if error < tol:
            break
        x = x_new
    return x
def gauss_seidel(matrix, tol, stop_crit):
    size = matrix.shape[0]
    A, b = matrix[:, :-1], matrix[:, -1]
    if not is_dominant(A):
        print("Matrix is not diagonally dominant.")
        return None
    x = np.ones(size)
    while True:
        x_old = x.copy()
        for i in range(size):
            x[i] = (b[i] - sum(A[i, j] * x[j] for j in range(size) if j != i)) / A[i, i]

        error = np.mean(np.abs(x - x_old)) if stop_crit == "MAE" else np.sqrt(np.mean((x - x_old)**2))
        if error < tol:
            break
    return x
if __name__ == "__main__":
    augmented = np.array([
        [1, -2, 4, 6],
        [8, -3, 2, 2],
        [-1, 10, 5, 4]
    ], dtype=float)
    tolerance = 0.001
    print("Jacobi Solution:")
    print(jacobi(augmented, tolerance, "MAE"))
    print(jacobi(augmented, tolerance, "RMSE"))
    print("Gauss-Seidel Solution:")
    print(gauss_seidel(augmented, tolerance, "MAE"))
    print(gauss_seidel(augmented, tolerance, "RMSE"))