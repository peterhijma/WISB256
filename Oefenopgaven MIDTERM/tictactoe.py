#dit programma test winnaar van spelsituatie tic-tac-toe

import sys
import math
import os

rij1=list(str(input()))
rij2=list(str(input()))
rij3=list(str(input()))

for i in range(0,3):
    if rij1[i]=='0' or rij1[i]=='1' or rij1[i]=='2':
        True
    else:
        print('Geef aub realistische spelsituatie')

for j in range(0,3):
    if rij2[j]=='0' or rij2[j]=='1' or rij2[j]=='2':
        True
    else:
        print('Geef aub realistische spelsituatie')

for k in range(0,3):
    if rij3[k]=='0' or rij3[k]=='1' or rij3[k]=='2':
        True
    else:
        print('Geef aub realistische spelsituatie')
        
if rij1[0]==rij1[1]==rij1[2] or rij2[0]==rij2[1]==rij2[2] or rij3[0]==rij3[1]==rij3[2]:
    if rij1==1
