import math
import sys

def findRoot(f,a,b,epsilon):
    m=(a+b)/2
    if math.fabs(a-b)<epsilon:
        return m
    if f(a)*f(b)>0:
        print('Kies een beter interval')
        quit()
    if f(a)*f(b)==0:
        if f(a)==0:
            print('f(a) is een nulpunt')
            quit()
        else:
            print('f(b) is een nulpunt')
            quit()
    if f(a)>f(b):
        if f(m)>0:
            return findRoot(f,m,b,epsilon)
        else:
            return findRoot(f,a,m,epsilon)
    else:
        if f(m)>0:
            return findRoot(f,a,m,epsilon)
        else:
            return findRoot(f,m,b,epsilon)

        
#y=findRoot(lambda x:x*x*x,-4,1,.1)
#if y==False:
#    print('')
#else:
#    print(y)