import time
import sys
import math

n=int(sys.argv[1])

T1 = time.perf_counter()

nietpriem = set()
priem = []
for i in range(2, n):
    if i not in nietpriem:
        priem.append(i)
        document=open(sys.argv[2],'w')
        document.write("\n".join(map(lambda x: str(x), priem)))
        document.close()
        for j in range(i*i, n+1, i):
            nietpriem.add(j)
              

T2 = time.perf_counter() 

print(str(len(priem)), 'priemgetallen gevonden in ', T2 - T1, 'seconden')
print('Argument List:', str(sys.argv))