import time
import sys
import math

n=int(sys.argv[1])

T1 = time.perf_counter()

document=open(sys.argv[2],'w')

nietpriem = set()
priem = []
for i in range(2, n):
    if i in nietpriem:
        continue
    for j in range(i*i, n+1, i):
        nietpriem.add(j)
    priem.append(i)   
    
document.write("\n".join(map(str, priem)))
document.close()

T2 = time.perf_counter() 

print(str(len(priem)), 'priemgetallen gevonden in ', T2 - T1, 'seconden')