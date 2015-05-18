n=int(input())

nietpriem = set()
priem = []
for i in range(2, n):
    if i in nietpriem:
        continue
    for j in range(i*i, n+1, i):
        nietpriem.add(j)
    if len(priem)<10001:
        priem.append(i)   

print(len(priem))
print(max(priem))