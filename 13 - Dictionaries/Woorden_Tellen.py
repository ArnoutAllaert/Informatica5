def woord_frequentie(zin):
    woorden = zin.replace('.', '').lower().split()
    aantal = {}
    for i in woorden:
        if i in aantal:
            aantal[i] += 1
        else:
            aantal[i] = 1
    return aantal

def woorden_per_frequentie(zin):
    zin = woord_frequentie(zin)
    kaas = {}
    for key, value in zin.items():
        if value in kaas:
            kaas[value] += [key]
        else:
            kaas[value] = [key]
    return kaas

def meest_gebruikte_woorden(zin):
    zin = woorden_per_frequentie(zin)
    waarden = []
    for key in zin.keys():
        waarden += [key]
    hoogste = max(waarden)
    return zin[hoogste]

print(meest_gebruikte_woorden('Dit is een zin. En nog een zin. En een laatste zin.'))
#['een', 'zin']