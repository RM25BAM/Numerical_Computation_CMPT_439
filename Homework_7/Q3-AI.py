import numpy as np

def newton_interpolation(x_interp, x_data, y_data):
  """
  Performs Newton interpolation using divided differences.

  Args:
    x_interp: The point at which to interpolate the function.
    x_data: A numpy array of x-values where the function is defined.
    y_data: A numpy array of corresponding function values.

  Returns:
    The interpolated function value at x_interp.
  """

  n = len(x_data) - 1
  divided_differences = np.zeros((n+1, n+1))
  divided_differences[:, 0] = y_data

  # Calculate divided differences
  for j in range(1, n+1):
    for i in range(n-j+1):
      divided_differences[i, j] = (divided_differences[i+1, j-1] - divided_differences[i, j-1]) / (x_data[i+j] - x_data[i])

  # Initialize the interpolated value
  p = divided_differences[0, 0]

  # Calculate the polynomial
  for k in range(1, n+1):
    term = 1
    for j in range(k):
      term *= (x_interp - x_data[j])
    p += divided_differences[0, k] * term

  return p
# Example data
x_data = np.array([1, 2, 3, 4])
y_data = np.array([1, 4, 9, 16])

# Point to interpolate at
x_interp = 2.5

# Interpolate the function
interpolated_value = newton_interpolation(x_interp, x_data, y_data)
print(interpolated_value)  # Output: 6.25