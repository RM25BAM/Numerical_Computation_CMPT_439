import numpy as np
import math
def fun_input(expression):
    return eval("lambda x: " + expression) # evaluates user input to comvert to mathematical calls like math.sin(x) or math.cos(x)
def secant_method(x0, x1, delta, fun_input, flag, true_root): #function for secant method
    iteration = 0  # Initialize iteration  = 0
    approx_error = 1e12  # Large initial value for approximate error (mimic + inf)
    prev_x2 = x1  # Start with the last x1 as the previous x2
    f_x0 = fun_input(x0)  # Function value x0
    f_x1 = fun_input(x1)  # Function value x1
    # Check if initial guesses bracket a root
    if f_x0 * f_x1 > 0: # if its true
        print('No root in the given interval. Try again.') # print statement 
        return None, iteration # return None for root and the iteration
    # Secant loop
    while True: # While loop as long as its true
        iteration += 1  # iteration count++
        if f_x1 - f_x0 == 0: # Check if division by zero
            print("Division by zero in secant method.") # print statment if division by zero true
            return None, iteration # return root -> none and the iteration
        x2 = x1 - f_x1 * ((x1 - x0) / (f_x1 - f_x0))    # Secant formula
        f_x2 = fun_input(x2)  # Evaluate function at x2
        if np.abs(f_x2) < 1e-12: # Check if the function value at x2 is near zero
            return x2, iteration  # Root found
        approx_error = np.abs(x2 - prev_x2) # calculate approx error
        rel_err = np.abs(approx_error / x2) * 100 if x2 != 0 else float('inf') # relative error
        if true_root is not None: # true error if true root is not None
            true_error = np.abs(x2 - true_root) #calcualte true error
        # Apply stopping criteria based on the flag
        if flag == 'A' and approx_error < delta: # if user A then stop + approx < delta
            print("Stopping due to Approximate Error") # print statment 
            break # break out of loop
        elif flag == 'B' and rel_err < delta: # if user B then stop + relative error < delta
            print("Stopping due to Relative Error")# print statment 
            break # break out of loop
        elif flag == 'C' and true_error is not None and true_error < delta: # if user C then stop + true error < delta
            print("Stopping due to True Error")# print statment 
            break # break out of loop
        elif flag == 'D' and approx_error < delta and true_error is not None and true_error < delta: # if user D then stop+ approx error < delta + true error < delta
            print("Stopping due to Both Approximate and True Error")# print statment 
            break # break out of loop
        prev_x2 = x2 # set x2 -> as prev_x2
        x0 = x1 # set x0 -> x1
        x1 = x2 # set x2 -> x1
        f_x0 = f_x1 # set f_0 -> f_x1
        f_x1 = f_x2 # set f_1 -> f_x2
    return x2, iteration # return root and iteration
def false_position_method(x0, x1, delta, f, flag, true_root):
    iteration = 0  # iteration set to 0
    f_x0 = f(x0)  # function value for x0
    f_x1 = f(x1)  # function value for x1
    if f_x0 * f_x1 > 0: # f_x0 and f_x1 greater than 0 
        raise ValueError("Function must have different signs at x0 and x1.") # print statement
    while True: # while loop true will iterate 
        x2 = x1 - f_x1 * (x0 - x1) / (f_x0 - f_x1) #false positiive formula
        f_x2 = f(x2) # function value at x2
        if np.abs(f_x2) < 1e-12: # 
            return x2, iteration  # return iteration and x2
        approx_error = np.abs(x2 - x1) # calcualte approx error
        if x2 != 0: # x2 not equal to 0 
            rel_err = np.abs(approx_error / x2) * 100 # calculate relative error
        else: # else statement
            rel_err =  float('inf') # set rel error as inf
        if true_root is not None: # if true root isn't 
            true_error = np.abs(x2 - true_root)  # calculate true error
        # Apply stopping criteria based on the flag
        if flag == 'a' and approx_error < delta: # if user A then stop + approx < delta
            print("Stopping due to Approximate Error") # print statement of stop
            break # break out of loop
        elif flag == 'b' and rel_err < delta: # if user B then stop + relative error < delta
            print("Stopping due to Relative Error") # print statement of stop
            break # break out of loop
        elif flag == 'c' and true_error is not None and true_error < delta: # if user C then stop + true error < delta
            print("Stopping due to True Error") # print statement of stop
            break # break out of loop
        elif flag == 'd' and approx_error < delta and true_error is not None and true_error < delta:# if user D then stop + approx < delta + true error < delta
            print("Stopping due to Both Approximate and True Error") # print statement of stop
            break # break out of loop
        if f(x0) * f_x2 < 0: # Update interval for the next iteration
            x1 = x2   # update x1 
            f_x1 = f_x2  #update function 1 value
        else: # else statement
            x0 = x2  # update x0
            f_x0 = f_x2  # Update function value
        iteration += 1  #  iteration ++1
    return x2, iteration # return root and iteration 
