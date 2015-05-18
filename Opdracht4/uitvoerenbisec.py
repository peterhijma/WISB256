import bisection
import math

def f(x):
    return (x*x*x)+1

root = bisection.findRoot(f,-3,3,0.01)
print(root)