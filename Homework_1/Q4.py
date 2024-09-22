import math

# Define the function
def f(x):
    return (2 * math.sin(x) / 4) - math.exp(-x) - 1

# Bisection method implementation
def bisection_method(a, b, tol=1e-6, max_iter=1000):
    if f(a) * f(b) >= 0:
        print("The bisection method cannot proceed. f(a) and f(b) must have opposite signs.")
        return None
    
    for _ in range(max_iter):
        midpoint = (a + b) / 2
        if f(midpoint) == 0:  # Exact root found
            return midpoint
        
        if f(a) * f(midpoint) < 0:
            b = midpoint  # Root is in the left subinterval
        else:
            a = midpoint  # Root is in the right subinterval
        
        # Check stopping criteria
        if abs(b - a) < tol:  # Absolute error criterion
            return midpoint

    return (a + b) / 2  # Return the midpoint as the root

# Finding roots
# Root in interval [-7, -5]
root1 = bisection_method(-7, -5)
print(f"Root in [-7, -5]: {root1}, f(root1) = {f(root1)}")

# Root in interval [-5, -3]
root2 = bisection_method(-5, -3)
print(f"Root in [-5, -3]: {root2}, f(root2) = {f(root2)}")
