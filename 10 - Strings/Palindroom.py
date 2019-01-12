def is_palindroom(woord):
    k = 0
    if len(woord) == 1:
        mes = True
    else:
        for i in range(0, len(woord)//2):
            if woord[i] == woord[len(woord) -1 - i] and k < 1000:
                mes = True
            else:
                mes = False
                k += 1000
    return mes



print(is_palindroom('winstoogmerk'))