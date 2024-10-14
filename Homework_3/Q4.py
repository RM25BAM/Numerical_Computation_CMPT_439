import numpy as np

def f(x):
    return 2 * np.sin(x) - (np.exp(x) / 4) - 1

def f_prime(x):
    return 2 * np.cos(x) - (np.exp(x) / 4)

def newton_method(initial_guess, tolerance, max_iterations):
    x0 = initial_guess
    for i in range(max_iterations):
        fx0 = f(x0)
        fpx0 = f_prime(x0)

        if fpx0 == 0:  # Avoid division by zero
            print("Derivative is zero. Stopping iteration.")
            return None

        x1 = x0 - fx0 / fpx0  # Newton's method formula

        if abs(x1 - x0) < tolerance:  # Check for convergence
            return x1  # Found a root

        x0 = x1  # Update for next iteration

    print("Max iterations reached without convergence.")
    return None

# Example usage
if __name__ == "__main__":
    initial_guesses = [-3, 0, 3]  # Example initial guesses
    tolerance = 1e-6
    max_iterations = 10

    for guess in initial_guesses:
        root = newton_method(guess, tolerance, max_iterations)
        print(f"Root found starting from {guess}: {root}")
