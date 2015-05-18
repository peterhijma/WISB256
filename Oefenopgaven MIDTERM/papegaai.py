import sys
import math
import random

eerst=int(input())

pap=[]

for i in range(eerst):
    x=input()
    pap.append(x)

for j in pap:
    y=j.split()
    if len(y)>4:
        print('Crackers!')
    else:
        print(j,'krAh!')