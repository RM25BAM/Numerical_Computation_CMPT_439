# Define the Lagrange interpolation function
def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    interpolated_value = 0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        interpolated_value += term
    return interpolated_value

# Data points provided
x_values_all = [0.3, 0.5, 0.7, 0.9, 1.1]
y_values_all = [0.404958, 0.824361, 1.40963, 2.21364, 3.30458]

# Point to interpolate
x_to_interpolate = 0.6

# Calculate interpolations for each specified subset of points
# (1) Using only the first 3 data points
interp_first_3 = lagrange_interpolation(x_values_all[:3], y_values_all[:3], x_to_interpolate)

# (2) Using only the first 4 data points
interp_first_4 = lagrange_interpolation(x_values_all[:4], y_values_all[:4], x_to_interpolate)

# (3) Using only the last 4 data points
interp_last_4 = lagrange_interpolation(x_values_all[1:], y_values_all[1:], x_to_interpolate)

# (4) Using all the given data points
interp_all_points = lagrange_interpolation(x_values_all, y_values_all, x_to_interpolate)

# Display the results
print("Interpolated value at x=0.6 using different subsets of points:")
print(f"(1) Using first 3 points: {interp_first_3}")
print(f"(2) Using first 4 points: {interp_first_4}")
print(f"(3) Using last 4 points: {interp_last_4}")
print(f"(4) Using all points: {interp_all_points}")
