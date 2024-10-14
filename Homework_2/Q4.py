import numpy as np
import sympy as sp

# Define the equation to be solved: 2*sin(x) - x/4 - exp(-x) = 0
def equation(x):
    return 2 * np.sin(x) - (x / 4) - np.exp(-x)

# False Position Method with flexible stopping criteria
def false_position_method(func, x1, x2, delta, flag, true_root=None):
    iteration = 0  # Initialize iteration count
    approx_error = 1e12  # Initial approximate error
    prev_x = None  # Previous x3 value
    
    # Check if there's a root in the interval
    if func(x1) * func(x2) > 0:
        print("No root in the given interval.")
        return None, iteration
    
    while True:
        iteration += 1
        x3 = x2 - (func(x2) * (x2 - x1)) / (func(x2) - func(x1))  # False Position formula
        
        if prev_x is not None:
            approx_error = np.abs(x3 - prev_x)  # Calculate approximate error
        
        rel_err = np.abs(approx_error / x3) * 100 if x3 != 0 else float('inf')  # Relative error
        
        true_error = np.abs(x3 - true_root) if true_root is not None else None  # True error if true root is provided
        
        # Update x1 and x2 based on function values
        if func(x1) * func(x3) < 0:
            x2 = x3
        else:
            x1 = x3

        prev_x = x3  # Update previous estimate
        
        # Stopping Criteria
        if flag == 'A' and approx_error < delta:
            break  # Stop based on absolute approximate error
        elif flag == 'B' and rel_err < delta:
            break  # Stop based on relative approximate error
        elif flag == 'C' and true_error is not None and true_error < delta:
            break  # Stop based on true absolute error
        elif flag == 'D' and approx_error < delta and true_error is not None and true_error < delta:
            break  # Stop based on both errors
    
    return x3, iteration  # Return the root and iteration count

# Main function to test the method for all stopping criteria
def solve_equation():
    # Define the equation symbolically
    x = sp.symbols('x')
    func = 2 * sp.sin(x) - x / 4 - sp.exp(-x)
    
    # Interval for root finding
    x1, x2 = 0, 2
    
    # Tolerance
    delta = 1e-6
    
    # Solve using all four stopping criteria
    root_a, iters_a = false_position_method(equation, x1, x2, delta, 'A')
    print(f"Root (Absolute Approx. Error): {root_a}, Iterations: {iters_a}, f(root): {equation(root_a)}")
    
    root_b, iters_b = false_position_method(equation, x1, x2, delta, 'B')
    print(f"Root (Relative Approx. Error): {root_b}, Iterations: {iters_b}, f(root): {equation(root_b)}")
    
    true_root = 1.5  # Assume an approximate true root
    root_c, iters_c = false_position_method(equation, x1, x2, delta, 'C', true_root)
    print(f"Root (True Absolute Error): {root_c}, Iterations: {iters_c}, f(root): {equation(root_c)}")
    
    root_d, iters_d = false_position_method(equation, x1, x2, delta, 'D', true_root)
    print(f"Root (Both Errors): {root_d}, Iterations: {iters_d}, f(root): {equation(root_d)}")

# Call the function to solve the equation
solve_equation()
