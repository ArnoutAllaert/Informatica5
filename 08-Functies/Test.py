def splits(getal):
    d = getal % 10
    getal = getal // 10
    c = getal % 10
    getal = getal // 10
    b = getal % 10
    getal = getal // 10
    a = getal % 10
    return a, b, c, d

def oplopende_cijfers(a, b, c, d):
    s1 = min(a, b, c, d)
    s4 = max(a, b, c, d)
    #middenste getallen bepalen
    k23 = max(min(a, b), min(b, c), min(a, c))
    k32 = a + b + c + d - s1 - s4 - k23
    # volgorde middenste getallen
    s2 = min(k23, k32)
    s3 = max(k23, k32)
    return s1, s2, s3, s4

def op_af_getallen(a, b, c, d):
    return str(a) + str(b) + str(c) + str(d), str(d) + str(c) + str(b) + str(a)

def verschil(af, op):
    uitkomst = str(int(af) - int(op))
    while len(uitkomst) < 4:
        uitkomst = '0' + uitkomst
    return uitkomst

def kaprekar(getal):
    uitkomst = ''
    while getal != 6174:
        a, b, c, d = splits(getal)
        w, x, y, z = oplopende_cijfers(a, b, c, d)
        op, af = op_af_getallen(w, x, y, z)
        v = verschil(af, op)
        uitkomst  += af + ' - ' + op + ' = ' + v

        getal = int(v)

        if getal != 6174:
            uitkomst += '\n'
    return uitkomst

print(kaprekar(5342))