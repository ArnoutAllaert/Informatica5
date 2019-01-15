def positie_laagste_ascii(woord):
    laag = 'z'
    for letter in woord:
        if ord(letter) < ord(laag):
            laag = letter
    return woord.find(laag)

def sorteer(woord):
    gesorteerd = ''


    return gesorteerd
def is_alfabetisch(woord):
    if sorteer(woord) == woord:
        mes = True
    else:
        mes = False
    return mes

print(sorteer('drenkeling'))