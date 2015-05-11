import sys
import math
import random

needle_amount = int(sys.argv[1])
needle_length = float(sys.argv[2])
if len(sys.argv) == 4:
    random.seed(sys.argv[3])

hits = 0

def drop_needle(L):
    x = random.uniform(0,0.5)
    phi = random.uniform(0,math.pi/2)
    if L*math.cos(phi)/2>x:
        return True
        
for i in range(0,needle_amount):
    if drop_needle(needle_length) == True:
        hits += 1

if needle_length > 1:
    pi = round(((2*needle_length-2*(math.sqrt(needle_length*needle_length-1)+math.asin(1/needle_length)))/(hits/needle_amount-1)),6)
else:
    pi = round(2*needle_length*needle_amount/hits,6)
        
print(str(hits) +" hits in "+ str(needle_amount) + " tries \nPi = "+ str(pi))