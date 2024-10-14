import numpy as np
import math
def fun_input(expression):
    return eval("lambda x: " + expression)
def secant_method(x0, x1, delta, f, flag, true_root):
    iteration = 0  
    approx_error = 1e12  
    prev_x2 = x1  
    f_x0 = f(x0)  
    f_x1 = f(x1)  
    if f_x0 * f_x1 > 0:
        print('No root in the given interval. Try again.')
        return None, iteration
    while True:
        iteration += 1  
        if f_x1 - f_x0 == 0:
            print("Division by zero in secant method.")
            return None, iteration
        x2 = x1 - f_x1 * ((x1 - x0) / (f_x1 - f_x0))
        f_x2 = f(x2)  
        if np.abs(f_x2) < 1e-12:
            return x2, iteration  
        approx_error = np.abs(x2 - prev_x2)
        if x2 != 0:
            rel_err = np.abs(approx_error / x2) * 100  
        else:
            float('inf')
        if true_root is not None:
            true_error = np.abs(x2 - true_root)  
        if flag == 'A' and approx_error < delta:
            print("Stopping due to Approximate Error")
            return x2, iteration
        elif flag == 'B' and rel_err < delta:
            print("Stopping due to Relative Error")
            return x2, iteration
        elif flag == 'C' and true_error is not None and true_error < delta:
            print("Stopping due to True Error")
            return x2, iteration
        elif flag == 'D' and approx_error < delta and true_error is not None and true_error < delta:
            print("Stopping due to Both Approximate and True Error")
            return x2, iteration
        prev_x2 = x2
        x0, x1 = x1, x2
        f_x0, f_x1 = f_x1, f_x2
def false_position_method(x0, x1, delta, f, flag, true_root):
    iteration = 0  
    f_x0 = f(x0)  
    f_x1 = f(x1)  
    if f_x0 * f_x1 > 0:
        raise ValueError("Function must have different signs at x0 and x1.")
    while True:
        x2 = x1 - f_x1 * (x0 - x1) / (f_x0 - f_x1)
        f_x2 = f(x2)
        if np.abs(f_x2) < 1e-12:
            return x2, iteration  
        approx_error = np.abs(x2 - x1)
        if x2 != 0:
            rel_err = np.abs(approx_error / x2) * 100 
        else:
            float('inf')
        if true_root is not None: 
            true_error = np.abs(x2 - true_root) 
        if flag == 'a' and approx_error < delta:
            print("Stopping due to Approximate Error")
            break
        elif flag == 'b' and rel_err < delta:
            print("Stopping due to Relative Error")
            break
        elif flag == 'c' and true_error is not None and true_error < delta:
            print("Stopping due to True Error")
            break
        elif flag == 'd' and approx_error < delta and true_error is not None and true_error < delta:
            print("Stopping due to Both Approximate and True Error")
            break
        if f(x0) * f_x2 < 0:
            x1 = x2  
            f_x1 = f_x2  
        else:
            x0 = x2  
            f_x0 = f_x2  
        iteration += 1  
    return x2, iteration
def main():
    function_input = input("Enter a function of x (e.g., 'math.sin(x)', 'math.cos(x)', '2 * math.sin(x) - (math.exp(x) / 4) - 1'): ")
    try:
        f = fun_input(function_input)
        x0 = float(input("Enter the first initial approximation (x0): "))
        x1 = float(input("Enter the second initial approximation (x1): "))
        delta = float(input("Enter the tolerance value (delta): "))
        flags = ['a', 'b', 'c', 'd']
        for item in flags:
            true_root_input = input('Optional true root (press Enter to skip): ')
            true_root = float(true_root_input) if true_root_input else None
            root_secant, iterations_secant = secant_method(x0, x1, delta, f, item, true_root)
            print("\nSecant Method Results")
            print("____________________________________\n")
            print(f"Function: {function_input}")
            print(f"Interval: {{{x0}, {x1}}}")
            print(f"Tolerance (delta): {delta}")
            print(f"Stopping Criterion (Flag): {item}")
            print(f"Root found: {root_secant}")
            if root_secant is not None:
                print(f"f(root): {f(root_secant)}")
            print(f"Number of iterations: {iterations_secant}")
            if true_root is not None and item in ['c', 'd']:
                true_error = abs(root_secant - true_root)
                print(f"True error: {true_error}")
            print(f"Closeness of f(root) to 0: {np.abs(f(root_secant)) if root_secant is not None else 'N/A'}\n")
        for item in flags:
            root_false_position, iterations_false_position = false_position_method(x0, x1, delta, f, item, true_root)
            print("\nFalse Position Method Results")
            print("____________________________________\n")
            print(f"Function: {function_input}")
            print(f"Interval: {{{x0}, {x1}}}")
            print(f"Tolerance (delta): {delta}")
            print(f"Stopping Criterion (Flag): {item}")
            print(f"Root found: {root_false_position}")
            if root_false_position is not None:
                print(f"f(root): {f(root_false_position)}")
            print(f"Number of iterations: {iterations_false_position}")
            if true_root is not None and item in ['c', 'd']:
                true_error = abs(root_false_position - true_root)
                print(f"True error: {true_error}")
            print(f"Closeness of f(root) to 0: {np.abs(f(root_false_position)) if root_false_position is not None else 'N/A'}\n")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
main()
