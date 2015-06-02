import time
import sys
import math

n=int(input('Geef priem: '))

nietpriem = set()
priem = []
for i in range(2, n):
    if i in nietpriem:
        continue
    for j in range(i*i, n+1, i):
        nietpriem.add(j)
    priem.append(i)   

print('Som van priemgetallen onder het gegeven getal: ', sum(priem))
