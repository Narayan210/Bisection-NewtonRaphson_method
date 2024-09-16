#Author: Narayan Prasad Ghimire
#Question number 5
#Newton Raphson Method

import math

# Define the function f(x) = x^2 - 2x - 3
def d(n):
    return n**2 - 2*n - 3

# Define the derivative of the function f'(x) = 2x - 2
def d_prime(n):
    return 2*n - 2

# Define the Newton-Raphson method
def newton_raphson(n0, iterations):
    n = n0
    for i in range(iterations):
        n = n - d(n) / d_prime(n)
        print(f"Iteration {i+1}: n = {n:.6f}")
    return n

# Initial guess
n0 = 4
# Number of iterations
iterations = 4

# Call the Newton-Raphson method
root = newton_raphson(n0, iterations)

print(f"The root after {iterations} iterations is approximately: {root:.6f}")
