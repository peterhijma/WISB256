tekst = list(str(input()))
code = list(str(input()))
for i in range(0,len(tekst)):
    x = ord(code[i % len(code)])
    x = x - 97
    new  = ord(tekst[i]) - x
    if new < 97:
        new += 26
    tekst[i] = chr(new)
print(''.join(tekst))