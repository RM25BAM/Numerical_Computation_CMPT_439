import numpy as np
import gauss
def main():
    v = int(input("Enter the number of variables (v): "))
    X = np.zeros((v, v + 1))
    print("Enter the augmented matrix (each row as space-separated values, including the right-hand side):")
    for i in range(v):
        row = list(map(float, input(f"Enter row {i + 1}: ").split()))
        X[i, :] = row
    result = gauss.gauss_Elimination(X)
    if result is not None:
        print(f"Solution: {result}")
    else:
        print("No unique solution") 
main()
