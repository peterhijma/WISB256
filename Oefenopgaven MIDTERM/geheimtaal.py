zin=list(str(input()))
code=list(str(input()))

for i in range(0,len(zin)):
    x=ord(code[i%len(code)])
    x=x-97
    z=zin[i]
    y=ord(z)-x
    while y<97:
        y=y+26
    echteletter=chr(y)
    zin[i]=echteletter

print(''.join(zin))