def fruitmand_maken(mand):
    mandje = {}
    for i in mand:
        mandje[len(i)] = i

    return mandje

def fruitmand_inpakken(mand):
    keze = []
    for v in mand.values():
        keze += [v]
    kaas = [keze[0]]
    for i in range(1, len(keze)):
        if len(keze[i]) > len(kaas[len(kaas) - 1]):
            kaas += [keze[i]]
        elif len(keze[i]) < len(kaas[0]):
            kaas = [keze[i]] + kaas
        else:
            a = 0
            while a < len(kaas) -1:
                if len(kaas[a]) < len(keze[i]) and len(keze[i]) < len(kaas[a + 1]):
                    kaas = kaas[: a+1] + [keze[i]] + kaas[a+1:]
                a += 1
    return kaas

print( fruitmand_maken(['banaan', 'aardbei', 'kiwi', 'peer', 'appel', 'bes', 'sinaasappel', 'framboos']))
print(fruitmand_inpakken({6: 'banaan', 7: 'aardbei', 4: 'peer', 5: 'appel', 3: 'bes', 11: 'sinaasappel', 8: 'framboos'}))
