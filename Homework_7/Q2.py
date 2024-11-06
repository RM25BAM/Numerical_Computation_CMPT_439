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
x_points = [1, 2, 3]
y_points = [2, 3, 5]
x = 2.5
result = lagrange_interpolation(x, x_points, y_points)
print("Interpolated value at x =", x, "is", result)
