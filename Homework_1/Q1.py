import numpy as ny

def main():
    x1 = int(input('Enter the lower bound of interval: '))
    x2 = int(input('Enter the upper bound of interval: '))
    delta = float(input('Enter the Delta (δ):'))
    flag = Flag()
    true_root = input('Optional true root: ')
    if true_root: 
        true_root = float(true_root)
    else:
        true_root = None
    root, iter = bisection_method(x1, x2, delta, flag, true_root )
    print("Bisection Method Results")
    print("____________________________________\n")
    print("Function: f(x) = x^3 - x - 2")
    print("Interval:", x1 ,"," , x2)
    print("Tolerance (delta):" , delta)
    print("Stopping Criterion (Flag): ", flag)
    print("Root found:", root)
    print("f(root): " , f(root))
    print(f"Number of iterations:", iter)
    if flag == 'C' or flag == 'D' and true_root is not None:
        true_error = abs(root - true_root)
        print(f"True error: {true_error}")
    print(f"Closeness of f(root) to 0: {ny.absolute(f(root))}\n")

# Here is where the bisection function starts
def bisection_method (x1, x2, delta, flag, true_root):
    iteration = 0  # I set the iteration to 0 because we will need it for the while loop when we iterate + 1 through each loop 
    midpoint_val = x1 # we set the midpoint value x3 from flowchart = x1
    approx_error = 1e12 #large value close to infinity
    prev_midpoint = None # no previous midpoint but can be set later in the loop
    
    if f(x1) * f(x2) > 0: # here we call the function called function in which it takes the parameter of x1 or x2, it will return the value pf x1 and x2 when input into the fucntion. its the first art of the flowchart in which it checks if the value f(x1) * f(x2) > 0
        print('No root in the given interval. Try again.') #if its greater than then it will print the issue
        main() # the user is sent back to the mian function and to restart from the beginning
    
    # bisection loop
    while True: #used a while loop as this problem a for loop cant be used (cant tell how many iterations needed)
        iteration += 1 #we add + 1 iteration after every loop unless it breaks
        midpoint_val = (x1 + x2) / 2.0 # take x1 and x2 / 2 to get the midpoint value 
        function_mid = f(midpoint_val) #call the function function lol sorry about that, named it function the function. we need the function value when we put the new midpoint

        # here an if statement is used to check if that function midpoint value is near 0, cant be exactly zero but near is good. 
        if ny.absolute(function_mid) < 1e-12: # 1e-12 is like saying -inf smiliar to how + inf is 12-12
            root = midpoint_val # if its near that value then its save to assume that value is the root and we can break out the loop
            break # here we break out -> return iteration + the root (goes back to the main function after return statement)

        # Continue with the flow chart, we must update the interval. here is where we check if function (x1) * function_mid(function value when we input the first)
        if f(x1) * function_mid < 0: # if condiiton is satisfied then we can set it as the new x2
            x2 = midpoint_val 
        else:
            x1 = midpoint_val # else it will be x1 as new iterval for x1

        # this if statement will check if its not empty
        if prev_midpoint is not None:
            approx_error = ny.absolute(midpoint_val - prev_midpoint) # if nopt empty then calculate the approx error using difference between midpoint
        
        # Calculate relative error
        if midpoint_val != 0: # check  if value is not equal to 0
            rel_err = ny.absolute(approx_error / midpoint_val) * 100 # calulcate relative error
        else: #else do rel err as inifinty
            rel_err = float('inf')  # Practically infinite

        # Calculate true error if true_root is given (its optional)
        if true_root: # if statment to calculate the true error if its filled, its based on if user input a value
            true_root = float(true_root) #set value as float to expand the number so its more than double or int
            true_error = ny.absolute(midpoint_val - true_root) # this is to calculate the true error
        else: # else if it doesnt have true error 
            true_error = None # if no true root then it will set true error as none, it wont display in main function 

       
        #print(f"Iteration: {iteration}, Midpoint: {midpoint_val}")
        prev_midpoint = midpoint_val  # Update previous midpoint for the next iteration

        # Applies a stopping criteria based on flag either a, b, c, d
        if flag == 'A':  # Absolute Approximate Error
            if approx_error < delta: #if approx_error less than delta (1e-6) 
                print("Stopping due to Approximate Error")
                break  # break out of while loop and return root and iteration
        elif flag == 'B':  # Relative Approximate Error
            if rel_err < delta: #rel error <delta
                print("Stopping due to Relative Error")
                break # break out of while loop and return root and iteration
        elif flag == 'C':  # True Absolute Error
            if true_error is not None and true_error < delta: # true error must be filled and true _ error < delta
                print("Stopping due to True Error")
                break # break out of while loop and return root and iteration
        elif flag == 'D':  # Both Approximate and True Error
            if approx_error < delta and true_error is not None and true_error < delta: #true error must br filled, approx < delta and  true error is  < delta
                print("Stopping due to Both Approximate and True Error")
                break # break out of while loop and return root and iteration
    return midpoint_val, iteration #return midpoint and iteration
def f(x):
    return x**3 - x - 2   # asked chatgpt based on my code to break a code that satifies for q1
def Flag():
    options = ["A) An absolute approximate error is used to stop the process. You may predict the number of iterations in advance in such a case.", "B) An absolute relative approximate error is used to stop the process", "C) Estimation of a true absolute error is used to stop the process.", "D) Conjunction of an absolute approximate error and an estimated true absolute error is used to stop the process."]
    for items in options:
        print(items)
    flag = input('What stopping criterion flag would you like to use[a - d]: ')[0]
    flag = flag.upper()
    if(flag == 'A' or flag == 'B' or flag == 'C' or flag == 'D' ):
        return flag
    else: 
        print('\nNot valid flag stopping criterion. Input either A,B,C or D... \n')
        print('loading \n')
        Flag()
main()