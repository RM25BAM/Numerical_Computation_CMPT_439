import numpy as np
import matplotlib.pyplot as plt
import os
def evaluate_function(x_value):
    return eval("lambda x: " + x_value, {"np": np, "sin": np.sin, "cos": np.cos})
def evaluate(func, x_value):
    return func(x_value)
def derivative_function(func, x, order=1):
    if order == 1:  # 1st der
        return (func(x + 1e-5) - func(x - 1e-5)) / (2 * 1e-5)
    elif order == 2:  # 2nd der
        return (func(x + 1e-5) - 2 * func(x) + func(x - 1e-5)) / (1e-5 ** 2)

# Newton's Method
def newton_method(func, x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        f_prime = derivative_function(func, x, order=1)
        f_double_prime = derivative_function(func, x, order=2)

        if f_double_prime == 0:
            raise ValueError("Zero second derivative encountered, cannot proceed.")

        x_new = x - f_prime / f_double_prime

        if abs(x_new - x) < tol:
            return x_new, evaluate(func, x_new), i + 1

        x = x_new

    raise ValueError("Newton's method did not converge within the maximum number of iterations.")

# Golden Section
def golden_section(func, a, b, tol=1e-6, minimize=True):
    phi = (1 + np.sqrt(5)) / 2
    inv_phi = 1 / phi

    x1 = b - (b - a) * inv_phi
    x2 = a + (b - a) * inv_phi

    f1 = func(x1)
    f2 = func(x2)

    iter_count = 0
    while abs(b - a) > tol:
        iter_count += 1
        if (f1 < f2 if minimize else f1 > f2):
            b, x2, f2 = x2, x1, f1
            x1 = b - (b - a) * inv_phi
            f1 = func(x1)
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + (b - a) * inv_phi
            f2 = func(x2)

    x_opt = (a + b) / 2
    return x_opt, func(x_opt), iter_count
def plot_function(func, a, b, c, d, e, f, figure_name="Graph", num_points=200):
    x_values = np.linspace(a, b, num_points)
    y_values = func(x_values)
    output_dir = './Homework_10/Screenshot'
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label="f(x)", color='blue')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.scatter(x_values[np.argmin(y_values)], min(y_values), color='red', label="Estimated Min")
    plt.scatter(x_values[np.argmax(y_values)], max(y_values), color='green', label="Estimated Max")
    print(c,d,e,f)
    plt.scatter(c,d,color='blue', label="Golden Section Min" )
    plt.scatter(e,f,color='orange', label="Golden Section Max" )
    plt.title("Plot of f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, figure_name))
    plt.show()
def main():
    try:
        user_function = input("Enter the function f(x) as a Python lambda (e.g., lambda x: x**2 - 4*x): ").strip()
        func = evaluate_function(user_function)
        a, b = map(float, input("Enter the interval [a, b] separated by space: ").split())
        if a >= b:
            raise ValueError("Interval must have a < b.")
        # Golden Section
        print("\nGolden Section Search:")
        x_min, f_min, iter_min = golden_section(func, a, b, minimize=True)
        print(f"Minimum at x = {x_min:.4f}, f(x) = {f_min:.4f}, iterations = {iter_min}")
        x_max, f_max, iter_max = golden_section(func, a, b, minimize=False)
        print(f"Maximum at x = {x_max:.4f}, f(x) = {f_max:.4f}, iterations = {iter_max}")

        # Newton's Method
        print("\nNewton's Method:")
        x0 = float(input("Enter the initial guess for Newton's method: "))
        x_newton, f_newton, iter_newton = newton_method(func, x0)
        print(f"Critical point at x = {x_newton:.4f}, f(x) = {f_newton:.4f} after {iter_newton} iterations.")
        plot_function(func, a, b, x_min, f_min, x_max, f_max)
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
main()



"""
x**3 - 4*x
"""