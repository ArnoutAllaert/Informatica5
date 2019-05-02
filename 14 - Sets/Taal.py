def behoort_tot_taal(woord, letters):
    kaas = set(woord)
    kaas.discard(' ')

    return kaas.issubset(letters) and woord != ''

def is_onleesbaar(woord, taal):
    kaas = set(woord)
    kaas.discard(' ')
    heuj = kaas.intersection(taal)
    return len(heuj) <= 1

print(is_onleesbaar('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(is_onleesbaar('ambigu',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))