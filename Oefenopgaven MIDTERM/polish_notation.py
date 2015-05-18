import sys
import math

som=str(input())

gebruik=som.split()

x=gebruik[2]
if x=='-': 
    y=int(gebruik[0])-int(gebruik[1])
if x=='+':
    y=int(gebruik[0])+int(gebruik[1])
if x=='*':
    y=int(gebruik[0])*int(gebruik[1])
if x=='/':
    y=int(gebruik[0])/int(gebruik[1])
    
print("{0:.3f}".format(y))