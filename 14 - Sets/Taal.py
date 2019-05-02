def behoort_tot_taal(woord, letters):
    kaas = set(woord)
    kaas.discard(' ')

    return kaas.issubset(letters) and woord != ''

def is_onleesbaar(woord, taal):
    kaas = set(woord)
    kaas.discard(' ')
    heuj = kaas.intersection(taal)

    return len(heuj) < 1

def perfect_woord(woord, taal):
    kaas = set(woord)
    kaas.discard(' ')
    heuj = kaas.intersection(taal)

    return len(heuj) == len(taal)

print(perfect_woord('hello world',{'e', 'l', 'h', 'r', 'o', 'w', 'd'}))