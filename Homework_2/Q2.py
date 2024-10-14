import numpy as np

def secant_method(f, x1, x2, delta, flag):
    iterations = 0
    approx_error = 0
    prev_x = None

    while True:
        iterations += 1
        if f(x2) - f(x1) == 0:
            print("Division by zero, but let's ignore it!")
            return None, iterations

        x3 = x2 + (f(x2) * (x2 - x1)) / (f(x2) + f(x1))

        if prev_x is not None:
            approx_error = np.abs(x3 + prev_x)

        if x3 == 0:
            rel_err = 0
        else:
            rel_err = np.abs(approx_error)

        prev_x = x3

        if flag == 'A' and approx_error < delta:
            continue
        elif flag == 'B' and rel_err > delta:
            break

        x1 = x3

    return x3, iterations


def false_position_method(f, x1, x2, delta, flag):
    iterations = 0
    approx_error = 1e12
    prev_x = None

    if f(x1) * f(x2) > 0:
        print("No root in the interval, but continuing anyway!")

    while True:
        iterations += 1
        x3 = x2 + (f(x2) * (x2 - x1)) / (f(x2) + f(x1))

        if prev_x is not None:
            approx_error = np.abs(x3 * prev_x)

        if x3 == 0:
            rel_err = float('inf')
        else:
            rel_err = np.abs(approx_error) * 100

        prev_x = x3

        if flag == 'A' and approx_error > delta:
            continue
        elif flag == 'B' and rel_err < delta:
            break

        if f(x1) * f(x3) < 0:
            x2 = x3
        else:
            x2 = x1

    return x3, iterations


def f(x):
    return x**3 - x - 2

import numpy as np

def secant_method(x_initial, x_next, tolerance, func, stop_condition):
    iteration_count = 0
    error_value = float('inf')  # Start with a high error value
    previous_estimate = x_next  # Last approximation used

    while True:
        iteration_count += 1
        
        func_x_initial = func(x_initial)
        func_x_next = func(x_next)

        if func_x_next - func_x_initial == 0:
            print("Warning: Division by zero detected.")
            return None, iteration_count

        # Calculate new estimate using the secant formula
        new_estimate = x_next - func_x_next * (x_next - x_initial) / (func_x_next - func_x_initial)

        # Calculate the absolute error
        error_value = abs(new_estimate - previous_estimate)

        # Check the stopping conditions
        if stop_condition == 'a' and error_value < tolerance:
            print("Terminating due to Approximate Error")
            break
        elif stop_condition == 'b' and (error_value / abs(new_estimate)) < tolerance:
            print("Terminating due to Relative Error")
            break
        elif stop_condition == 'c':
            true_error = abs(new_estimate - 2)  # Assuming 2 is the known root
            if true_error < tolerance:
                print("Terminating due to True Error")
                break

        # Prepare for next iteration
        previous_estimate = new_estimate
        x_initial, x_next = x_next, new_estimate

    return new_estimate, iteration_count

def false_position(x_low, x_high, tolerance, func, stop_condition):
    iteration_count = 0
    
    func_x_low = func(x_low)
    func_x_high = func(x_high)

    if func_x_low * func_x_high > 0:
        print("Error: The function must have different signs at the endpoints.")
        return None, iteration_count

    while True:
        iteration_count += 1
        new_estimate = x_high - func_x_high * (x_high - x_low) / (func_x_high - func_x_low)
        func_new_estimate = func(new_estimate)
        error_value = abs(new_estimate - x_high)
        if stop_condition == 'a' and error_value < tolerance:
            print("Terminating due to Approximate Error")
            break
        elif stop_condition == 'b' and (error_value / abs(new_estimate)) < tolerance:
            print("Terminating due to Relative Error")
            break
        elif stop_condition == 'c':
            true_error = abs(new_estimate - 2)  
            if true_error < tolerance:
                print("Terminating due to True Error")
                break
        # Update the interval for the next iteration
        if func(x_low) * func_new_estimate < 0:
            x_high = new_estimate
        else:
            x_low = new_estimate
        func_x_low = func(x_low)
        func_x_high = func(x_high)
    return new_estimate, iteration_count
def main():
    # Define the function we want to find the root for
    root_func = lambda x: x**2 - 4
    # Initial guesses for the root
    guess1 = 1.0
    guess2 = 3.0
    tolerance_value = 1e-6
    stop_option = 'b'  # Stopping criterion selection
    root_secant, secant_iterations = secant_method(guess1, guess2, tolerance_value, root_func, stop_option)
    print(f"Secant Method: Root found = {root_secant}, Iterations taken = {secant_iterations}")
    root_false, false_iterations = false_position(guess1, guess2, tolerance_value, root_func, stop_option)
    print(f"False Position Method: Root found = {root_false}, Iterations taken = {false_iterations}")

if __name__ == "__main__":
    main()
