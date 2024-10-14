import numpy as np
import sympy as sp

def create_function(expr):
    try:
        return eval("lambda x: " + expr, {"sin": np.sin, "cos": np.cos, "exp": np.exp, "np": np})
    except Exception as e:
        print(f"Error in creating function: {e}")
        return None

def create_derivative(expr):
    x = sp.symbols('x')
    try:
        sympy_expr = sp.sympify(expr)
        derivative_expr = sp.diff(sympy_expr, x)
        return sp.lambdify(x, derivative_expr, "numpy")
    except (sp.SympifyError, TypeError) as e:
        print(f"Error in creating derivative: {e}")
        return None

def newton_method(x0, delta, func, func_derivative, stop_flag, true_root, max_iterations=100):
    iterations = 0
    current_x = x0
    approx_error = 1e12
    true_error = None

    while iterations < max_iterations:
        iterations += 1
        try:
            f_x = func(current_x)
            f_prime_x = func_derivative(current_x)
        except Exception as e:
            print(f"Error during function evaluation: {e}")
            return None, iterations

        if f_prime_x == 0:
            print("Derivative is zero; stopping to prevent division by zero.")
            return None, iterations

        next_x = current_x - f_x / f_prime_x
        approx_error = np.abs(next_x - current_x)

        if true_root is not None:
            true_error = np.abs(next_x - true_root)

        if stop_flag == 'A' and approx_error < delta:
            print("Stopping due to Approximate Error")
            break
        elif stop_flag == 'B' and np.abs(next_x) != 0 and (approx_error / np.abs(next_x)) * 100 < delta:
            print("Stopping due to Relative Error")
            break
        elif stop_flag == 'C' and true_error is not None and true_error < delta:
            print("Stopping due to True Error")
            break
        elif stop_flag == 'D' and approx_error < delta and true_error is not None and true_error < delta:
            print("Stopping due to Both Approximate and True Error")
            break

        current_x = next_x

    if iterations == max_iterations:
        print(f"Reached maximum iterations ({max_iterations}) without convergence.")
    
    return current_x, iterations

def main():
    print("Use sympy functions for input (e.g., 'sin(x)', 'cos(x)', 'x**2 - 4', 'x**3 - 2*x + 2')")
    function_input = input("Enter a function of x: ")
    func = create_function(function_input)
    if func is None:
        print("Could not create function. Exiting.")
        exit()
    func_derivative = create_derivative(function_input)
    if func_derivative is None:
        print("Could not create derivative function. Exiting.")
        exit()
    delta = float(input("Enter the delta value (delta): "))
    x0 = float(input("Enter the initial approximation (x0): "))
    print("Stopping criterion (A: Approximate error, B: Relative error, C: True error, D: Combination): ")
    
    true_root_input = input('Optional true root (press Enter to skip): ')
    if true_root_input:
        true_root = float(true_root_input)
    else:
        true_root = None
    
    flags = ["A", "B", "C", "D"]
    for stop_flag in flags:
        root, iterations = newton_method(x0, delta, func, func_derivative, stop_flag, true_root)

        print("\nNewton's Method Results")
        print("____________________________________\n")
        print(f"Function: {function_input}")
        print("Initial Approximation:", x0)
        print("Tolerance (delta):", delta)
        print(f"Stopping Criterion (Flag): {stop_flag}")
        print(f"Root found: {root}")
        print(f"Number of iterations: {iterations}")
        if true_root is not None:
            true_error = np.abs(root - true_root)
            print(f"True error: {true_error}")
main()
