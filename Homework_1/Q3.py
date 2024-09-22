import numpy as np
import math

def main():
    intervals = []
    
    
    for i in range(2): 
        print(f"Enter the interval {i + 1}:")
        x1 = float(input(f"Enter the lower bound of interval {i + 1}: "))
        x2 = float(input(f"Enter the upper bound of interval {i + 1}: "))
        intervals.append((x1, x2)) 
    delta = float(input('Enter the Delta (δ): '))
     
    
    true_root_input = input('Optional true root: ')
    true_root = float(true_root_input) if true_root_input else None


    for idx, (x1, x2) in enumerate(intervals):
        print(f"\nRoot in the interval {x1}, {x2}")
        
        for flag in ['A', 'B', 'C', 'D']:
            print(f"\nUsing stopping criterion: {flag}")
            root, iterations = bisection_method(x1, x2, delta, flag, true_root)
            
           
            print("\nBisection Method Results")
            print("____________________________________\n")
            print("Function: f(x) = 2*sin(x) - (e^(x)/4) - 1")
            print("Interval:", x1, ",", x2)
            print("Tolerance (delta):", delta)
            print("Stopping Criterion (Flag):", flag)
            print("Root found:", root)
            print("f(root):", function(root))
            print("Number of iterations:", iterations)

           
            if flag in ['C', 'D'] and true_root is not None:
                true_error = np.abs(root - true_root)
                print(f"True error: {true_error}")

            
            print(f"Closeness of f(root) to 0: {np.abs(function(root))}\n")

def bisection_method(x1, x2, delta, flag, true_root):
    iteration = 0 
    prev_midpoint = None
    approx_error = float('inf')  

 
    if function(x1) * function(x2) > 0:
        print('No root in the given interval. Try again.')
        return None, None

    while True:
        iteration += 1
        midpoint_val = (x1 + x2) / 2.0
        function_mid = function(midpoint_val)
        if np.abs(function_mid) < 1e-12:
            root = midpoint_val
            break
        if function(x1) * function_mid < 0:
            x2 = midpoint_val
        else:
            x1 = midpoint_val
        if prev_midpoint is not None:
            approx_error = np.abs(midpoint_val - prev_midpoint)
        rel_error = np.abs(approx_error / midpoint_val) * 100 if midpoint_val != 0 else float('inf')
        true_error = np.abs(midpoint_val - true_root) if true_root is not None else None
        prev_midpoint = midpoint_val
        if flag == 'A' and approx_error < delta:  # Absolute Approximate Error
            break
        elif flag == 'B' and rel_error < delta:  # Relative Approximate Error
            break
        elif flag == 'C' and true_error is not None and true_error < delta:  # True Absolute Error
            break
        elif flag == 'D' and approx_error < delta and true_error is not None and true_error < delta:  # Both Approximate and True Error
            break
    return midpoint_val, iteration
def function(x):
    return (2 * math.sin(x)) - (math.exp(x) / 4) - 1

main()