""" def false_position_method(x0, x1, delta, f, flag, true_root):
    iteration = 0  # Initialize iteration 0
    f_x0 = fun_input(x0)  # Function value at x0
    f_x1 = fun_input(x1)  # Function value at x1
    if f_x0 * f_x1 > 0: # Check if root is in the interval
        raise ValueError("Function must have different signs at x0 and x1.") # raise error
    # False position loop
    while True: # while loop if true
        x2 = x1 - f_x1 * (x0 - x1) / (f_x0 - f_x1) # false positive function
        # Check if the function value at x2 is near zero
        f_x2 = fun_input(x2) # set f(x2) -> f_x2
        if np.abs(f_x2) < 1e-12:
            return x2, iteration  # Root found
        approx_error = np.abs(x2 - x1) # Calculate approximate error
        if x2 != 0: # x2 not equal to 0
            rel_err = np.abs(approx_error / x2) * 100  # calculate relative error
        else: # else
            rel_err = float('inf') # set rel_error to infinity
        if true_root is not None: # true root not none
            true_error = np.abs(x2 - true_root) # calculate true error
        # Apply stopping criteria based on the flag
        if flag == 'a' and approx_error < delta: # if user A then stop + approx < delta
            print("Stopping due to Approximate Error") # print statement of stop
            break # break out of loop
        elif flag == 'b' and rel_err < delta: # if user B then stop + relative error < delta
            print("Stopping due to Relative Error") # print statement of stop
            break # break out of loop
        elif flag == 'c' and true_error is not None and true_error < delta: # if user C then stop + true error < delta
            print("Stopping due to True Error") # print statement of stop
            break # break out of loop
        elif flag == 'd' and approx_error < delta and true_error is not None and true_error < delta:# if user D then stop + approx < delta + true error < delta
            print("Stopping due to Both Approximate and True Error") # print statement of stop
            break # break out of loop
        if f(x0) * f_x2 < 0: # Update interval for the next iteration
            x1 = x2  # update x1 
            f_x1 = f_x2  # Update function value
        else:
            x0 = x2  # update x0
            f_x0 = f_x2  # Update function value
        iteration += 1  #  iteration ++1
    return x2, iteration # return root and iteration """
def main():
    function_input = input("Enter a function of x (e.g., 'math.sin(x)', 'math.cos(x)', 'x**2 - 2'): ")
    try:
        f = fun_input(function_input)
        x0 = float(input("Enter the first initial approximation (x0): "))
        x1 = float(input("Enter the second initial approximation (x1): "))
        delta = float(input("Enter the tolerance value (delta): "))
        flag = input("Choose stopping criterion (a: Absolute error, b: Relative error, c: True error, d: Combination): ")
        true_root_input = input('Optional true root (press Enter to skip): ')
        true_root = float(true_root_input) if true_root_input else None
        # Secant method
        root_secant, iterations_secant = secant_method(x0, x1, delta, f, flag, true_root)
        # Display Secant method
        print("\nSecant Method Results")
        print("____________________________________\n")
        print(f"Function: {function_input}")
        print(f"Interval: {{{x0}, {x1}}}")
        print(f"Tolerance (delta): {delta}")
        print(f"Stopping Criterion (Flag): {flag}")
        print(f"Root found: {root_secant}")
        if root_secant is not None:
            print(f"f(root): {f(root_secant)}")
        print(f"Number of iterations: {iterations_secant}")
        if true_root is not None and flag in ['c', 'd']:
            true_error = abs(root_secant - true_root)
            print(f"True error: {true_error}")
        print(f"Closeness of f(root) to 0: {np.abs(f(root_secant)) if root_secant is not None else 'N/A'}\n")
        # False Position method
        root_false_position, iterations_false_position = false_position_method(x0, x1, delta, f, flag, true_root)
        # Display False Position method
        # Secant method output section
        print("\nFalse Position Method Results")
        print("____________________________________\n")
        print(f"Function: {function_input}")
        print(f"Interval: {{{x0}, {x1}}}")
        print(f"Tolerance (delta): {delta}")
        print(f"Stopping Criterion (Flag): {flag}")
        print(f"Root found: {root_false_position}")
        if root_false_position is not None:
            print(f"f(root): {f(root_false_position)}")
        print(f"Number of iterations: {iterations_false_position}")
        if true_root is not None and flag in ['c', 'd']:
            true_error = abs(root_false_position - true_root)
            print(f"True error: {true_error}")
        print(f"Closeness of f(root) to 0: {np.abs(f(root_false_position)) if root_false_position is not None else 'N/A'}\n")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
main()
"""
Q1 
4 stopping criteria
"""