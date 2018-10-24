#invoer
x = int(input('Geef aantal sol: '))
#bewerking
aarde = x * (24 * 60 * 60 + 39 * 60 + 35.244)
dagen = aarde // (24 * 60 * 60)
r1 = aarde % (24 * 60 * 60)
uren = r1 // (60 * 60)
r2 = r1 % (60 * 60)
minuten =  r2 // (60)
r3 = r2 % (60)
seconden = r3 // 1

aantal_dagen = str(x) + ' sol = ' + str(int(dagen)) + ' dagen, ' + str(int(uren)) + ' uren, ' + str(int(minuten)) + ' minuten en ' + str(int(seconden)) + ' seconden'

#uitvoer
print(str(aantal_dagen))