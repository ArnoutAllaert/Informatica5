#def is_palindroom(woord):
    #mes = True
    #if len(woord) == 1:
        #mes = True
    #else:
        #for i in range(0, len(woord)//2):
            #if woord[i] == woord[len(woord) -1 - i] and mes != False:
                #mes = True
            #else:
                #mes = False
    #return mes


def palindroom(woord):
    #return woord == woord[:: -1]   dit is effficientst, maar niet de oefening
    i = 0
    while woord[i] == woord[ -i -1] and i < (len(woord)) // 2:
        i += 1

    return i == (len(woord) // 2)

print(palindroom(10000 * 'k'))