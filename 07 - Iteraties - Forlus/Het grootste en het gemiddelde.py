#invoer
getallen= int(input('aantal getallen xi∈Z: '))
max = int(input('getak: '))
som = max

#bewerking
for i in range(getallen - 1):
    getal = int(input('getal: '))
    som += getal
    gemiddelde = som / getallen
    if getal > max:
        max = getal
#uitvoer
print('Het grootste getal is {} en het gemiddelde is {:.2f}'.format( max, gemiddelde))
