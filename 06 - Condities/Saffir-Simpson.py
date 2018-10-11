# invoer
x = float(input('Geef windsnelheid: '))

#berekening

if x < 119:
    uitkomst = 'geen orkaan'

if x >= 119 and x <= 153:
    uitkomst = 'categorie 1'

if x >= 154 and x <= 177:
    uitkomst = 'categorie 2'

if x >= 178 and x <= 209:
    uitkomst = 'categorie 3'

if x >= 210 and x <= 249:
    uitkomst = 'categorie 4'

if x >= 250:
    uitkomst = 'categorie 5'

# uitvoer
print(uitkomst)