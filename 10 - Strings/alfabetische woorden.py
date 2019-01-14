def positie_laagste_ascii(woord):
    laag = 'z'
    for letter in woord:
        if ord(letter) < ord(laag):
            laag = letter
    return woord.find(laag)

def sorteer(woord):
    gesorteerd = ''
    laag = 500
    hoog = 1
    for letter in woord:
        if ord(letter) <= laag:
            if ord(letter) >= hoog:
                gesorteerd = letter + gesorteerd
                laag = ord(letter)
                hoog = ord(letter)
            else:
                gesorteerd = letter + gesorteerd
                laag = ord(letter)
        elif ord(letter) > laag:
            if ord(letter) >= hoog:
                gesorteerd += letter
                hoog = ord(letter)
            else:
                gesorteerd = gesorteerd[:gesorteerd.find(chr(hoog)) -1] + letter + gesorteerd[gesorteerd.find(chr(hoog)):]
    return gesorteerd

def is_alfabetisch(woord):
    if sorteer(woord) == woord:
        mes = True
    else:
        mes = False
    return mes

print(sorteer('9 * (7 - 2) = 45'))