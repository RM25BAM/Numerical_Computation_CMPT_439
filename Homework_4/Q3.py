import numpy as np , Q1
def main():
    row = int(input("Enter the number of rows:"))
    column = int(input("Enter the number of columns:"))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(int, input().split()))
    matrix = np.array(entries).reshape(row, column)
    print(f"\n{matrix}\n")
    cramer_sol = Q1.cramer(matrix) 
    print(cramer_sol)
main()
