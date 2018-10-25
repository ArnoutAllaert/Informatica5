from math import sqrt
#invoer
x = float(input('Geef x∈R: '))

#bewerking
if x < 2:
    mes = str(round(x, 2)) + ' is ∉ dom(f)'
elif sqrt(x - 2) == 0:
    mes = str(round(x,2)) + ' is nulpunt van f'
else:
    mes = 'f(' + str(round(x, 2)) + ') = ' + str(round(sqrt(x - 2),2))

#uitvoer
print(mes)