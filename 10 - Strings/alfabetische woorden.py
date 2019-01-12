def positie_laagste_ascii(woord):
    laag = 'z'
    for letter in woord:
        if ord(letter) < ord(laag):
            laag = letter
    return woord.find(laag)

def sorteer(woord):
    gesorteerd = ''
    laag = 'z'
    for letter in woord:
    ### letter is bv. 'k' en gesorteerd = 'abl', dan moet gesorteerd 'abkl' worden en niet 'ablk'
        #for i in gesorteerd:
           #if ord(letter) <= ord(i):
               #gesorteerd = gesorteerd[:woord.find(i) - 1] + letter + gesorteerd[woord.find(i):]
        if ord(letter) <= ord(laag):
            gesorteerd = letter + gesorteerd
            laag = letter
        else:
            gesorteerd += letter
    return gesorteerd

def is_alfabetisch(woord):
    if sorteer(woord) == woord:
        mes = True
    else:
        mes = False
    return mes

print(sorteer('9 * (7 - 2) = 45'))