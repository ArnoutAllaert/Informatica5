from math import sqrt
#invoer
x = float(input('Geef x∈R: '))

#bewerking

if x < 2:
    mes = '{:.2f}{}'.format(x, ' ∉ dom(f)')
elif sqrt(x - 2) == 0:
    mes = '{:.2f}{}'.format(x, ' is nulpunt van f')
else:
    mes = '{}{:.2f}{}{:.2f}'.format('f(', x ,') = ', sqrt(x - 2))

#uitvoer
print(mes)