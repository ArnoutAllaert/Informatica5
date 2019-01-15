def is_palindroom(woord):
    mes = True
    if len(woord) == 1:
        mes = True
    else:
        for i in range(0, len(woord)//2):
            if woord[i] == woord[len(woord) -1 - i] and mes != False:
                mes = True
            else:
                mes = False
    return mes


print(is_palindroom('winstoogmerk'))