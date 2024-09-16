#Author: Narayan Prasad Ghimire
#Question number 3
#BisectionMethod

import math  
# Define the function f(x)= e**x-3x
#Intervals (0, 1)

def d(n):
    return math.exp(n) - 3 * n

# Define the bisection method function
def bisection_method(a, b, tol):
    # Check if the initial interval is valid
    if d(a) * d(b) >= 0:
        print("No root exists within the given interval")
        return None
    
    c = a  # midpoint initialize gareko
    
    # Iterate until the interval width is less than the tolerance
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0  
        if d(c) == 0:  # If the midpoint is a root, break the loop
            break
        elif d(a) * d(c) < 0:  #  root left subinterval ma xa bhane
            b = c
        else:  # root right subinterval ma xa bhane
            a = c
    
    return c  # Return the approximate root

# Define the interval [0, 1] and the tolerance 0.001
a = 0
b = 1
tol = 0.001

# Call the bisection method and store the result
root = bisection_method(a, b, tol)

# Print the result if a root was found
if root is not None:
    print(f"The root is approximately: {root:.4f}")