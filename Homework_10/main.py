import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def evaluate_function(expr, x_value):
    """
    Evaluates the user-defined function at a specific point.
    """
    x = sp.symbols('x')
    function = sp.lambdify(x, expr, 'numpy')
    return function(x_value)

def derivative_function(expr, order=1):
    """
    Returns the derivative of the user-defined function.
    """
    x = sp.symbols('x')
    derivative_expr = sp.diff(expr, x, order)
    return sp.lambdify(x, derivative_expr, 'numpy')

def newton_method(f_expr, x0, tol=1e-5, max_iter=100):
    """
    Newton's method to find critical points (extrema) of the function.
    """
    f_prime = derivative_function(f_expr, order=1)
    f_double_prime = derivative_function(f_expr, order=2)

    x = x0
    for i in range(max_iter):
        f_prime_val = f_prime(x)
        f_double_prime_val = f_double_prime(x)

        if f_double_prime_val == 0:
            raise ValueError("Zero second derivative encountered, cannot proceed.")

        x_new = x - f_prime_val / f_double_prime_val

        if abs(x_new - x) < tol:
            return x_new, evaluate_function(f_expr, x_new), i + 1

        x = x_new

    raise ValueError("Newton's method did not converge within the maximum number of iterations.")

def golden_section_search(f_expr, a, b, tol=1e-5, minimize=True):
    """
    Golden Section Search for minimizing or maximizing a unimodal function.
    """
    phi = (1 + np.sqrt(5)) / 2
    inv_phi = 1 / phi

    x1 = b - (b - a) * inv_phi
    x2 = a + (b - a) * inv_phi

    f = sp.lambdify(sp.symbols('x'), f_expr, 'numpy')
    f1 = f(x1)
    f2 = f(x2)

    iter_count = 0
    while abs(b - a) > tol:
        iter_count += 1
        if (f1 < f2 if minimize else f1 > f2):
            b, x2, f2 = x2, x1, f1
            x1 = b - (b - a) * inv_phi
            f1 = f(x1)
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + (b - a) * inv_phi
            f2 = f(x2)

    x_opt = (a + b) / 2
    return x_opt, f(x_opt), iter_count

def plot_function(expr, a, b, num_points=100):
    """
    Plots the function over the given interval [a, b] and estimates extrema visually.
    """
    x = sp.symbols('x')
    f = sp.lambdify(x, expr, 'numpy')

    # Generate x and y values for the plot
    x_values = np.linspace(a, b, num_points)
    y_values = f(x_values)

    # Plot the function
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f"f(x) = {expr}", color='blue')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

    # Highlight minimum and maximum visually (optional)
    plt.scatter(x_values[np.argmin(y_values)], min(y_values), color='red', label="Estimated Min")
    plt.scatter(x_values[np.argmax(y_values)], max(y_values), color='green', label="Estimated Max")

    # Add labels and grid
    plt.title("Plot of f(x) with Estimated Extrema")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    try:
        # User input for the function
        user_function = input("Enter the function f(x): ")
        expr = sp.sympify(user_function)

        # Plot the function
        a, b = map(float, input("Enter the interval [a, b] separated by space: ").split())
        plot_function(expr, a, b)

        # Golden Section Search
        print("Golden Section Search:")
        x_min, f_min, iter_min = golden_section_search(expr, a, b, minimize=True)
        print(f"Minimum at x = {x_min:.4f}, f(x) = {f_min:.4f}, iterations = {iter_min}")

        x_max, f_max, iter_max = golden_section_search(expr, a, b, minimize=False)
        print(f"Maximum at x = {x_max:.4f}, f(x) = {f_max:.4f}, iterations = {iter_max}")

        # Newton's Method
        print("\nNewton's Method:")
        x0 = float(input("Enter the initial guess for Newton's method: "))
        x_newton, f_newton, iter_newton = newton_method(expr, x0)
        print(f"Critical point at x = {x_newton:.4f}, f(x) = {f_newton:.4f} after {iter_newton} iterations.")

    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


"""
x**3 - 4*x



"""