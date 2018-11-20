#invoer
getal = int(input('Geef getal: '))
x = 2
y = 1

#bewerking
while x < getal:
    if (getal % x) == 0:
        uitkomst = str(getal) + ' is geen priemgetal'
        y = 0
    x += 1
if y and getal != 1:
    uitkomst = str(getal) + ' is een priemgetal'

elif getal == 1:
    uitkomst = '1 is geen priemgetal'

#uitvoer
print(uitkomst)