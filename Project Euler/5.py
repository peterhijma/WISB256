multiples=[]
n=20
while len(multiples)==0:
    if all(n%i==0 for i in range(1,20)):
        multiples.append(n)
    else:
        n=n+20
        
print(multiples)