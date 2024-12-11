# Function for the multiple application trapezoidal rule
def compute_trapezoidal_integral(h, f):
    return h * (sum(f) - (f[0] + f[-1]) / 2)

# Function for the composite Simpson's 1/3 rule
def compute_simpsons_integral(h, f):
    return (h / 3) * (f[0] + f[-1] + 4 * sum(f[1:-1:2]) + 2 * sum(f[2:-2:2]))

# Lagrange interpolation for missing values
def lagrange_interpolation(x, y, x_target):
    return sum(y[i] * prod((x_target - x[j]) / (x[i] - x[j]) for j in range(len(x)) if i != j) for i in range(len(x)))

# Function to interpolate missing points
def interpolate_missing_points(f):
    f[2] = lagrange_interpolation([1.0, 1.3, 1.5], [1.543, 1.971, 2.352], 1.2)
    f[6] = lagrange_interpolation([1.5, 1.7, 1.8], [2.352, 2.828, 3.107], 1.6)

# Given data
h = 0.1
f = [1.543, 1.669, None, 1.971, 2.151, 2.352, None, 2.828, 3.107]

# Interpolate missing values
interpolate_missing_points(f)

# Compute integrals
trapezoidal_result = compute_trapezoidal_integral(h, f)
simpsons_result = compute_simpsons_integral(h, f)

# Output results
print(f"Trapezoidal Rule Result: {trapezoidal_result:.4f}")
print(f"Simpson's Rule Result: {simpsons_result:.4f}")
