import math
import time

x=input()
try:
    x=int(x)
except:
    x=str(x)

if type(x)==int:
    if x>2:
        print('Ug '+(x-2)*'ug '+'ug'+'!')
    if x==1:
        print('Ug!')
    if x==2:
        print('Ug ug!')
else:
    y=x.split()
    print(len(y))


    