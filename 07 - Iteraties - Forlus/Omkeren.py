#invoer
woord = str(input('geef een woord: '))
nieuw_woord = ''
#bewerking

for letter in woord:
    nieuw_woord = letter + nieuw_woord

#uitvoer
print(nieuw_woord)