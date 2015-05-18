#dit programma vind palyndroomnummers die product zijn van twee 3-cijferige nummers met een lengte van 6 cijfers :-)

palins=[]
mog=[]

for i in range (100,999):
    for j in range(100,999):
        mogelijkheid=i*j
        mogelijkheid=str(mogelijkheid)
        mog.append(mogelijkheid)

for j in mog:
    j = str(j)
    if len(j)==6:
        if j[0]==j[5] and j[1]==j[4] and j[2]==j[3]:
            palins.append(j)

print(max(palins))
    
    