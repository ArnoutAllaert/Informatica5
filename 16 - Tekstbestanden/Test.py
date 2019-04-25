#lijnen = []
#with open('klas.txt') as bestand:
#    lijnen = bestand.readlines()

#print('Er zitten ' + str(len(lijnen)) + ' personen in de klas.')

nieuwe_leerlingen = ['Alice\n', 'Baptiste']

with open('klas.txt', 'w') as bestand:
    bestand.writelines(nieuwe_leerlingen)