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

output=[]

for i in swipes:
    for j in woordenboek:
        if i[0]!=j[0]:
            output.append('?')
        if i[-1]!=j[-1]:
            output.append('?')
        else:
            for n in range(len(woordenboek)):
                if all(i[m] in j[n] for m in range(len(i))):
                    output.append(j[n])

#for x in output:
    #for y in output:
        #if x==y:
            #output.remove(y)
            
for i in range(n):
    print(''.join(output[i]))