# invoer
x = str(input('blad, steen, schaar: '))
y = str(input('blad, steen, schaar: '))

#bewerking
if x == y:
    uitkomst = 'onbeslist'

elif (x == 'blad' and y == 'steen') or (x == 'steen' and y == 'schaar') or (x == 'schaar' and y == 'blad'):
    uitkomst = 'speler 1 wint'

else:
    uitkomst = 'speler 2 wint'

# uitvoer
print(uitkomst)