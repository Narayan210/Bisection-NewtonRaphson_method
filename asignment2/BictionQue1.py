# question1
#Author: Narayan Prasad Ghimire
# Define the function for f(x) = x^3 - 4x - 9
#BisectionMethod

import math
def d(n):
    return n**3 - 4*n - 9

# Initial interval
n1 = 2
n2 = 3

# Function values at initial points
y1 = d(n1)
y2 = d(n2)

# Check if root exists in the interval
if y1 * y2 > 0:
    print('No roots exist within the given interval')
    exit()

# Bisection method loop
for i in range(1, 101):
    # Midpoint of the interval
    nh = (n1 + n2) / 2
    yh = d(nh)
    
    # Check for convergence (close to zero with tolerance 0.001)
    if abs(yh) < 1.0e-3:
        break
    # Update the interval based on the sign of function values
    elif y1 * yh < 0:
        n2 = nh  # Update x2, x1 stays the same, no need to recalculate y1
    else:
        n1 = nh  # Update x1, so we need to recalculate y1
        y1 = yh  # Recalculate y1 only when x1 is updated

# Print the root and number of iterations
print('The root: %.3f' % nh)
print('Number of bisections: %d' % i)

