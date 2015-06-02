import sys
import math

som=str(input())

gebruik=som.split()

vervolg=[]

for i in range(len(gebruik)-3):
    if type(gebruik[i])==type(gebruik[i+1])==str:
        if gebruik[i+2]=='-':
            y=int(gebruik[i])-int(gebruik[i+1])
            vervolg.append(y)
            gebruik.remove(gebruik[i])
            gebruik.remove(gebruik[i+1])
            gebruik.remove(gebruik[i+2])
        if gebruik[i+2]=='+':
            y=int(gebruik[i])+int(gebruik[i+1])
            vervolg.append(y)
            gebruik.remove(gebruik[i])
            gebruik.remove(gebruik[i+1])
            gebruik.remove(gebruik[i+2])
        if gebruik[i+2]=='*':
            y=int(gebruik[i])*int(gebruik[i+1])
            vervolg.append(y)
            gebruik.remove(gebruik[i])
            gebruik.remove(gebruik[i+1])
            gebruik.remove(gebruik[i+2])
        if gebruik[i+2]=='/':
            y=int(gebruik[i])/int(gebruik[i+1])
            vervolg.append(y)
            gebruik.remove(gebruik[i])
            gebruik.remove(gebruik[i+1])
            gebruik.remove(gebruik[i+2])

    
print(vervolg)
print(gebruik)