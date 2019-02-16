def volgende_rij(list):
    volgende = []
    for i in range(len(list) - 1):
        if list[i] == list[i +1]:
            volgende += [list[i]]
        elif list[i] == 'R' and list[i + 1] == 'Y' or list[i] == 'Y' and list[i +1] == 'R':
            volgende += ['G']
        elif list[i] == 'R' and list[i + 1] == 'G' or list[i] == 'G' and list[i +1] == 'R':
            volgende += ['Y']
        else:
            volgende += 'R'
    return volgende

def driehoek(basis):
    mes = [basis]
    for i in range(0, len(basis) -1):
        mes += [volgende_rij(mes[i])]
    return mes

def kleuren(driehoek):
    g = 0
    r = 0
    y = 0
    for i in range(0, len(driehoek)):
        g += driehoek[i].count('G')
        r += driehoek[i].count('R')
        y += driehoek[i].count('Y')
    return g, r, y

print(kleuren([['G', 'G', 'G', 'G', 'G'], ['G', 'G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G'], ['G']]))
#(15, 0, 0)
print(kleuren([['Y', 'R', 'G', 'Y', 'Y'], ['G', 'Y', 'R', 'Y'], ['R', 'G', 'G'], ['Y', 'G'], ['R']]))
#(5, 4, 6)