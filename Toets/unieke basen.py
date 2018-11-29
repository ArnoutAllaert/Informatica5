#invoer
basen = int(input('Geef aantal basen: '))
ketting = ''
dna = ''
soort = 0
#bewerking
for i in range(basen):
    base = str(input('Geef een base: '))
    ketting += base
    if base not in dna:
        dna += base + ' '

for letter in dna:
    soort += 1

if (soort // 2) == 1:
    mes = 'De DNA-keting bevat 1 soort base: ' + str(dna)
else:
    mes = 'De DNA-keting bevat ' + str(soort // 2) + ' verschillende soorten basen: ' + str(dna)
#uivoer
print(mes)