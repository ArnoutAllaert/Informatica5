def hint(gok, woord):
    mes = ''
    for i in range(0, len(woord)):
        if gok[i] == woord[i]:
            mes += woord(i).upper
        elif gok[i] != woord[i] and gok[i] in woord:
            mes += gok[i]
        else:
            mes += '.'

    return mes

print(hint('spoed', 'depri'))