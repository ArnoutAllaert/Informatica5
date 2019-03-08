def woord_frequentie(zin):
    woorden = zin.replace('.','').lower().split()
    aantal = {}
    for i in woorden:
        if i in aantal:
            aantal[i] += 1
        else:
            aantal[i] = 1
    return aantal

def woorden_per_frequentie(zin):
    frequentie = {}
    for v in woord_frequentie(zin).values():
        if v in frequentie:
            frequentie[v] += [woord_frequentie(zin).keys(v)]
        else:
            frequentie[v] = [woord_frequentie(zin).keys(v)]

    return frequentie

print(woorden_per_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))
#{1: ['dit', 'is', 'nog', 'laatste'], 3: ['een', 'zin'], 2: ['en']}