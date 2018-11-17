#invoer
kaart = int(input('geef kaart tussen 1 en 11: '))
totaal = 0

#bewerking
while kaart > 0 and kaart +totaal < 21:
    totaal += kaart
    kaart = int(input('geef kaart tussen 1 en 11: '))
if kaart + totaal == 21:
    uitkomst = 'Gewonnen!'
elif kaart + totaal < 21:
    uitkomst = 'Voorzichtig gespeeld ({})'.format(totaal + kaart)
else:
    uitkomst = 'Verbrand ({})'.format(totaal + kaart)

#uitvoer
print(uitkomst)