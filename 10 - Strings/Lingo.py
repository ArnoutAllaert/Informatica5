def hint(gok, woord):
    mes = ''
    for i in range(0, len(woord)):
        if gok[i] in woord:
            if gok[i] == woord[i]:
                mes += gok[i].upper()
            else:
                mes += gok[i]
        else:
            mes += '.'

    return mes

print(hint('rockt', 'salet'))