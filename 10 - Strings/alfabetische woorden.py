def positie_laagste_ascii(woord):
    laag = 'z'
    for letter in woord:
        if ord(letter) < ord(laag):
            laag = letter
    return woord.find(laag)

def sorteer(woord):
    gesorteerd = ''
    for letter in woord:
        laag = 'z'
        for letter in woord:
            if ord(letter) < ord(laag):
                laag = letter

        gesorteerd += laag
        a = woord.find(laag)
        woord = woord[0:a] + woord[a + 1:]
    return gesorteerd

def is_alfabetisch(woord):
    if sorteer(woord) == woord:
        mes = True
    else:
        mes = False
    return mes

print(sorteer('drenkeling'))
