import numpy as np
import matplotlib.pyplot as plt

def optimization_and_plot(func, dfunc, d2func, a, b, x0_min, x0_max, num_points=200):
    def golden_section(func, a, b, is_min=True, tol=1e-5):
        gr = (np.sqrt(5) - 1) / 2  # Golden ratio
        x1, x2 = b - gr * (b - a), a + gr * (b - a)
        f1, f2 = func(x1), func(x2)
        iterations = 0

        while abs(b - a) > tol:
            iterations += 1
            if is_min:
                if f1 < f2:
                    b, x2, f2 = x2, x1, f1
                    x1 = b - gr * (b - a)
                    f1 = func(x1)
                else:
                    a, x1, f1 = x1, x2, f2
                    x2 = a + gr * (b - a)
                    f2 = func(x2)
            else:
                if f1 > f2:
                    b, x2, f2 = x2, x1, f1
                    x1 = b - gr * (b - a)
                    f1 = func(x1)
                else:
                    a, x1, f1 = x1, x2, f2
                    x2 = a + gr * (b - a)
                    f2 = func(x2)

        return (a + b) / 2, func((a + b) / 2), iterations

    def newton_method(func, dfunc, d2func, x0, tol=1e-5, max_iter=100):
        x = x0
        iterations = 0

        while abs(dfunc(x)) > tol and iterations < max_iter:
            iterations += 1
            if d2func(x) == 0:  # Prevent division by zero
                print("Warning: Division by zero in Newton's Method")
                break
            x -= dfunc(x) / d2func(x)
        return x, func(x), iterations

    # Plot the function
    x_values = np.linspace(a, b, num_points)
    y_values = func(x_values)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label="f(x)", color="blue")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
    plt.title("Function Plot")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)

    # Golden Section Method
    x_min_golden, f_min_golden, iter_min_golden = golden_section(func, a, b, is_min=True)
    x_max_golden, f_max_golden, iter_max_golden = golden_section(func, a, b, is_min=False)

    # Newton's Method
    x_min_newton, f_min_newton, iter_min_newton = newton_method(func, dfunc, d2func, x0_min)
    x_max_newton, f_max_newton, iter_max_newton = newton_method(func, dfunc, d2func, x0_max)

    # Annotate the plot
    plt.scatter([x_min_golden, x_max_golden], [f_min_golden, f_max_golden], color="red", label="Golden Section Extrema")
    plt.scatter([x_min_newton, x_max_newton], [f_min_newton, f_max_newton], color="green", label="Newton Extrema")
    plt.legend()
    plt.show()

    # Print results
    print("Results:")
    print(f"Golden Section Method (Min): x = {x_min_golden}, f(x) = {f_min_golden}, Iterations = {iter_min_golden}")
    print(f"Golden Section Method (Max): x = {x_max_golden}, f(x) = {f_max_golden}, Iterations = {iter_max_golden}")
    print(f"Newton's Method (Min): x = {x_min_newton}, f(x) = {f_min_newton}, Iterations = {iter_min_newton}")
    print(f"Newton's Method (Max): x = {x_max_newton}, f(x) = {f_max_newton}, Iterations = {iter_max_newton}")

# Define the function and its derivatives
func = lambda x: x**3 - 4 * x
dfunc = lambda x: 3 * x**2 - 4
d2func = lambda x: 6 * x

# Call the function with given inputs
optimization_and_plot(func, dfunc, d2func, a=-3, b=3, x0_min=-2, x0_max=2)
