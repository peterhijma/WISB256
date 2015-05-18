import sys
import math
import os

fibbo=[]

fibbo.append(1)
fibbo.append(2)

while max(fibbo) < 4000000:
    x=fibbo[-2]+fibbo[-1]
    fibbo.append(x)
    
if max(fibbo) > 4000000:
    fibbo.pop(-1)

print(fibbo)

even=[]

for i in fibbo:
    if i%2==0:
        even.append(i)
        
print(even)

print(sum(even))