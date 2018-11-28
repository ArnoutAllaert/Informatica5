#priemgetallen

getal = int(input('getal: '))
#zolang je het niet kan delen door 2,3,4 is het allicht een priemgetal
deler = 2

while getal % deler != 0 and getal != 1:
    deler += 1

if deler == getal:
    mes='priemgetal'
else:
    mes='geen priemgetal'

print(mes)