naam = input("Wat is je naam? ")

while True:
    x=input("Hoeveel groeten wil je? ")
    try:
        x=int(x)
        break
    except ValueError:
        print('Kies integer')
print(str(x)+' x gegroet, '+naam+'!')
