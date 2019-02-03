def geldige_zet(kaas):
    if kaas[0] in 'KDTLP' and kaas[1] in 'abcdefgh' and kaas[2] in '12345678':
        mes = True

    elif kaas[0] in 'abcdefgh' and kaas[1] in '12345678':
        mes = True
    elif len(kaas) > 3:
        mes = False
    else:
        mes = False
    return mes

def geldige_zetten(tuple):
    i = 0
    mes = True
    while geldige_zet(tuple[i]) == True and mes != False and i < len(tuple) - 1:
        i += 1
        mes = True
    if i == len(tuple) -1:
        mes = True
    else:
        mes = False
    return mes


print(geldige_zet('De5'))
print(geldige_zet('LYKFB'))
print(geldige_zet('c8'))

print(geldige_zetten(('f8', 'XZJM', 'Pa3', 'Pf3')))
print(geldige_zetten(('Ta1', 'e5', 'h8', 'f7', 'Db7', 'Lg3')))
