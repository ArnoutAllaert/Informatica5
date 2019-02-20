def kleur_toevoegen(list, kleur):
    if kleur == 'rood':
        list[0] += 1
    elif kleur == 'groen':
        list[1] += 1
    else:
        list[2] += 1
    return list

def is_wit(lijst):
    return lijst[0] == lijst[1] == lijst[2]

def verf_verzamelen(lijst):
    r = 0
    g = 0
    b = 0
    a = 0
    while a < len(lijst):
        if r == b == g and r != 0:
            a += 1000000000
        elif lijst[a] == 'rood':
            r += 1
        elif lijst[a] == 'groen':
            g += 1
        elif lijst[a] == 'blauw':
            b += 1
        a += 1
    if r == b == g and r != 0:
        return r + g + b, [r, g, b]


print(verf_verzamelen(['groen', 'groen', 'rood', 'groen', 'rood', 'groen', 'groen', 'rood', 'blauw', 'groen', 'groen', 'blauw', 'blauw', 'rood', 'rood', 'rood', 'blauw', 'rood']))
#None