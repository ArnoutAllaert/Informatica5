#invoer
getallen= int(input('aantal getallen xi∈Z: '))
max = -87304958934789679237595637846586
som = 0

#bewerking
for i in range(getallen):
    getal = int(input('getal: '))
    if getal > max:
        max = getal
    som += getal
    gemiddelde = round((som / getallen), 2)

#uitvoer
print('{} {:d} {} {:.2f}'.format('Het grootste getal is ', max ,' en het gemiddelde is ', gemiddelde))
