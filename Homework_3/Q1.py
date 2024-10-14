import numpy as np
import sympy as sp

def create_function(expr): # function to evaluate user input for function
    try: # exception handling for the user input
        return eval("lambda x: " + expr) # return as eval()
    except Exception as e: # throw error
        print(f"Error in creating function: {e}") # print statement
        return None # return None
def create_derivative(expr): # function to evaluate the derivative od userinput
    x = sp.symbols('x') # x-> sympy to x 
    try:
        sympy_expr = sp.sympify(expr)  # converts to a sympy expression
        derivative_expr = sp.diff(sympy_expr, x)  #converts the sympy express to derivative (user input to derivative)
        return sp.lambdify(x, derivative_expr, "numpy") # returns the derviative value
    except (sp.SympifyError, TypeError) as e: # exception handling 
        print(f"Error in creating derivative: {e}") # if error print statement
        return None # return none
def newton_method(x0, delta, func, func_derivative, stop_flag, true_root): # newton method with paramters
    iterations = 0  # set iteration to 0
    current_x = x0  # current x = x0
    approx_error = 1e12 # aprrox error in large num to mimic + inf
    while True: # while loop is true
        iterations += 1  # add iteration 
        try: #try block
            f_x = func(current_x)  # set value of function for current_x
            f_prime_x = func_derivative(current_x) # derivative valye of current_x
        except Exception as e: # exception handling
            print(f"Error during function evaluation: {e}") # print statement
            return None, iterations # return None if exception raises
        if f_prime_x == 0: # if derivative value current_x equals 0
            print("Derivative is zero; stopping to prevent division by zero.") # print statement
            return None, iterations # return None for root and iterations
        next_x = current_x - f_x / f_prime_x # calculate next_x netwon formula
        approx_error = np.abs(next_x - current_x)  # calculate approx error
        if true_root is not None: # if true_root is not None
            true_error = np.abs(next_x - true_root) # calculate true error
        if stop_flag == 'A' and approx_error < delta: # if user A then stop + approx < delta
            print("Stopping due to Approximate Error") # print statement
            break # break out of loop
        elif stop_flag == 'B' and (approx_error / np.abs(next_x)) * 100 < delta:  # if user B then stop + relative error < delta
            print("Stopping due to Relative Error") # print statement
            break # break out of loop
        elif stop_flag == 'C' and true_error is not None and true_error < delta:  # if user C then stop + true error < delta
            print("Stopping due to True Error") # print statement
            break # break out of loop
        elif stop_flag == 'D' and approx_error < delta and true_error is not None and true_error < delta: # if user D then stop + approx < delta + true error < delta
            print("Stopping due to Both Approximate and True Error") # print statement
            break # break out of loop
        current_x = next_x # set current_x = next_x to prepare for next increment
    return next_x, iterations # return next_x and iteration
def main(): # main function
    print("Use sympy functions for input (e.g., 'sin(x)', 'cos(x)', 'x**2 - 4', 'x**3 - 2*x + 2')") # print statment 
    function_input = input("Enter a function of x: ") # user input
    func = create_function(function_input)  # function to evaluate user input convert string to working function for newton method
    if func is None: # if None
        print("Could not create function. Exiting.") # print statement
        exit() # exit program
    func_derivative = create_derivative(function_input)  # set function derivative
    if func_derivative is None: # if cant compute derivative
        print("Could not create derivative function. Exiting.")# print statement
        exit() # exit program
    delta = float(input("Enter the delta value (delta): "))  # user input delta
    x0 = float(input("Enter the initial approximation (x0): "))  # user input initial approx
    stop_flag = input("Choose stopping criterion (A: Approximate error, B: Relative error, C: True error, D: Combination): ")  # Stopping criterion
    stop_flag = stop_flag.upper() # set flag to upper
    true_root_input = input('Optional true root (press Enter to skip): ') # user input true root 
    if true_root_input: # if user input
        true_root = float(true_root_input)  # set as float
    else: # else
        true_root = None # set true root as None
    root, iterations = newton_method(x0, delta, func, func_derivative, stop_flag, true_root) # call function netwon and return root and iterations 
    print("\nNewton's Method Results")
    print("____________________________________\n")
    print(f"Function: {function_input}")
    print("Initial Approximation:", x0)
    print("Tolerance (delta):", delta)
    print("Stopping Criterion (Flag):", stop_flag)
    print("Root found:", root)
    print(f"Number of iterations: {iterations}")
    if true_root is not None:
        true_error = np.abs(root - true_root)
        print(f"True error: {true_error}")
main()
