def splits(n):
    a = n // 1000
    b = (n - (a * 1000)) // 100
    c = (n - (a * 1000) - (b * 100)) // 10
    d = n - (a * 1000) - (b * 100) - (c * 10)
    cijfers = a, b, c, d
    return cijfers

def oplopende_cijfers(a,b,c,d):
    g1 = min(a,b,c,d)
    g2 = max(min(a,b,c),min(b,c,d),min(a,b,d),min(a,c,d))
    g3 = min(max(a,b,c),max(b,c,d),max(a,b,d),max(a,c,d))
    g4 = max(a,b,c,d)
    return g1, g2, g3, g4

def op_af_getallen(a,b,c,d):
    oprij = str(a)+str(b)+str(c)+str(d)
    afrij = str(d)+str(c)+str(b)+str(a)
    return oprij, afrij

def verschil(a,b):
    verschil = str(int(a) - int(b))
    return verschil

def kaprekar(n):
    mes =''
    a = n // 1000
    b = (n - (a * 1000)) // 100
    c = (n - (a * 1000) - (b * 100)) // 10
    d = n - (a * 1000) - (b * 100) - (c * 10)
    g1 = min(a, b, c, d)
    g2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
    g3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
    g4 = max(a, b, c, d)
    oprij = str(g1) + str(g2) + str(g3) + str(g4)
    afrij = str(g4) + str(g3) + str(g2) + str(g1)

    if int(afrij) - int(oprij) == 6174:
        mes = '{} - {} = {}'.format(afrij, oprij, int(afrij) - int(oprij))
    else:

        while int(afrij) - int(oprij) != 6174:
            mes += '{} - {} = {}\n'.format(afrij, oprij, int(afrij) - int(oprij))
            n = int(afrij) - int(oprij)
            a = n // 1000
            b = (n - (a * 1000)) // 100
            c = (n - (a * 1000) - (b * 100)) // 10
            d = n - (a * 1000) - (b * 100) - (c * 10)
            g1 = min(a, b, c, d)
            g2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
            g3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
            g4 = max(a, b, c, d)
            oprij = str(g1) + str(g2) + str(g3) + str(g4)
            afrij = str(g4) + str(g3) + str(g2) + str(g1)
        a = n // 1000
        b = (n - (a * 1000)) // 100
        c = (n - (a * 1000) - (b * 100)) // 10
        d = n - (a * 1000) - (b * 100) - (c * 10)
        g1 = min(a, b, c, d)
        g2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
        g3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
        g4 = max(a, b, c, d)
        oprij = str(g1) + str(g2) + str(g3) + str(g4)
        afrij = str(g4) + str(g3) + str(g2) + str(g1)
        mes += '{} - {} = {}'.format(afrij, oprij, int(afrij) - int(oprij))
    return mes




print(kaprekar(5432))