def behoort_tot_taal(woord, letters):
    kaas = set(woord)
    kaas.discard(' ')

    return kaas.issubset(letters) and woord != ''


print(behoort_tot_taal('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(behoort_tot_taal('ambigu',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(behoort_tot_taal('python',{'e', 'l', 'h', 'r', 'o', 'w', 'd'}))
print(behoort_tot_taal('',{'e', 'l', 'h', 'r', 'o', 'w', 'd'}))