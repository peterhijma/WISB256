import sys
import os
import math

gr1=list(str(one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eightteen, nineteen, twenty))
#30 = thirty
#40 = forty
#50 = fifty
#60 = sixty
#70 = seventy
#80 = eighty
#90 = ninety
#100 = hundred
#1000 = thousand

letter=[]

for i in (0,19):
    i=gr1[i]
    letter.append(len(i))

print(letter)