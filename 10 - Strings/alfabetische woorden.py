#def positie_laagste_ascii(woord):
    #laag = 'z'
    #for letter in woord:
        #if ord(letter) < ord(laag):
            #laag = letter
    #return woord.find(laag)

#def sorteer(woord):
    #gesorteerd = ''
    #for letter in woord:
        #laag = 'z'
        #for letter in woord:
            #if ord(letter) < ord(laag):
                #laag = letter

        #gesorteerd += laag
        #a = woord.find(laag)
        #woord = woord[0:a] + woord[a + 1:]
    #return gesorteerd

#def is_alfabetisch(woord):
    #if sorteer(woord) == woord:
        #mes = True
    #else:
        #mes = False
    #return mes

def positie_laaagste_ascii(tekst):
    p_laagste = 0
    ord_laagste = ord(tekst[0])

    for i in range(1, len(tekst)):
        ord_huidige = ord(tekst[i])
        if ord_huidige < ord_laagste:
            p_laagste = i
            ord_laagste = ord_huidige
    return p_laagste

def sorteer(tekst):
    s_tekst = ''

    while len(tekst) > 0:
        i = positie_laaagste_ascii(tekst)
        s_tekst += tekst[i]
        tekst = tekst[:i] + tekst[i + 1:]
    return s_tekst

def is_alfabetisch(tekst):
    return tekst == sorteer(tekst)

print(is_alfabetisch('vincent.vangogh@gmail.com'))