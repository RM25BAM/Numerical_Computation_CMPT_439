import numpy as np

def trapezoidal_rule(h, x_values, f_values):
    """
    Implements the multiple application trapezoidal rule.
    Args:
        h (float): Step size.
        x_values (list): x values from the table.
        f_values (list): Corresponding f(x) values from the table.
    Returns:
        float: Approximation of the integral using the trapezoidal rule.
    """
    n = len(x_values) - 1
    integral = 0.5 * (f_values[0] + f_values[-1])
    for i in range(1, n):
        integral += f_values[i]
    return h * integral

def simpsons_rule(h, x_values, f_values):
    """
    Implements the composite Simpson's 1/3 rule.
    Args:
        h (float): Step size.
        x_values (list): x values from the table.
        f_values (list): Corresponding f(x) values from the table.
    Returns:
        float: Approximation of the integral using Simpson's rule.
    """
    n = len(x_values) - 1
    if n % 2 != 0:
        raise ValueError("Number of intervals (n) must be even for Simpson's rule.")

    integral = f_values[0] + f_values[-1]
    for i in range(1, n, 2):
        integral += 4 * f_values[i]
    for i in range(2, n - 1, 2):
        integral += 2 * f_values[i]
    return (h / 3) * integral

if __name__ == "__main__":
    # User input for x and f(x) values
    x_values = list(map(float, input("Enter x values separated by spaces: ").split()))
    f_values = list(map(float, input("Enter corresponding f(x) values separated by spaces: ").split()))

    if len(x_values) != len(f_values):
        raise ValueError("The number of x values must match the number of f(x) values.")

    # User input for step size
    h = float(input("Enter the step size (h): "))

    # Trapezoidal Rule Application
    trapezoidal_result = trapezoidal_rule(h, x_values, f_values)
    print(f"Trapezoidal Rule Result: {trapezoidal_result:.4f}")

    # Simpson's Rule Application
    try:
        simpsons_result = simpsons_rule(h, x_values, f_values)
        print(f"Simpson's Rule Result: {simpsons_result:.4f}")
    except ValueError as e:
        print(e)
