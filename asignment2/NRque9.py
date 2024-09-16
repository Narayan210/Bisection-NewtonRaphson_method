#Author: Narayan Prasad Ghimire
#Question number 9
#Newton Raphson Method

import math  

# Define the function f(x) = x^3 - 6x^2 + 11x
def f(n):
    return n**3 - 6*n**2 + 11*n

def f_prime(n):
    return 3*n**2 - 12*n + 11

def newton_raphson(n0, tolerance=1e-7, max_iterations=100):
    n = n0
    for _ in range(max_iterations):
        fn = f(n)
        fpn = f_prime(n)
        if fpn == 0:  # Avoid division by zero
            raise ValueError("Derivative is zero; Newton-Raphson method fails.")
        n_new = n - fn / fpn
        if abs(n_new - n) < tolerance:
            return n_new
        n = n_new
    raise ValueError("Maximum iterations exceeded; solution did not converge.")

# Example usage:
initial_guess = 1.5
root = newton_raphson(initial_guess)
print(f"Root: {root}")

