def simpsons_rule(h, x_values, f_values):
    n = len(x_values) - 1
    if n % 2 != 0:
        raise ValueError("Number of intervals (n) must be even for Simpson's rule.")

    integral = f_values[0] + f_values[-1]
    for i in range(1, n, 2):
        integral += 4 * f_values[i]
    for i in range(2, n - 1, 2):
        integral += 2 * f_values[i]
    return (h / 3) * integral