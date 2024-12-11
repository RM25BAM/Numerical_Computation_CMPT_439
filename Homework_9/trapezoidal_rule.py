def trapezoidal_rule(h, x_values, f_values):
    n = len(x_values) - 1
    integral = 0.5 * (f_values[0] + f_values[-1])
    for i in range(1, n):
        integral += f_values[i]
    return h * integral