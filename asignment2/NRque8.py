#Author: Narayan Prasad Ghimire
#Question number 8
#Newton Raphson Method
import math
# Define the function f(x) = ln(x) - 1
def d(n):
    return math.log(n) - 1
# Initial guess
n0 = 2.0

# derivative nikaleko f'(x) = 1/x
def d_prime(n):
    return 1 / n

# Implementing the Newton-Raphson method
def newton_raphson(n0, tolerance=1e-3, max_iterations=100):
    n = n0  
    for i in range(max_iterations):  
        n_new = n- d(n) /d_prime(n)  # Newton-Raphson formula
        if abs(n_new - n) < tolerance:  # Check if the result is within the desired tolerance
            return round(n_new, 3)  # Return the root rounded to 3 decimal places
        n = n_new  # naya value ma x lai update gareko
    return round(n, 3)  # Return the root if max_iterations is reached


#  Newton-Raphson method use garera root nikaleko
root = newton_raphson(n0)
print(f"Root: {root}")  # Print the root