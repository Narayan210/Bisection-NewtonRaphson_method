#Author: Narayan Prasad Ghimire
#Question number 6
#Newton Raphson Method

import math

# Initial guess
n0 = 0.5
# Number of iterations
iterations = 5
def f(n):
    return n**3 - n + 1

def f_prime(n):
    return 3*n**2 - 1

def newton_raphson(n0, iterations):
    n = n0
    for i in range(iterations):
        n = n - f(n) / f_prime(n)
        print(f"Iteration {i+1}: n = {n}")
    return n

root = newton_raphson(n0, iterations)
print(f"Root after {iterations} iterations: {root}")
