#Author: Narayan Prasad Ghimire
#Question number 4
#BisectionMethod

import math  
#Define the function f(x)= xsin(x)-1
#Error 0.001 bhanda thorai xa
def d(n):
    return n * math.sin(n) - 1

#bisection method function define gareko
def bisection_method(a, b, tol):
    #Check if the initial interval is valid
    if d(a) * d(b) >= 0:
        print("Bisection method fails.")
        return None
    
    c = a  #Initialize the midpoint
    
    #Iterate until the interval width is less than the tolerance
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0  
        if d(c) == 0:  #If the midpoint is a root, break the loop
            break
        elif d(a) * d(c) < 0:  #root left subinterval ma xa bhane
            b = c
        else:  #root right subinterval ma xa bhane
            a = c
    
    return c  

# Define the interval [a, b] and the tolerance
a = 0
b = 2
tol = 0.001

# Call the bisection method and store the result
root = bisection_method(a, b, tol)

# Print the result if a root was found
if root is not None:
    print(f"The root is approximately: {root:.4f}")


