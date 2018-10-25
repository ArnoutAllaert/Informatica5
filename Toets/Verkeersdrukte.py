#input
dv = float(input('verkeersdichtheid van het vrachtvervoer op het eerste rijvak: '))
vv = float(input('snelheid van het vrachtverkeer op het eerste rijvak: '))
da = float(input('verkeersdichtheid van het personenvervoer op het tweede rijvak: '))
va = float(input('snelheid van de personenwagens op het tweede rijvak: '))

#berekening
pv = min((dv * vv)/40,1)
pa = min((da * va)/40,1)

if min(pv,pa) > 0.7:
    mes = 'zwart'
elif max(pv,pa) > 0.7 and abs(pv - pa) < 0.2:
    mes = 'rood'
elif abs(pv - pa) > 0.7:
    mes = 'geel'
else:
    mes = 'groen'
#uitvoer
print(mes)