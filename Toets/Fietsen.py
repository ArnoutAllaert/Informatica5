#invoer
stijn = int(input('Geef snelheid Stijn in m/s: '))
kaat = int(input('Geef snelheid Kaat m/s: '))
afstand = int(input('Geef afstand: '))
x = 1

#bewerking
while x * (stijn + kaat) < afstand:
    x += 1

#uitvoer
print('Na ' + str(x) + ' s hebben Stijn en Kaat elkaar ontmoet.')