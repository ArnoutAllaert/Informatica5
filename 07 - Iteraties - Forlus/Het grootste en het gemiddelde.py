#invoer
getallen= int(input('aantal getallen xi∈Z: '))
max = 0
nieuw_max = 0
som = 0

#bewerking
for i in range(getallen):
    getal = int(input('getal: '))
    if getal > max and getal > nieuw_max:
        nieuw_max = getal
    som += getal
    gemiddelde = round((som / getallen), 2)

#uitvoer
print('{} {:d} {} {:.2f}'.format('Het grootste getal is ', nieuw_max ,' en het gemiddelde is ', gemiddelde)
