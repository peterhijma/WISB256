k=int(input())

woordenboek=[]

for i in range(k):
    x=str(input())
    y=list(x)
    woordenboek.append(y)

n=int(input())

swipes=[]

for j in range(n):
    u=str(input())
    v=list(u)
    swipes.append(v)
    
kanshebbers=[]    

for x in range(len(swipes)):
    y=swipes[x]
    for z in woordenboek:
        if y[0]==z[0]:
            kanshebbers.append(y)

grotekanshebbers=[]

for g in range(len(kanshebbers)):
    h=kanshebbers[g]
    for z in woordenboek:
        if h[-1]==z[-1]:
            grotekanshebbers.append(h)
            
print(kanshebbers)
print(grotekanshebbers)

noggroter=[]

for u in grotekanshebbers:
    for p in range(len(u)):
        for z in woordenboek:
            for o in range(len(z)):
                if u[p]==z[o]:
                    noggroter.append(u)

for c in noggroter:
    for v in noggroter:
        if c==v:
            noggroter.remove(v)

    
print(noggroter)