#invoer
prijs = int(input('geef prijs: '))
totaal = 0

#bewerking
while prijs > 0:
    totaal+= prijs
    prijs = int(input('geef prijs: '))


print('De totale prijs is €' + str(totaal))