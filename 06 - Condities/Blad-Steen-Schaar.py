# invoer
x = str(input('blad, stten, schaar: '))
y = str(input('blad, stten, schaar: '))

#bewerking
if x == y:
    uitkomst = 'onbeslist'

if (x == 'blad' and y == 'steen') or (x == 'steen' and y == 'schaar') or (x == 'schaar' and y == 'blad'):
    uitkomst = 'speler 1 wint'

if (x == 'steen' and y == 'blad') or (x == 'schaar' and y == 'steen') or (x == 'blad' and y == 'schaar'):
    uitkomst = 'speler 2 wint'

# uitvoer
print(uitkomst)