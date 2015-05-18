lijstje=[]

for i in range(0,1000,3):
    lijstje.append(i)
for j in range(0,1000,5):
    if j not in lijstje:
        lijstje.append(j)
    

print(lijstje)
som=sum(lijstje)

print(som)
    