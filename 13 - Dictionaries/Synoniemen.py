def synoniemen(zin, synoniem):
    zin = zin.split()

    for i in range(len(zin)):
        if zin[i] in synoniem:
            zin[i] = synoniem.get(zin[i])
    zin = ' '.join(zin)
    return zin


print(synoniemen('knoeien levert stoute leerlingen een straf op',{'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))
#'broddelen levert stoute leerlingen een sanctie op'