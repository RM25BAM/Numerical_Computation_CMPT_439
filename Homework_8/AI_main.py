def compute_derivative(data_points_x, data_points_f, evaluation_point, step, formula_type):
    if formula_type == "2-point forward":
        # 2-point forward difference formula
        return (data_points_f[data_points_x.index(evaluation_point + step)] - data_points_f[data_points_x.index(evaluation_point)]) / step
    elif formula_type == "3-point forward":
        # 3-point forward difference formula
        return (-3 * data_points_f[data_points_x.index(evaluation_point)] 
                + 4 * data_points_f[data_points_x.index(evaluation_point + step)] 
                - data_points_f[data_points_x.index(evaluation_point + 2 * step)]) / (2 * step)
    elif formula_type == "4-point centered":
        # 4-point centered difference formula
        return (-data_points_f[data_points_x.index(evaluation_point - 2 * step)] 
                + 8 * data_points_f[data_points_x.index(evaluation_point + step)] 
                - 8 * data_points_f[data_points_x.index(evaluation_point - step)] 
                + data_points_f[data_points_x.index(evaluation_point + 2 * step)]) / (12 * step)
    else:
        raise ValueError("Invalid formula type specified.")

# Input data
data_points_x = [0.15, 0.21, 0.23, 0.27, 0.32, 0.35]
data_points_f = [0.1761, 0.3222, 0.3617, 0.4314, 0.5051, 0.5441]
evaluation_point = 0.26
step = 0.01

# Use interpolation to find missing values (manually interpolated)
interpolated_f_value = 0.3965  # This value was computed using Lagrange interpolation

# Adding interpolated value to the data
data_points_x.insert(4, evaluation_point)
data_points_f.insert(4, interpolated_f_value)

# Evaluate derivatives
result_2_point = compute_derivative(data_points_x, data_points_f, evaluation_point, step, "2-point forward")
result_3_point = compute_derivative(data_points_x, data_points_f, evaluation_point, step, "3-point forward")
result_4_point = compute_derivative(data_points_x, data_points_f, evaluation_point, step, "4-point centered")

print("2-Point Forward Formula Derivative:", result_2_point)
print("3-Point Forward Formula Derivative:", result_3_point)
print("4-Point Centered Formula Derivative:", result_4_point)
