import numpy as np
#langrange from the hw7
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    interpolated_value = 0.0
    for i in range(n):
        L_i = 1.0
        for j in range(n):
            if j != i:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        interpolated_value += y_points[i] * L_i
    return interpolated_value
# Numerical differentiation function
def numerical_differentiation(x, y, h, method, x_value, interpolation=True):
    if interpolation and x_value not in x: # Interpolate missing f(x) if not in the x coor point
        interpolated_func = lagrange_interpolation(x_value, x, y)
        x.append(x_value)
        y.append(interpolated_func)
    required_points = [x_value]
    if method == "a":  # 2-point forward difference
        required_points.append(x_value + h)
    elif method == "b":  # 3-point forward difference
        required_points.extend([x_value + h, x_value + 2 * h])
    elif method == "c":  # 3-point centered difference
        required_points.extend([x_value - h, x_value + h])
    for point in required_points:
        if point not in x:
            interpolated_func = lagrange_interpolation(point, x, y)
            x.append(point)
            y.append(interpolated_func)
    x, y = (list(t) for t in zip(*sorted(zip(x, fx))))
    mx = x.index(x_value)
    jh = x.index(x_value + h) if (x_value + h) in x else None
    dh = x.index(x_value + 2 * h) if method == "b" and (x_value + 2 * h) in x else None
    mh = x.index(x_value - h) if method == "c" and (x_value - h) in x else None
    if method == "a":  # 2-point forward difference
        if jh is None:
            raise ValueError("Required point for method 'a' is missing.")
        return (fx[jh] - fx[mx]) / h
    elif method == "b":  # 3-point forward difference
        if dh is None or jh is None:
            raise ValueError("Required points for method 'b' are missing.")
        return (-fx[dh] + 4 * fx[jh] - 3 * fx[mx]) / (2 * h)
    elif method == "c":  # 3-point centered difference
        if mh is None or jh is None:
            raise ValueError("Required points for method 'c' are missing.")
        return (fx[jh] - fx[mh]) / (2 * h)
    else:
        raise ValueError("Invalid method, only (a,b,c)")
def main():
    print("\n{:-^50}".format(""))
    x = list(map(float, input("Enter the x values: ").split()))
    y = list(map(float, input("Enter the corresponding f(x) values: ").split()))
    h = float(input("Enter the step size (h): "))
    x_target = float(input("Enter the point at which to evaluate the derivative: "))
    print("\nInterpolating missing points...\n")
    for method in ['a', 'b', 'c']:
        required_points = [x_target]
        if method == "a":  # 2-point forward dif
            required_points.append(x_target + h)
        elif method == "b":  # 3-point forward dif
            required_points.extend([x_target + h, x_target + 2 * h])
        elif method == "c":  # 3-point centered dif
            required_points.extend([x_target - h, x_target + h])
        for point in required_points:
            if point not in x:
                interpolated_value = lagrange_interpolation(point, x, y)
                x.append(point)
                fx.append(interpolated_value) # append to fx list
                print(f"Interpolated value at x = {point}: f({point}) = {interpolated_value:.4f}")

    x, y = (list(t) for t in zip(*sorted(zip(x, y))))
    print("\n{:-^20}".format(""))
    print("\nNumerical differentiation Values:")
    for method in ['a', 'b', 'c']:
        derivative = numerical_differentiation(x, y, h, method, x_target)
        method_name = {
                'a': "2-point forward difference",
                'b': "3-point forward difference",
                'c': "3-point centered difference",
        }
        print(f"{method_name[method]}: f'({x_target}) = {derivative:.4f}")
    print("\n{:-^50}".format(""))
main()

