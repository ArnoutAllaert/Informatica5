#invoer
woord = str(input('Geef verborgen woord: '))
geld = int(input('gedraaid geldbedrag: '))
letter = str(input('Geef letter: '))
totaal_geld = 0
kaas = ''
#bewerking
while letter in woord and letter not in kaas:
    totaal_geld += geld
    kaas += letter
    letter = str(input('Geef letter: '))

if letter not in woord:
    totaal_geld += 0

#uivoer
print(totaal_geld)