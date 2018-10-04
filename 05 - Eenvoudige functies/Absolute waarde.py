# invoer
x = float(input('geef x: '))
y = float(input('geef y: '))

# bewerking
linkerlid = abs(x) - abs(y)
rechterlid = abs(x - y)

# uitvoer
print('{:.4f} ≤ {:.4f}'.format(linkerlid, rechterlid))