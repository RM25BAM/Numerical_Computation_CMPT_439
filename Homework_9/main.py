import numpy as np
import matplotlib.pyplot as plt
import os
from tabulate import tabulate
from trapezoidal_rule import trapezoidal_rule
from simpson_rule import simpsons_rule
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
def find_missing_points(x_values, step_size):
    missing_points = []
    x_values_sorted = sorted(x_values)
    for i in range(len(x_values_sorted) - 1):
        current = x_values_sorted[i]
        next_expected = current + step_size
        while next_expected < x_values_sorted[i + 1]:
            missing_points.append(next_expected)
            next_expected += step_size
    return missing_points
def plot_results(x, f, missing_points, interpolated_values, trapezoidal_result, simpsons_result, figure_name = "Graph"):
    output_dir = "./Screenshot"
    os.makedirs(output_dir, exist_ok=True)
    x_range = np.linspace(min(x), max(x), 500)
    y_range = [Lagrange(xi, x, f) for xi in x_range]
    plt.figure(figsize=(12, 8))
    plt.plot(x_range, y_range, label="Lagrange Polynomial Curve", linestyle="--", color="green")
    plt.scatter(x, f, color="red", label="Given Points")
    plt.scatter(missing_points, interpolated_values, color="blue", label="Interpolated Points", marker='x', s=100)
    for i in range(len(x) - 1):
        plt.fill_between([x[i], x[i+1]], [f[i], f[i+1]], color="yellow", alpha=0.3, label="Trapezoids" if i == 0 else "")
    for i in range(0, len(x) - 1, 2):
        x_segment = x[i:i+3] 
        y_segment = [f[i], f[i+1], f[i+2]]
        x_range_simpson = np.linspace(x_segment[0], x_segment[-1], 100)
        y_range_simpson = [Lagrange(xi, x_segment, y_segment) for xi in x_range_simpson]
        plt.plot(x_range_simpson, y_range_simpson, label="Simpson's Rule Segment" if i == 0 else "", color="orange")
    plt.title("Interpolation and Numerical Integration")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, figure_name))
    plt.show()
def main():
    x = list(map(float, input("Enter x values separated by spaces: ").split()))
    y = list(map(float, input("Enter corresponding f(x) values separated by spaces: ").split()))
    if len(x) != len(y):
        raise ValueError("The number of x values must match the number of f(x) values.")
    h = float(input("Enter the step size (h): "))
    missing_points = find_missing_points(x, h)
    print("\nInterpolating missing points...")
    interpolated_values = [Lagrange(round(point, 4), x, y) for point in missing_points]
    for point, value in zip(missing_points, interpolated_values):
        print(f"Interpolated f({point:.1f}) = {value:.4f}")
    x += missing_points
    y += interpolated_values
    x, y = zip(*sorted(zip(x, y)))
    trapezoidal_result = trapezoidal_rule(h, x, y)
    print(f"\nTrapezoidal Rule Result: {trapezoidal_result:.4f}")
    try:
        simpsons_result = simpsons_rule(h, x, y)
        print(f"Simpson's Rule Result: {simpsons_result:.4f}")
    except ValueError as e:
        simpsons_result = None
        print(e)
    data_table = [["x", "f(x)"]] + [[xi, yi] for xi, yi in zip(x, y)]
    print("\nData Table:")
    print(tabulate(data_table, headers="firstrow", tablefmt="grid"))

    results_table = [
        ["Method", "Result"],
        ["Trapezoidal Rule", trapezoidal_result],
        ["Simpson's Rule", simpsons_result if simpsons_result is not None else "N/A"]
    ]
    print("\nIntegration Results:")
    print(tabulate(results_table, headers="firstrow", tablefmt="fancy_grid"))
    print("\n{:-^50}".format(" Plotting Results "))
    plot_results(x, y, missing_points, interpolated_values, trapezoidal_result, simpsons_result)
main()
