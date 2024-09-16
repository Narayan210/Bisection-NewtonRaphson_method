#Author: Narayan Prasad Ghimire
#Question number 10
#Newton Raphson Method

import math

# Define the function f(x) = x * sin(x) - 1
def f(n):
    return n * math.sin(n) - 1
# Initial guess
n0 = 1.0

# Define the derivative of the function f'(x) = sin(x) + x * cos(x)
def f_prime(n):
    return math.sin(n) + n * math.cos(n)

# Implement the Newton-Raphson method
def newton_raphson(n0, tolerance=1e-6, max_iterations=100):
    n = n0  # Initialize n with the initial guess n0
    for i in range(max_iterations):  # Iterate up to max_iterations times
        n_new = n - f(n) / f_prime(n)  # Apply the Newton-Raphson formula
        if abs(n_new - n) < tolerance:  # Check if the result is within the desired tolerance
            return n_new  # Return the root if within tolerance
        n = n_new  # Update n to the new value
    return n  # Return the root if max_iterations is reached

# Find the root using the Newton-Raphson method
root = newton_raphson(n0)
print(f"Root: {root:.6f}")  # Print the root rounded to 6 decimal places
