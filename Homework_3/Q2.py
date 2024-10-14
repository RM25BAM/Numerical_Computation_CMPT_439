import numpy as np

def func(x):
    """Example function: f(x) = sin(x)"""
    return np.cos(x)  # Change this to your desired function

def d_func(x):
    """Example derivative: f'(x) = cos(x)"""
    return np.cos(x)  # Change this to the derivative of your function

def newtons_method(initial_guess, tolerance, stop_criteria, true_root=None):
    """Find a root using Newton's method."""
    estimate = initial_guess
    iterations = 0
    
    while True:
        iterations += 1
        f_value = func(estimate)
        d_value = d_func(estimate)

        if d_value == 0:
            return None, iterations  # Derivative zero error

        estimate -= f_value / d_value  # Update step

        abs_error = abs(f_value)
        rel_error = abs_error / abs(estimate) * 100 if estimate != 0 else float('inf')
        true_error = abs(estimate - true_root) if true_root else None

        # Stopping conditions
        if stop_criteria == 'A' and abs_error < tolerance:
            break
        elif stop_criteria == 'B' and rel_error < tolerance:
            break
        elif stop_criteria == 'C' and true_error and true_error < tolerance:
            break
        elif stop_criteria == 'D' and abs_error < tolerance and true_error and true_error < tolerance:
            break

    return estimate, iterations

def main():
    tolerance = float(input("Enter tolerance: "))
    initial_guess = float(input("Initial guess: "))
    stop_criteria = input("Stopping criterion (A, B, C, D): ")
    true_root_input = input("Optional true root (leave blank if unknown): ")
    true_root = float(true_root_input) if true_root_input else None

    root, iter_count = newtons_method(initial_guess, tolerance, stop_criteria, true_root)

    # Different output format
    result_message = f"Estimated Root: {root}, Total Iterations: {iter_count}"
    if true_root:
        result_message += f", True Error: {abs(root - true_root)}"
    
    print(result_message)

if __name__ == "__main__":
    main()
