import numpy as np
import matplotlib.pyplot as plt
import os

def fun_input(expression):
    return eval("lambda x: " + expression) 

def Lagrange(z, x, f):
    n = len(x)
    Interpolated_Value = 0 
    for i in range(n):
        Lagrangian = 1  
        for j in range(n):
            if j != i:
                Lagrangian *= ((z - x[j]) / (x[i] - x[j])) 
        Interpolated_Value += Lagrangian * f[i]  
    return Interpolated_Value

def plot_interpolation(x, f, z, interpolated_value, figure_name="Interpolating_Polynomial"):
    x_range = np.linspace(min(x), max(x), 500)
    y_range = [Lagrange(xi, x, f) for xi in x_range]
    output_dir = './Homework_7/Screenshot/Problem_a'
    os.makedirs(output_dir, exist_ok=True)
    plt.plot(x_range, y_range, label="Lagrange Interpolating Polynomial", linestyle="--")
    plt.scatter(x, f, color="red", label="Given Points")  
    plt.scatter(z, interpolated_value, color="blue", label=f"Interpolated value at z = {z}", marker='x', s=100) 
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Lagrange Interpolation")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, figure_name))

def main():
    print("Lagrange Interpolation")
    x = list(map(float, input("Enter the x-coordinates (comma-separated): ").split(',')))
    f = list(map(float, input("Enter the corresponding y-coordinates (comma-separated): ").split(',')))
    if len(x) != len(f):
        print("Error: The x and y arrays must have the same number of elements.")
        return main()
    z = float(input("Enter the point at which you want to interpolate: "))
    interpolated_value = Lagrange(z, x, f)
    print("\nLagrange Interpolation Results")
    print("____________________________________\n")
    print(f"x-coordinates: {x}")
    print(f"y-coordinates: {f}")
    print(f"Interpolated value at {z}: {interpolated_value}\n")
    plot_interpolation(x, f, z, interpolated_value)
main()
