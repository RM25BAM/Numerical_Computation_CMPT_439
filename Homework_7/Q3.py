import os, numpy as np, matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-pastel')
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return coef

def newton_poly(coef, x_data, x):
    n = len(x_data) - 1 
    m = coef[n]
    for k in range(1, n + 1):
        m = coef[n - k] + (x - x_data[n - k]) * m
    return m

def plot_interpolation(x, y, z, interpolated_value, figure_name):
    x_range = np.linspace(min(x), max(x), 500)
    divided_diffs = divided_diff(x, y)[0, :]
    y_range = [newton_poly(divided_diffs, x, xi) for xi in x_range]
    output_dir = f'./Homework_7/Screenshot/Problem_c'
    os.makedirs(output_dir, exist_ok=True)
    plt.plot(x_range, y_range, label="Newton Interpolating Polynomial", linestyle="--", linewidth=1)
    plt.scatter(x, y, color="red", label="Given Points", s=30)
    plt.scatter(z, interpolated_value, color="blue", label=f"Interpolated value at z = {z}", marker='x', s=50)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Newton Interpolation")
    plt.legend(loc="best")
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, f"{figure_name}.png"))
    plt.clf()

def main():
    while True:
        print("Newton's Interpolation")
        x = list(map(float, input("Enter the x-coordinates (comma-separated): ").split(',')))
        f = list(map(float, input("Enter the corresponding y-coordinates (comma-separated): ").split(',')))
        
        if len(x) != len(f):
            print("Error: The x and y arrays must have the same number of elements.")
            continue
        z = float(input("Enter the point at which you want to interpolate: "))
        cases = [
            ("First_Run", x[:3], f[:3]),
            ("Second_Run", x[:4], f[:4]),
            ("Third_Run", x[1:], f[1:]),
            ("Fourth_Run", x, f)
        ]
        for label, x_subset, y_subset in cases:
            divided_diffs = divided_diff(x_subset, y_subset)[0, :]
            val = newton_poly(divided_diffs, x_subset, z)
            plot_interpolation(x_subset, y_subset, z, val, figure_name=label)
            print(f"Interpolated value at {z} with '{label.replace('_', ' ')}' points: {val}\n")
        cont = input('Would you like to continue:(Y/N) ')
        if cont == 'N' or cont == 'n':
            break
        if cont == 'Y' or cont == 'y':
            continue
main()
