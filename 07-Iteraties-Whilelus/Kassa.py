#invoer
prijs = float(input('geef prijs: '))
totaal = 0

#bewerking
while prijs > 0:
    totaal += prijs
    prijs = float(input('geef prijs: '))


print('{}{:.2f}'.format('De totale prijs is € ', float(totaal) ))