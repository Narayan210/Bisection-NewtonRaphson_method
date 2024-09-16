#Author: Narayan Prasad Ghimire
#Question number 7
#Newton Raphson Method


import math
#Determine the root of f(x)=tan(x)-x

n = 4.5

# Newton-Raphson iteration
for iteration in range(1,101 ):
    nnew = n - (math.tan(n) - n) / (1 / math.cos(n)**2 - 1)
    if abs(nnew - n) < 0.0001: 
        break
    n = nnew

print('The root : %0.5f' % nnew)
print('The number of iterations : %d' % iteration)

