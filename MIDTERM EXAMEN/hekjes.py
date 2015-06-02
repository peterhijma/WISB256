import math
import time

lengte=int(input())

counter=0

for i in range(lengte):
    x=input()
    y=list(x)
    for j in y:
        if j=='#':
            counter=counter+1

print('Om de hekjes in dit weiland te verven heb je', 5*counter, 'liter verf nodig')