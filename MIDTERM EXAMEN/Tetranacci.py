import sys
import math
import os

getal=int(input())

tetra=[]

tetra.append(0)
tetra.append(0)
tetra.append(1)
tetra.append(1)

while len(tetra)<getal:
    x=tetra[-4]+tetra[-3]+tetra[-2]+tetra[-1]
    tetra.append(x)

print(tetra[-1])