from math import sqrt

def binnen_of_buiten(m, c, p):
    #straal = d(m,c)
    r = sqrt((m[0] - c[0]) ** 2 + (m[1] - c[1]) ** 2)
    #d(m,t)
    d_mp = sqrt((m[0] - p[0]) ** 2 + (m[1] - p[1]) ** 2)
    if r == d_mp:
        mes = 'op'
    elif r > d_mp:
        mes = 'binnen'
    else:
        mes =  'buiten'

    return mes, round(d_mp, 4)

print(binnen_of_buiten((17, 31),(-10, 6),(-6, 26)))